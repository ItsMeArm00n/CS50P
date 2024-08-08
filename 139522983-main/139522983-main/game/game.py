import random
while True:
    try:
        n=int(input("Level: "))
        if n>0:
            break
        else:
            continue
    except:
        pass
x=random.randint(1,n)
while True:
    try:
        g=int(input("Guess: "))
        if g>x :
            print("Too large!")
        elif g<x :
            print("Too Small!")
        else:
            print("Just right!")
            break
    except:
        pass
