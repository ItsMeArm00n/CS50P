def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>6 or len(s)<2:
        return False
    if s[0].isalpha()==False or s[1].isalpha()==False:
        return False
    i=0
    while i<len(s):
        if s[i].isalpha()==False:
            if s[i] == "0":
                return False
            else :
                break
        i+=1
    if (s[-1].isdigit()==False and s[-2].isdigit()==True) or (s[-2].isdigit()==False and s[-3].isdigit()==True) or (s[-3].isdigit()==False and s[-4].isdigit()==True):
        return False
    for j in s:
        if j in [",","."," ","?","!"] :
            return False
    return True

if __name__ == "__main__":
    main()
