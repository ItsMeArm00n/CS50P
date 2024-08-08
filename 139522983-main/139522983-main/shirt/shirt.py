import sys
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith((".png",".jpg",".jpeg")) and not sys.argv[2].endswith((".png",".jpg",".jpeg")) :
    sys.exit("Invalid output")

if sys.argv[1].split(".")[-1].lower()!=sys.argv[2].split(".")[-1].lower():
    sys.exit("Input and output have different extensions")

try:
    img=Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    S=shirt.size
    final=ImageOps.fit(img,S)
    final.paste(shirt,shirt)
    final.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
