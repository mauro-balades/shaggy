
import sys

from termcolor import colored, cprint
from hunt import hunt

def print_shaggy():
    print(f"""

    
{colored('          88                                                              ', 'green', attrs=['bold'])}      ░░░░░░░░░░░░░░░░▄▄█▀▀██▄▄░░░░░░░
          {colored('88', 'green', attrs=['bold'])}                                                                    ░░░░░░░░░░░░░▄█▀▀░░░░░░░▀█░░░░░░
          {colored('88', 'green', attrs=['bold'])}                                                                    ░░░░░░░░░░░▄▀░░░░░░░░░░░░░█░░░░░
{colored(',adPPYba, 88,dPPYba,  ,adPPYYba,  ,adPPYb,d8  ,adPPYb,d8 8b       d8', 'green', attrs=['bold'])}            ░░░░░░░░░▄█░░░░░░░░░░░░░░░█░░░░░
{colored('I8[    "" 88P´    "8a ""     `Y8 a8"    `Y88 a8"    `Y88 `8b     d8"', 'green', attrs=['bold'])}            ░░░░░░░██▀░░░░░░░▄▄▄░░▄░█▄█▄░░░░
{colored(' `"Y8ba,  88       88 ,adPPPPP88 8b       88 8b       88  `8b   d8´', 'green', attrs=['bold'])}             ░░░░░▄▀░░░░░░░░░░████░█▄██░▀▄░░░
{colored('aa    ]8I 88       88 88,    ,88 "8a,   ,d88 "8a,   ,d88   `8b,d8´', 'green', attrs=['bold'])}              ░░░░█▀░░░░░░░░▄▄██▀░░█████░██░░░
{colored('`"YbbdP"´ 88       88 `"8bbdP"Y8  `"YbbdP"Y8  `"YbbdP"Y8     Y88´', 'green', attrs=['bold'])}               ░░░█▀░░░░░░░░░▀█░▀█▀█▀▀▄██▄█▀░░░
                           {colored('       aa,    ,88  aa,    ,88     d8', 'green', attrs=['bold'])}                 ░░░██░░░░░░░░░░█░░█░█░░▀▀▄█▀░░░░
                            {colored('       "Y8bbdP"    "Y8bbdP"     d8', 'green', attrs=['bold'])}                  ░░░░█░░░░░█░░░▀█░░░░▄░░░░░▄█░░░░
                                                                                ░░░░▀█░░░░███▄░█░░░░░░▄▄▄▄█▀█▄░░
                                                                                ░░░░░▀██░░█▄▀▀██░░░░░░░░▄▄█░░▀▄░
                                                                                ░░░░░░▀▀█▄░▀▄▄░▄░░░░░░░███▀░░▄██
        By Gonzalo and Mauro                                                    ░░░░░░░░░▀▀▀███▀█▄░░░░░█▀░▀░░░▀█
       {colored('^^^^^^^^^^^^^^^^^^^^^^', 'red', attrs=['bold'])}                                                   ░░░░░░░░░░░░▄▀░░░▀█▄░░░░░▄▄░░▄█▀
                                                                                ░░░▄▄▄▀▀▀▀▀█▀░░░░░█▄▀▄▄▄▄▄▄█▀▀░░
                                                                                ░▄█░░░▄██▀░░░░░░░░░█▄░░░░░░░░░░░
                                                                                █▀▀░▄█░░░░░░░░░░░░░░▀▀█▄░░░░░░░░
                                                                                █░░░█░░░░░░░░░░░░░░░░░░█▄░░░░░░░
                                   
""")

def main(argv):
    if len(argv) == 2:
        print_shaggy()

        name = argv[1]
        hunt(name)
    else:
        print("A name hasn't been defined!")
        print("Usage: social-scout [name]")

if __name__ == "__main__":
    main(sys.argv)