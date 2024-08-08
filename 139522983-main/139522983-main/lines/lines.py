import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")
x=0
y=0
try:
    with open(sys.argv[1],"r") as n:
        for i in n:
            x+=1
            if i.lstrip().startswith("#"):
                y+=1
            elif len(i.strip())==0:
                y+=1
        print(f"{x-y}")
except FileNotFoundError:
    sys.exit("File does not exist")


