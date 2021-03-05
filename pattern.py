n = 4  # Put any integer here
col = (n-1) + n
l = []
main = []

main.append(str(n)*col)

x = 1
p = col - 1
y = 0
center = None
i = 0


def replacer(x, y, string):
    # print(string + "This")
    string = list(string)
    string = list(map(int, string))
    for x in range(x, y):
        string[x] = string[x] - 1
    string = list(map(str, string))
    string = ''.join(string)
    return string


while center != "2":
    string = main[y]
    nexxt = replacer(x, p, string)
    main.append(nexxt)
    a = (string[x:p])
    # print(f"{a:<9}{x}-{p}")
    x += 1
    y += 1
    if y != (n-1):
        p -= 1
    else:
        x -= 1
    center = a.strip()

main = main + main[-2::-1]

for i in main:
    print(i)
