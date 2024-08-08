import tabulate
import sys
import csv


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
m=[]
try:
    with open(sys.argv[1],"r") as f:
        n=csv.reader(f)
        for i in n:
            m.append(i)
    print(tabulate.tabulate(m[1:], headers=m[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
