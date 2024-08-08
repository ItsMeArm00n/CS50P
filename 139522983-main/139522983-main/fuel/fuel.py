while True:
  n=input("Fraction: ")
  try:
    x,y=n.split("/")
    x=int(x)
    y=int(y)
    z=x/y
    if z <= 1:
       break
  except(ValueError,ZeroDivisionError):
    pass
amt=z*100
amt=round(amt)
amt=int(amt)
if amt<=1:
  print("E")
elif amt>=99:
  print("F")
else :
  print(f"{amt}%")
