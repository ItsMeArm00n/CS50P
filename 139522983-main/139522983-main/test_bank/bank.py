def main():
    n=input("Greating: ").strip().lower()
    print(f"${value(n)}")

def value(greeting):
    z="hello"
    if greeting==z or z in greeting:
        return 0
    elif greeting[0]=="h" or greeting[0]=="H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
