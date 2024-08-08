list={}
while True:
    try:
        n=input("").upper()
        if n in list:
            list[n]+=1
        else :
            list[n]=1
    except EOFError:
        for i in sorted(list.keys()):
            print(list[i],i)
        break
