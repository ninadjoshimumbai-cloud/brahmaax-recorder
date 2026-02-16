import requests
import csv
from datetime import datetime
import os

# Stooq NIFTY API (works on GitHub)
url = "https://stooq.com/q/l/?s=nifty&i=1"

response = requests.get(url)

text = response.text.strip()

# format: SYMBOL,DATE,TIME,OPEN,HIGH,LOW,CLOSE,VOLUME
parts = text.split(",")

price = parts[6]  # CLOSE price

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
