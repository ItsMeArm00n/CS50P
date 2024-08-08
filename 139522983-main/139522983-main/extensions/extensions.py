n=input("File name: ").lower().strip()
if ".gif" in n:
    print("image/gif")
elif ".jpg" in n or ".jpeg" in n :
    print("image/jpeg")
elif ".png" in n :
    print("image/png")
elif ".pdf" in n :
    print("application/pdf")
elif ".txt" in n :
    print("text/plain")
elif ".zip" in n :
    print("application/zip")
else :
    print("application/octet-stream")
