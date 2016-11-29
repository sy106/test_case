#!/usr/bin/env python
#################################################################
#
# Module : ELF2FW
# Purpose: Converts an ELF to a legacy firmware
#
#################################################################
#
#  Copyright (c) 2011 SEQUANS Communications.
#  All rights reserved.
#  
#  This is confidential and proprietary source code of SEQUANS
#  Communications. The use of the present source code and all
#  its derived forms is exclusively governed by the restricted
#  terms and conditions set forth in the SEQUANS
#  Communications' EARLY ADOPTER AGREEMENT and/or LICENCE
#  AGREEMENT. The present source code and all its derived
#  forms can ONLY and EXCLUSIVELY be used with SEQUANS
#  Communications' products. The distribution/sale of the
#  present source code and all its derived forms is EXCLUSIVELY
#  RESERVED to regular LICENCE holder and otherwise STRICTLY
#  PROHIBITED.
#
#################################################################
from plib.fw.convert import elfinfw, elf2fw, fw2elf
from plib.fw.fff import elf2flash, elfPartialFff,fff2elf
from pyu import process_cli, get_option, options, CliException

import os, sys, array, getopt

ENC_OPTIONS = [
    (None, "password=", "FW key."),
    (None, "bootkey=", "Boot key."),
    ]

def __import (name, iName):
    import imp
    path = os.path.join(os.path.dirname(__file__), name)
    globals()[iName] = imp.load_source(iName, path + "_.py", open(path, "r"))

__import("boot-config", "mBC")
__import("flash-builder", "mFB")

# -------------------------------------------------// Utility /__________________________________
def abort (msg):
	sys.stderr.write("Error: " + msg + "\n")
	sys.exit(1)

def warn(msg):
	sys.stderr.write("Warn: " + msg + "\n")

class Error(Exception): pass

class odict(object):
	def __init__ (self):
		self.__dict = {}
		self.__order = []

	def __setitem__ (self, key, value):
		self.__dict[key] = value
		self.__order.append(key)

	def iteritems (self):
		for key in self.__order:
			yield key, self.__dict[key]

	def __len__ (self):
		return len(self.__dict)

def parseOffset (value):
	offset = int(value, 0)
	tOffset = offset & 0x1FFFFFFF
	if (offset % (1 << 20)) != 0:
		raise CliException("offset is not mebibyte (2^20) aligned")
	elif tOffset < (22 << 20):
		warn("!?! offset < 22 MiB is not allowed but allowed as unpack does not offset back acpu binary !?!")
	return offset

def get_sector_size(chips, region):
    for c in chips:
        for r in c['regions']:
            if r['id'] == region:
                return c['sectorSize']
    raise Error('Region not found')

# -------------------------------------------------// CLI /______________________________________
@options(ENC_OPTIONS)
def do_convert (options, argv):
	"""Converts an ELF to legacy firmware format\nusage: convert %s <chip> <elf> <firmware>

Converts an ELF to legacy firmware format.

Arguments:
 * chip:        Chip name
 * elf:         ELF to parse
 * firmware:    Firmware to create

"""
        password = get_option("password")
        bootkey = get_option("bootkey")

	if len(argv) < 3:
		raise CliException("Missing arguments")

	chip, elfFile, fwFile = argv[:3]
	image = array.array("c", open(elfFile, "rb").read())
	content = elf2fw(chip, image, password, bootkey)

	outputFw = open(fwFile, "wb")
	content.tofile(outputFw)
	outputFw.close()

