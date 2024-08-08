def main():
    while True:
        n = input("Fraction: ")
        try:
            percentage = convert(n)
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)

    grade = gauge(percentage)
    print(grade)

def convert(fraction):
    while True:
      try:
          x, y = fraction.split("/")
          x = int(x)
          y = int(y)
          z = (x / y) * 100
          return round(z)
      except (ValueError, ZeroDivisionError) :
          pass

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
