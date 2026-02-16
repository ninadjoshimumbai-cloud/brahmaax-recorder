import requests
import csv
from datetime import datetime
import os

url = "https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

data = response.json()

price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]

now = datetime.utcnow()

date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

file = "brahmaax_candles.csv"

exists = os.path.exists(file)

with open(file, "a", newline="") as f:

    writer = csv.writer(f)

    if not exists:
        writer.writerow(["Date", "Time", "Price"])

    writer.writerow([date, time, price])

print("Recorded:", date, time, price)