def do_rasterize (argv):
	"""Creates an image suitable for firmware-from-flash\nusage: rasterize %s [<options>] [<sectorSize>|<config>] <bcpu_elfs...> [<bcpu_elf1>] [-- <acpu>:[<bootline>]...] <image> 

For firmware-from-flash (FFF), creates a rasterized image than can be directly 
flashed to the FFF region. Multiple ELF images can be included, in such a 
case on target tools allow for selecting which to use.

Rasterized image includes file names given on command line to facilitate
on target ELF switching. These names can be overridden by providing a 
list using the -d option.

Options:
 * --bcpu-only	If given disable ACPU, booting only BCPU (ACPU can be 
                later re-enabled).
 * -d<file>     If given reads file (one line per ELF) instead of file 
                names for descriptions.
 * --aoffset=	Changes the base offset of the ACPU (default 0x21600000)
                Must be mebibyte aligned and larger than or equal 
                to 22 MiB.
 * --validate   If given mark the FW as validated.
 * --boot=      Default boot boot type(default FFF).

Arguments:
 * sectorSize:  NVRAM sector size. The suffix k can be used to express size in kibibytes.
 * config:      Configuration file to parse.
 * bcpu_elfs:   List of at most 2 baseband CPU ELFs, first ELF given will be booted.
 * acpu:	 	Application CPU ELF, first ELF given will be booted 
                unless disabled with --bcpu-only.
 * bootline: 	Optional file containing bootline to be passed to ACPU
 * image:       Image to create

"""
	dFile = None
	bcpuOnly = False
	aoffset = 0x21600000
	opts, args = getopt.getopt(argv, "d:b", ["bcpu-only", "aoffset=", "validate", "boot="])
	validate = False
	fff = True
	for o, a in opts:
		if o == "-d":
			dFile = a
		elif o in ("-b", "--bcpu-only"):
			bcpuOnly = True
		elif o == "--aoffset":
			aoffset = parseOffset(a)
		elif o == "--validate":
			validate = True
		elif o == "--boot":
			bootType = a.lower()
			if bootType not in ('fff', 'ffh'):
			    raise CliException("Invalid boot type '%s'" % a)
			if bootType == 'ffh':
			    fff = False
		else:
			raise CliException("Invalid argument '%s'" % o)
			exit(0)

	if len(args) < 3:
		raise CliException("Missing arguments")

	if os.path.exists(args[0]):
		config = args[0]
		try:
			info = mBC.parse(open(config, "r").read(), config)
			chips = mFB.get_flash_chips(info['psi']['mtdDesc'])
			sSize = get_sector_size(chips, 'PSI_MTD_REGION_FFF')
		except Error, e:
			abort(str(e))
	else:
		sSize = args[0]
		if sSize[-1] in ("k", "K"):
			sSize = int(sSize[:-1], 0) * 1024
		else:
			sSize = int(sSize, 0)

	args = args[1:]
	output = args[-1]
	try:
		index = args.index("--")
		bcpus = args[:index]
		acpus = args[index + 1:-1]
	except ValueError:
		bcpus = args[:-1]
		acpus = []

	if (len(bcpus) > 2) or (len(acpus) > 2):
		raise CliException("More than 2 firmwares per CPU")

	if dFile != None:
		names = open(dFile, "rb").readlines()
	else:
		names = map(os.path.basename, bcpus)
		names += map(lambda n: os.path.basename(n.split(":")[0]), acpus)

	bElfs = odict()
	for index,elf in enumerate(bcpus):
		bElfs[names[index]] = array.array("c", open(elf, "rb").read())

	aInfo = {}
	aElfs = odict()
	for index,elf in enumerate(acpus):
		if ":" in elf:
			elf, info = elf.split(":")
			aInfo[names[len(bcpus) + index]] = array.array("c", open(info, "rb").read())
		aElfs[names[len(bcpus) + index]] = array.array("c", open(elf, "rb").read())

	bin = elf2flash(sSize, bElfs, aoffset, aElfs, aInfo, bcpuOnly, validate, fff)
	open(output, "wb").write(bin)

def do_fffconvert2elf (argv):
	"""convert fff file to elf format\nusage: fffconvert2elf %s  <fff> <elf> 

	Arguments:
	 * elf: 		Firmware image.
	 * fff:		fff image

"""
	if len(argv) < 2:
		raise CliException("Missing arguments")

	file, output = argv[0:2]
	eData = array.array("c", open(file, "rb").read())
	bin = fff2elf(eData)
	open(output, "wb").write(bin)



