from socket import socket
import readline


def scan(host, port):
	s = socket()
	try:
		s.connect((host, port))
		s.close()
		print("Port {:<7} is open in {}".format(i, host))
	except:
		# print("close")
		pass


host = raw_input("Enter IP to scan: ").split(" ")
print("_______________________________________")
start, end = 1, 9000
for x in host:
	for i in range(start, (end+1)):
		scan(x, i)
	print("_______________________________________")