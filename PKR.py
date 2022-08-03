import requests
from bs4 import BeautifulSoup
from datetime import date
from os import popen

  
def get_rate():
    URL = "https://www.google.com/search?client=firefox-b-d&q=usd+to+pkr"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    mydivs = soup.find_all("div", {"class": "BNeawe iBp4i AP7Wnd"})[0]
    rate = mydivs.find("div", class_="BNeawe iBp4i AP7Wnd").text
    return rate


def format_csv(prev_data):
    date_data = []
    rate_data = []
    for row in prev_data:
        data = (row.replace("\n", "").split(", "))
        date_data.append(data[0])
        rate_data.append(data[1])
    return (date_data, rate_data)


def save_get_data():
    today = date.today().strftime("%B %d& %Y   ")
    PKR_file_path = popen("echo %userprofile%", "r").read()[:-1] + "\\PKR.csv"
    PKR_file = open(PKR_file_path, "a+")
    PKR_file.seek(0)
    prev_data = PKR_file.readlines()[::-1]
    date_data, rate_data = format_csv(prev_data)

    if (today not in date_data):
        rate = get_rate()
        today_data = f"{today}, {rate}\n"
        PKR_file.seek(0)
        PKR_file.write(today_data)
    else:
        today_data = None
    PKR_file.close()
    return (date_data, rate_data, today_data)


date_data, rate_data, today_data = save_get_data()
if today_data: print(today_data.replace(", ", " ").replace("&", ","))
print("########################################################")
print("PREVIOUS DATA")
for i in range(len(date_data)):
    print(date_data[i].replace("&", ", "), rate_data[i])
print("########################################################")

while 1:
    input()