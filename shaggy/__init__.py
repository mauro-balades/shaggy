from termcolor import colored, cprint

from shaggy.hunt import hunt
from shaggy.output import output_accounts

import argparse

def print_shaggy():
    print(
        f"""
                                                                                        ░░░░░░░░░░░░░░░░▄▄█▀▀██▄▄░░░░░░░
                                                                                        ░░░░░░░░░░░░░▄█▀▀░░░░░░░▀█░░░░░░
        {colored('          88                                                              ', 'green', attrs=['bold'])}      ░░░░░░░░░░░▄▀░░░░░░░░░░░░░█░░░░░
                  {colored('88', 'green', attrs=['bold'])}                                                                    ░░░░░░░░░▄█░░░░░░░░░░░░░░░█░░░░░
                  {colored('88', 'green', attrs=['bold'])}                                                                    ░░░░░░░██▀░░░░░░░▄▄▄░░▄░█▄█▄░░░░
        {colored(',adPPYba, 88,dPPYba,  ,adPPYYba,  ,adPPYb,d8  ,adPPYb,d8 8b       d8', 'green', attrs=['bold'])}            ░░░░░▄▀░░░░░░░░░░████░█▄██░▀▄░░░
        {colored('I8[    "" 88P´    "8a ""     `Y8 a8"    `Y88 a8"    `Y88 `8b     d8"', 'green', attrs=['bold'])}            ░░░░█▀░░░░░░░░▄▄██▀░░█████░██░░░
        {colored(' `"Y8ba,  88       88 ,adPPPPP88 8b       88 8b       88  `8b   d8´', 'green', attrs=['bold'])}             ░░░█▀░░░░░░░░░▀█░▀█▀█▀▀▄██▄█▀░░░
        {colored('aa    ]8I 88       88 88,    ,88 "8a,   ,d88 "8a,   ,d88   `8b,d8´', 'green', attrs=['bold'])}              ░░░██░░░░░░░░░░█░░█░█░░▀▀▄█▀░░░░
        {colored('`"YbbdP"´ 88       88 `"8bbdP"Y8  `"YbbdP"Y8  `"YbbdP"Y8     Y88´', 'green', attrs=['bold'])}               ░░░░█░░░░░█░░░▀█░░░░▄░░░░░▄█░░░░
                                   {colored('       aa,    ,88  aa,    ,88     d8', 'green', attrs=['bold'])}                 ░░░░▀█░░░░███▄░█░░░░░░▄▄▄▄█▀█▄░░
                                    {colored('       "Y8bbdP"    "Y8bbdP"     d8', 'green', attrs=['bold'])}                  ░░░░░▀██░░█▄▀▀██░░░░░░░░▄▄█░░▀▄░
                                                                                        ░░░░░░▀▀█▄░▀▄▄░▄░░░░░░░███▀░░▄██
                                                                                        ░░░░░░░░░▀▀▀███▀█▄░░░░░█▀░▀░░░▀█
                                                                                        ░░░░░░░░░░░░▄▀░░░▀█▄░░░░░▄▄░░▄█▀
                    By Gonzalo and Mauro                                                ░░░▄▄▄▀▀▀▀▀█▀░░░░░█▄▀▄▄▄▄▄▄█▀▀░░
                   {colored('^^^^^^^^^^^^^^^^^^^^^^', 'red', attrs=['bold'])}                                               ░▄█░░░▄██▀░░░░░░░░░█▄░░░░░░░░░░░                                    
                                                                                        █▀▀░▄█░░░░░░░░░░░░░░▀▀█▄░░░░░░░░
                                                                                        █░░░█░░░░░░░░░░░░░░░░░░█▄░░░░░░░
                                                                                        
                                                                                        
"""
    )


def main():
    parser = argparse.ArgumentParser(description='Search for social media accounts.')
    parser.add_argument('username', metavar='username', nargs='+', type=str,
                    help='Username to search for')
    parser.add_argument('--output', '-o', dest='output',
                    help='Output file for the found accounts')
    args = parser.parse_args()
    print_shaggy()

    
    names = args.username
    accounts = hunt(names)

    if args.output is not None:
        output_accounts(args.output, accounts)

