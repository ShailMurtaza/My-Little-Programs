from scapy.all import *
l1 = IP(src="192.168.0.56", dst="192.168.0.1")
l3 = TCP(sport=(1234), dport=80)
pkt = l1/l3
while True:
	send(pkt, count=1, inter=0.05)
"""
from time import sleep as sl
from socket import socket
s = socket()
host, port = "192.168.0.1", 80
s.connect((host, port))
print("Conected ...")
while True:
	# sl(1)
	s.send("a"*102)
"""
