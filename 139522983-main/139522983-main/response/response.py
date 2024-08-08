import validators

n=input("what's your email address? ")
if validators.email(n):
    print("Valid")
else:
    print("Invalid")
