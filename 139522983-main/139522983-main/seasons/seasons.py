from datetime import date
import sys
import inflect
p=inflect.engine()

def main():
    n=input("Date of Birth: ")
    validate(n)
    print(convert(n))




def convert(input):
    y,m,d=input.split("-")
    t_days=date.today() - date(int(y),int(m),int(d))
    min=t_days.days * 60 * 24
    min=(p.number_to_words(min, andword=""))
    min=min.capitalize()
    return (f"{min} minutes")



def validate(x):
    try:
        y,m,d=x.split("-")
        if len(y)!=4 or len(m)!=2 or len(d)!=2 :
            sys.exit("Invalid Date")
        else:
            pass
    except:
        sys.exit("Invalid Date")

if __name__ == "__main__":
    main()
