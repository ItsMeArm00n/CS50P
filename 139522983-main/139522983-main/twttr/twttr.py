def main():
    txt=input("Input: ")
    z=shorten(txt)
    print(f"Output: {z}")


def shorten(word):
    x=["a","e","i","o","u"]
    new=""
    for i in word:
        if not i.lower() in x:
            new+=i
    word=new
    return word

if __name__ == "__main__":
    main()
