#!/usr/bin/python
from pyperclip import copy
dragon = (u'\U0001F409')
data = (u"%sShail%s" % (dragon, dragon))
copy(data)
raw_input("Go and Paste")

# from time import sleep as sl
# from threading import Thread
# import os


# def attack():
# 	a = 0
# 	while True:
# 		os.system('start')
# 		sl(0.1)

# def start_attack():
# 	Thread(target=attack).start()

# while 1:
# 	start_attack()
# 	sl(0.01)
