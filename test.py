#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

from time import sleep, ctime
import thread
loops = [4,2]
# def loop0():
#     print 'start loop 0 at:', ctime()
#     sleep(4)
#     print 'loop 0 done at:', ctime()
#
# def loop1():
#     print 'start loop 1 at:', ctime()
#     sleep(2)
#     print 'loop 1 done at:', ctime()
#
# def main():
#     print 'start:', ctime()
#     # loop0()
#     # loop1()
#     thread.start_new_thread(loop0, ())
#     thread.start_new_thread(loop1, ())
#     sleep(6)
#     print 'all end:', ctime()
#
# if __name__ == '__main__':
#     main()
def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    #解锁
    lock.release()
def main():
    print 'starting at:', ctime()
    locks =[]
#以loops 数组创建列表，并赋值给nloops
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()
        #锁定
        lock.acquire()
        #追加到locks[]数组中
        locks.append(lock)
    #执行多线程
    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
    for i in nloops:
        while locks[i].locked():
            pass
    print 'all end:', ctime()

if __name__ == '__main__':
    main()