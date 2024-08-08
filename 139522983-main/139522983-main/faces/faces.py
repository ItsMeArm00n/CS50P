def convert(x):
    a=":)"
    b=":("
    if a in x and b in x :
        y=x.replace(":)","🙂")
        print(y.replace(":(","🙁"))
    elif b in x :
        print(x.replace(":(","🙁"))
    elif a in x:
        print(x.replace(":)","🙂"))
n=input("")
convert(n)
