import os

def available_RAM():
    mem = os.popen('free -m').read()
    print(f'Available memory => {mem} mb')


def load_average():
    cmds = os.popen('cat /proc/loadavg').read()
    print(f"\nload avg => {cmds}")
   

def display_hostname():
    cmd = 'hostnamectl status'
    res = os.popen(cmd).read()
    print(res)


def display_all_process():
    cmd = 'ps -a | wc -l'
    res = os.popen(cmd).read()
    print(f' {res} processes running on system ')


def uptime():

    cmd = os.popen("uptime").read()
    print(f'Uptime ==>  {cmd}')


def main_menu():
    print('1.Display available RAM')
    print('2.Display load average')
    print('3.Display Hostname details')
    print('4.Display All process count')
    print('5.Display uptime')
    print('6.Exit')
while True:
    main_menu()
    ch = int(input('Enter choice : '))
    if ch == 1:
        available_RAM()
    elif ch == 2:
        load_average()
    elif ch == 3:
        display_hostname()
    elif ch == 4:
        display_all_process()
    elif ch == 5:
        uptime()
    elif ch == 6:
        break
    else:
        print('oops ! wrong option')

