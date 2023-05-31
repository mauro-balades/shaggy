
import sys
from hunt import hunt

def main(argv):
    if len(argv) == 2:
        name = argv[1]
        hunt(name)
    else:
        print("A name hasn't been defined!")
        print("Usage: social-scout [name]")

if __name__ == "__main__":
    main(sys.argv)