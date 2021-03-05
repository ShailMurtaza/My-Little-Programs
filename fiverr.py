#!/usr/bin/python2
from tabulate import tabulate as table


def good(data, fmt="psql"):
	print(table(data, [""], tablefmt=fmt))

msg = "\nMoney That you will get:"
while True:
	full_data = []
	try:
		print("")
		print("1) Get new order and wants to analysis")
		print("2) US Dollars to PKR")
		choice = raw_input("Enter: ")
		money = float(eval(raw_input("Enter Amount of money: ")))
		print("")
		if choice == '1':
			full_data.append(["Total Money:", "", "%f $" % money])
			money = 80 * money / 100
			full_data.append([msg , "( $ - 20% = 80% )", "%-10f $" % money])
			full_data.append([msg , "( $ x 140 )", "%-10f Rs" % (money*140)])
			full_data.append([msg , "( $ x 150 )", "%-10f Rs" % (money*150)])
			full_data.append([msg , "( $ x 155 )", "%-10f Rs" % (money*155)])
		elif choice == '2':
			full_data.append(["Total Money:", "", "%-10f $" % money])
			full_data.append([msg , "( $ x 140 )", "%-10f Rs" % (money*140)])
			full_data.append([msg , "( $ x 150 )", "%-10f Rs" % (money*150)])
			full_data.append([msg , "( $ x 155 )", "%-10f Rs" % (money*155)])
		good(full_data)
	except (NameError, SyntaxError):
		print("What The Heck!")
