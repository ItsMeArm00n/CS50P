import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        time=re.search(r"(([0-9][0-2]*):*([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):*([0-5][0-9])*) (AM|PM)",s)

        if not (re.search(r"(([0-9][0-2]*):*([0-5][0-9])*) (AM|PM) to (([0-9][0-2]*):*([0-5][0-9])*) (AM|PM)",s)):
            raise ValueError
        else :
            x=time.groups()
            start_min=x[2]
            end_min=x[6]
            start_min = start_min if start_min else "00"
            end_min = end_min if end_min else "00"
            if time.group(4)=="AM" and time.group(8)=="PM" :
                if time.group(2)=="12" :
                    return f"00:{start_min} to 12:{end_min}"
                else:
                    start_hour = time.group(2)
                    end_hour = str(int(time.group(6))+12)
                    if len(start_hour)==1:
                        return f"0{start_hour}:{start_min} to {end_hour}:{end_min}"
                    else:
                        return f"{start_hour}:{start_min} to {end_hour}:{end_min}"

            elif time.group(4)=="PM" and time.group(8)=="AM" :
                if time.group(6) == "12":
                    return f"12:{start_min} to 00:{end_min}"
                else :
                    start_hour = str(int(time.group(2))+12)
                    end_hour = time.group(6)
                    if len(end_hour)==1:
                        return f"{start_hour}:{start_min} to 0{end_hour}:{end_min}"
                    else:
                        return f"{start_hour}:{start_min} to {end_hour}:{end_min}"



if __name__ == "__main__":
    main()
