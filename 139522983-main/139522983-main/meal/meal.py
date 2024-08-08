def main():
    n=input("What time is it? ")
    t=convert(n)
    if t >= 7.00 and t <= 8.00:
        print("breakfast time")
    elif t >= 12.00 and t <= 13.00:
        print("lunch time")
    elif t >= 18.00 and t <= 19.00:
        print("dinner time")
def convert(time):
    x,y=time.split(":")
    y=float(y)/60
    time = float(x)+y
    return time

if __name__ == "__main__":
    main()
