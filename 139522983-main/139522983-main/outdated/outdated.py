months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    n = input("Date: ")
    try:
        x,y,z = n.split("/")
        x = int(x)
        y = int(y)
        z = int(z)
        if 1 <= x <= 12 and 1 <= y <= 31:
            break
    except:
        try:
            a,b,c = n.split(" ")
            if not b.endswith(","):
                continue
            b = b.replace(",","")
            c = int(c)
            for i in range(len(months)):
                if a == months[i]:
                    x = i + 1
                    break
            y = int(b)
            z=c
            if 1 <= x <= 12 and 1 <= y <= 31:
                break
        except:
            pass
print(f"{z}-{x:02}-{y:02}")
