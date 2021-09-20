import os

def ip_cmd():
	#Assign IP address
	ip=input("Enter ip address to assign : ")
	if len(ip.split('.')) == 4:
		s = os.popen('ip l').read()
		print(s)
		choice=input("Enter interface : ") 
		cmd = f'ip address add {ip} dev {choice}'
		ip_assign = os.popen(cmd).read()
		print(ip_assign)
		print("Ip address assigned successfull")
def dlt_cmd():
	#Delete IP address
	ip=input("Enter ip address to assign : ")
	if len(ip.split('.')) == 4:
		s = os.popen('ip l').read()
		print(s)
		choice=input("Enter interface : ") 
		cmd = f'ip address del {ip} dev {choice}'
		ip_del = os.popen(cmd).read()
		print(ip_del)
		print("Ip address deleted successfull")
def ip_disp():
	#Display IP address
	cmd= f'ip -c -br address'
	res=os.popen(cmd).read()
	print(res)
def disp_interface():
	#Display all interface
	s = os.popen('ip l').read()
        interfaces = s.split('\n')[:-2:2]

	cmd = 'ip l'
#	 interfaces = s.split('\n')[:-2:2]
	res = os.popen(cmd).read()
	print(f'Interface Name :{interface} Details :{res}')
	
def config_routing():
	#Configure routing
	nw_addr = input("Enter network address with mask(nw add/mask) : ")
	gate_way = input("Enter gateway ip address : ") 
	if len(nw_addr.split('.')) == 4 and len(gate_way.split('.')) == 4:
		cmd = f'ip r add {nw_addr} via {gate_way}'
		res = os.popen(cmd).read()
		print(res)
		print("Sucessfull")
def on_off_interface():
	#Turn On/Off interface
	print("Enter 1 for Turn on interface")
	print("Enter 2 for Turn off interface")
	ch = int(input("Enter your choice : "))
	s = os.popen('ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
	interface = s.split('\n')[:-2:2]
	print(interface)
	choice=input("enter interface : ")
	if ch == 1:
		cmd = f'ip link set dev {choice} up'
		res = os.popen(cmd).read()
		print(f'{choice} turned on | Details :{res}')
	elif ch ==2:
		cmd = f'ip link set dev {choice} down'
		res = os.popen(cmd).read()
		print(f'{choice} turned off | Details :{res}')
	else:
		print("Invalid")
		
def add_arp():
	#Add ARP entry
	ip=input("Enter ip address to assign : ")
	if len(ip.split('.')) == 4:
		s = os.popen('ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
		interface = s.split('\n')[:-2:2]
		print(interface)
		choice=input("Enter interface : ")
		arp_cache = os.popen('ip n show | cut -d " " -f5').read()
		cmd=f'ip n add {ip} lladdr {arp_cache} dev {choice} nud permanent'
		res = os.popen(cmd).read()
		print("arp entry added ")

		
def dlt_arp():
	#Delete ARP Entry
	ip = input('Enter ip address : ')
	if len(ip.split('.')) == 4:
        	s = os.popen(
            		'ip l | cut -d":" -f2 | tr -d " " | cut -d" " -f1').read()
        	interfaces = s.split('\n')[:-2:2]
        	print(interfaces)
        	choice = input("Enter interface : ")
        	cmd = f'ip n del {ip} dev {choice}'
        	res = os.popen(cmd).read()
        	console.print('ARP Entry deleted successfully ')
def network_restart():
	#Restart Network
	cmd = 'sudo systemctl restart networking'
	cmd2 = 'sudo systemctl status networking'
	os.popen(cmd).read()
	print('Network services restarted ')
	print(os.popen(cmd2).read())
def change_host():
	#Change hostname
	host_name = input("Enter new host name :")
	cmd = f'hostnamectl set-hostname {host_name}'
	os.popen(cmd).read()
	print(f'new host name {host_name} set successfully ')
def add_dns_server():
	#Add DNS server entry
	print('adding dns server')
	print('first : nameserver 8.8.8.8 write in this format')
	print('second : ctrl + d  to exit ')
	cmd = 'sudo cat  >> /etc/resolv.conf'
	print(os.popen(cmd).read())
	print('Added successfully  ')
