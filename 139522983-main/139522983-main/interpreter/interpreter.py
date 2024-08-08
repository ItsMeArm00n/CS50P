n=input("Expression: ")
x,y,z=n.split()
if y == "+" :
    print(float(x)+float(z))
elif y=="-":
    print(float(x)-float(z))
elif y=="/" :
    print(float(x)/float(z))
else :
    print(float(x)*float(z))
