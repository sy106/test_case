#!/bin/sh
. /www/manage_if.sh

manage_interface_table=100
manage_ip=''
manage_interface=$(get_manage_if)

if [ "$manage_interface" = "" ];then
    manage_interface=icc0.1121
fi

init_policy_table(){
    table=$1
    table_name=$2

    init_flag=`cat /etc/iproute2/rt_tables|grep $table_name`

    if [ "$init_flag"x  = ""x ];then
        echo $table $table_name >> /etc/iproute2/rt_tables
    fi
}

check_manage_ip(){
    str=`ifconfig $manage_interface`;
    manage_ip=`expr "$str" : '.*inet addr:[[:space:]]*\([0-9.]*\).*'`

    if [ "$manage_ip" = "" ] || [ "$manage_interface" = "" ];then
        echo "policy_route:manage_ip or manage_interface is null"
        exit 1
    fi

    if [ $# -eq 2 ];then
        ip=$1
        interface=$2

        if [ "$ip" != "$manage_ip" ];then
            echo "update_policy_route:ip not equal manage_ip"
            exit 1
        fi

        if [ "$interface" != "$manage_interface" ];then
            echo "update_policy_route:not manage interface"
            exit 1
        fi
        manage_ip=$ip
        manage_interface=$interface
    fi
}

update_policy_route(){
    ip=$1
    interface=$2
    echo "ip:$ip interface:$interface" >>/dev/console
    ip rule del table manage pref $manage_interface_table 2>/dev/null
    ip route del default table manage 2>/dev/null
    ip rule add from $manage_ip table manage pref $manage_interface_table
    ip route add default dev $manage_interface table manage
}

init_policy_table $manage_interface_table manage

action_help(){
    echo "*********** mangage interface policy route operation help ****************"
    echo "update    :update policy route "
    echo "****************************************************"
}

case $1 in
    "update" )
        check_manage_ip $2 $3
        update_policy_route $manage_ip $manage_interface
        ;;
    * )
        action_help
        ;;
esac






