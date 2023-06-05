import sys
from pyfiglet import Figlet
import random

def getText():
    return input("Input: ")

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 3:
        if sys.argv[1] in ("-f", "--font"):
            font = sys.argv[2]
            if font in fonts:
                figlet.setFont(font=font)
                text = getText()
                rendered_text = figlet.renderText(text)
                print(rendered_text)
                sys.exit(0)
            else:
                print("Invalid usage")
                sys.exit(1)
        else:
            print("Invalid usage")
            sys.exit(1)

    elif len(sys.argv) == 1:
        randfont = random.choice(fonts)
        figlet.setFont(font=randfont)
        text = getText()
        rendered_text = figlet.renderText(text)
        print(rendered_text)
        sys.exit(0)
    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == "__main__":
    main()
