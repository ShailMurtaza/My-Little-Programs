#!/usr/bin/python
from time import sleep as sl
import readline
import sys


def printf(*arg):
    sys.stdout.write(' '.join(list(map(str, arg))))
    sys.stdout.flush()


def format_time(h, m, s):
    if len(str(h)) == 1:
        h = "0" + str(h)
    if len(str(m)) == 1:
        m = "0" + str(m)
    if len(str(s)) == 1:
        s = "0" + str(s)
    return "{}:{}:{}".format(h, m, s)


def timer(alarm):
    beep = False
    print(alarm)
    h, m, s = 0, 0, 0
    while True:
        try:
            show = format_time(h, m, s)
            if beep and (s%1 == 0):
                # printf("\a")
                pass
            printf(show)

            f = open("/home/shail/Desktop/programming/python/stopwatch", "w")
            f.write(show)
            f.close()
            
            if alarm == show:
                printf("\a")
                beep = True
            sl(1)
            printf("\r")
            s += 1
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1
        except KeyboardInterrupt:
            choice = raw_input("Do you wants to continue or not [Y/N] ").lower()
            if choice == "n":
                break


def set_alarm(time):
    try:
        time = str(eval(time))
    except (NameError, SyntaxError):
        pass
    if time.isdigit():
        time = "::%s" % (time)
    time = time.split(":")
    if (len(time) != 3):
        print("Incorrect Format")
        return

    h, m, s = time
    if (not(h.isdigit()) and h != "") or (not(m.isdigit()) and m != "") or (not(s.isdigit()) and s != ""):
        print("Incorrect Format")
        return

    if not h:
        h = 0
    if not m:
        m = 0
    if not s:
        s = 0
    h, m, s = list(map(int, (h, m, s)))
    while (int(s) >= 60):
        s -= 60
        m += 1
    while (int(m) >= 60):
        m -= 60
        h += 1

    return format_time(h, m, s)


while True:
    try:
        alarm = raw_input("Enter time in [00:00:00] FORMAT: ")
        if alarm == "exit":
            print("BYE! . . .")
            sl(4)
            exit()
    except KeyboardInterrupt:
        sl(4)
    	print("BYE! . . .")
    if not alarm:
        alarm = "00:00:00"
    else:
        alarm = set_alarm(alarm)
    timer(alarm)
