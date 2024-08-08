import requests
from sys import argv

if len(argv)!=2:
    exit("Missing command-line argument")

try:
    p=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate_float"]
    n=float(argv[1])

except requests.RequestException:
    exit("Command-line argument is not a number")
print(f"${n*p:,.4f}")
