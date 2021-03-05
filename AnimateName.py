from sys import stdout
from time import sleep as sl


def printf(data):
	stdout.write(data)
	stdout.flush()

a = ['/', '-',  '\\', '|', '-', '|']
string = "shail hacker"
x = 0
point = 0
for i in range(1000):
	for n in range(len(string)):
		if n == point:
			char = string[n].upper()
		else:
			char = string[n]
		printf(char)
	printf("%c\r" % (a[x]))
	sl(0.2)
	x += 1
	point += 1
	if x>=len(a):
		x = 0
	if point >= len(string):
		point = 0
