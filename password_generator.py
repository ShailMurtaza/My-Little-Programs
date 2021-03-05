# Random password generator CREATED BY SHAIL
from __future__ import print_function
import random
from os import system
from time import sleep
from threading import Thread

x = 0.3
alpha = "qwertyuioplkjhgfdsazxcvbnm"
sym = r"<>?;:!@#$%^&*()_+=-{}[]\"'|`"


class Done():
	pass


# def anime():
# 	global stop
# 	stop = False
# 	while True:
# 		if stop:
# 			break
# 		system("clear")
# 		print(""" -------------------------------------------
# | Random password generator CREATED BY SHAIL |
#  -------------------------------------------
# """)
# 		sleep(x)
# 		system("clear")
# 		print(""" -------------------------------------------\n
# | Random password generator CREATED BY SHAIL |\n
#  -------------------------------------------
# """)
# 		sleep(x)


def anime():
	global stop
	stop = False
	while True:
		if stop:
			break
		print(""" -------------------------------------------
| Random password generator CREATED BY SHAIL |                    
                                                  
""")
		print("\033[F", end='')
		print("\033[F", end='')
		print("\033[F", end='')
		print("\033[F", end='')
		sleep(x)
		print(""" -------------------------------------------\n                                                        
| Random password generator CREATED BY SHAIL |                       \n
 -------------------------------------------
""")
		print("\033[F", end='')
		print("\033[F", end='')
		print("\033[F", end='')
		print("\033[F", end='')
		print("\033[F", end='')
		print("\033[F", end='')
		sleep(x)


def shuffle():
	funcs = [add_num, add_alpha, add_sym]
	random.shuffle(funcs)
	return funcs


def add_num(key):
	a = str(random.randint(0, 9))
	key.append(a)
	return key


def add_alpha(key):
	choice = random.randint(0, 1)
	b = random.randint(0, (len(alpha) - 1))
	if choice == 0:
		key.append(alpha[b])
	else:
		key.append(alpha[b].upper())
	return key


def add_sym(key):
	c = random.randint(0, (len(sym) - 1))
	key.append(sym[c])
	return key


def gen(length):
	def test(key, length):
		if len(key) >= length:
			raise Done
	key = []
	funcs = shuffle()
	try:
		for i in range(length):
			test(key, length)
			key = funcs[0](key)
			test(key, length)
			key = funcs[1](key)
			test(key, length)
			key = funcs[2](key)
			test(key, length)
	except Done:
		pass
	finally:
		return ''.join(key)


def main():
	global stop
	test = True
	while True:
		try:
		    lenght = input("Enter: ")
		except (NameError, SyntaxError):
		    lenght = random.randint(5, 20)
		finally:
			stop = True
			if test:
				sleep(0.5)
			print(gen(lenght))
			test = False


Thread(target=anime).start()
Thread(target=main).start()