def do_fffpartial (argv):
	"""Creates an partial FFF image of a firmware\nusage: fffpartial %s [<options>] <elf> <image> 

For firmware-from-flash (FFF), creates a partial image of a firmware that can
be used to add or replace a firmware within a preexisting FFF installation.

Writing this image as-is to the flash will not have the desired effect. 
Additional bookkeeping is required.

Options:
 * -a			Indicate that ELF is for the ACPU & should have its base
				offset relocated.
 * --aoffset=	Changes the base offset of the ACPU (default 0x21600000)
                Must be mebibyte aligned and larger than or equal 
                to 22 MiB. Implies '-a'.

Arguments:
 * elf: 		Firmware image.
 * image:       Image to create

"""
	isAcpu = False
	aoffset = 0x21600000
	opts, args = getopt.getopt(argv, "a", ["aoffset="])
	for o, a in opts:
		if o == "-a":
			isAcpu = True
		elif o == "--aoffset":
			aoffset = parseOffset(a)
			isAcpu = True
		else:
			raise CliException("Invalid argument '%s'" % o)
			exit(0)

	if len(args) < 2:
		raise CliException("Missing arguments")

	file, output = args[0:2]
	eData = array.array("c", open(file, "rb").read())
	bin = elfPartialFff(eData, aoffset if isAcpu else None)
	open(output, "wb").write(bin)

def do_unpack (argv):
	"""Unpacks one or two ELF images from a firmware\nusage: %s unpack <firmware> <bcpu.elf> [<acpu.elf>] 

Unpacks one or two ELF images from a firmware.

Arguments:
 * firmware:    Firmware to unpack
 * bcpu.elf:    Baseband CPU elf to get
 * acpu.elf:    Application CPU elf to get

"""
	if not len(argv) in [2, 3]:
		raise CliException("Missing arguments")

	fw = argv.pop(0)
	bcpu = argv.pop(0)

	if len(argv) == 1:
		acpu = argv.pop(0)
	else:
		acpu = None

	fw = array.array("c", open(fw, "rb").read())

	raw1,raw2 = fw2elf(fw)

	if not raw1:
		raise CliException("Bad firmware")

	if raw2:
		raw2.tofile(open(bcpu, "wb"))
		if acpu:
			raw1.tofile(open(acpu, "wb"))
	else:
		raw1.tofile(open(bcpu, "wb"))

@options(ENC_OPTIONS)
def do_pack (options, argv):
	"""Packs one or two ELF images into a firmware\nusage: pack %s <chip> <bcpu.elf> [<acpu.elf> <offset>] <firmware> 

Packs one or two ELF images into a firmware.

Arguments:
 * chip:        Chip name
 * firmware:    Firmware to create
 * bcpu.elf:    Baseband CPU elf
 * acpu.elf:    Application CPU elf
 * offset:      Base address of application CPU.
                Must be mebibyte aligned and larger than or equal 
                to 22 MiB

The ACPU image will occupy physical memory starting
at <offset> which from the ACPU's point of view is the first
byte of memory (offset 0)

"""
        password = get_option("password")
        bootkey = get_option("bootkey")

	if not len(argv) in [3, 5]:
		raise CliException("Missing arguments")

	chip = argv.pop(0)
	bcpu = argv.pop(0)
	if len(argv) == 3:
		acpu, offset, firmware = argv
		offset = parseOffset(offset)
		acpu = array.array("c", open(acpu, "rb").read())
	else:
		firmware = argv.pop(0)
		acpu = offset = None

	bcpu = array.array("c", open(bcpu, "rb").read())
	fw = elfinfw(chip, bcpu, acpu, offset, password, bootkey)

	outputFw = open(firmware, "wb")
	fw.tofile(outputFw)
	outputFw.close()

if __name__ == "__main__": process_cli()

