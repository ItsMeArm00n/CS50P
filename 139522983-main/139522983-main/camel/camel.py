n=input("camelCase: ")
print("snake_case: ",end="")
for i in n :
    if i.isupper():
        print("_" + i.lower(),end="")
    else :
        print(i,end="")
print()
