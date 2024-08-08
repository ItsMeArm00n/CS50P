x=50
while x>0:
    print(f"Amount Due: {x}")
    y=int(input("Insert Coin: "))
    if y==25 or y==5 or y==10:
        x=x-y
z=abs(x)
print(f"Change Owed: {z}")
