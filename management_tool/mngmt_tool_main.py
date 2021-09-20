
#!/usr/bin/python3
import os
from mngmt_fun import *
def main_menu():
    
    print('1.Assign ip address')
    print('2.Delete ip address')
    print('3.Display ip adress')
    print('4.Display all interfaces')
    print('5.Configure Routing')
    print('6.Turn On/Off interface')
    print('7.Add ARP entry')
    print('8.Delete ARP Entry')
    print('9.Restart Network')
    print('10.Change hostname')
    print('11.Add DNS server entry')
    print('12.Exit')
    


while True:
    main_menu()
    ch = int(input('Enter choice : '))
    if ch == 1:
        ip_cmd()

    elif ch == 2:
        dlt_cmd()

    elif ch == 3:
        disp_ip()

    elif ch == 4:
        disp_interface()

    elif ch == 5:
        config_routing()

    elif ch == 6:
        On_Off_interface()

    elif ch == 7:
        add_ARP_entry()

    elif ch == 8:
        del_arp()

    elif ch == 9:
        network_restart()

    elif ch == 10:
        change_host_name()

    elif ch == 11:
        add_dns_server()

    elif ch == 12:
        break

    else:
        print('oops ! Wrong option,  please choose correct option below ')
