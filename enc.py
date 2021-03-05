#!/usr/bin/python

def enc(data):
    a = "abcdefghijklmnopqrstuvwxyz-123456789"
    b = a[::-1]
    c = {}
    d = []
    for i in range(len(a)):
        c[a[i]] = b[i]
    for i in data:
        try:
            d.append(c[i])
        except KeyError:
            d.append(i)
    return (''.join(d)[::-1])


data = raw_input("Enter: ")
print(enc(data))
print(enc(enc(data)))
