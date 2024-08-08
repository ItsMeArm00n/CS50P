import inflect
p = inflect.engine()
name=[]
while True:
    try:
        n=input("Name: ")
        name.append(n)
    except EOFError:
        break

print("Adieu, adieu, to",p.join(name))
