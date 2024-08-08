import sys
from pyfiglet import Figlet
from random import choice
figlet = Figlet()
if len(sys.argv) == 1:
    figlet.setFont(font=choice(figlet.getFonts()))
    print("Output:", figlet.renderText(input("Input: ")), sep="\n")
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    print("Output:", figlet.renderText(input("Input: ")), sep="\n")
else:
    sys.exit("Invalid usage")

