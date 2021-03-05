#!/usr/bin/python
from time import sleep as sl
import sys


def printf(*arg):
    sys.stdout.write(' '.join(list(map(str, arg))))
    sys.stdout.flush()


def pause():
    printf("Press enter to continue")
    raw_input()


def timer(time):
    i = 0
    while True:
        try:
            printf(i)
            sl(1)
            printf("\r")
            i += 1
            if time == i:
                printf("\a")
        except KeyboardInterrupt:
            choice = raw_input("Do you wants to continue or not [Y/N] ").lower()
            if choice == "n":
                break


while True:
    try:
        time = raw_input("Enter time in seconds: ")
        if time == "exit":
            print("\nBye!\n")
            break
    except KeyboardInterrupt:
        print("\nBye!\n")
        exit()
    try:
        time = eval(time)
        print(time)
        timer(time)
    except (NameError, SyntaxError):
        timer(0)
        continue
