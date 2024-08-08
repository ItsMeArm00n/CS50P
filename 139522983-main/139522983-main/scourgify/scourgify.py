import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")

l=[]
try:
    with open(sys.argv[1],"r") as f:
        n=csv.DictReader(f)
        for i in n:
            x=i["name"].split(",")
            l.append({"first":x[1].lstrip(),"last":x[0],"house":i["house"]})
        with open(sys.argv[2],"w") as f_2:
            y=csv.DictWriter(f_2,fieldnames=["first","last","house"])
            y.writerow({"first":"first","last":"last","house":"house"})
            for j in l:
                y.writerow({"first":j["first"],"last":j["last"],"house":j["house"]})
except FileNotFoundError:
    sys.exit("Could not read",sys.argv[1])
