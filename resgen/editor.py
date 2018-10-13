import json
import sys

data = dict()
try:
    filename = sys.argv[1]
except IndexError:
    print('pass in a filename!')
    sys.exit(1)
with open(filename, 'r') as f:
    data = json.loads(f.read())

def get_choice():
    print("What would you like to do?")
    print("only option right now is to [exit]")
    choice = None
    while choice not in ['exit']:
        choice = input()
    return choice


def main():
    print("This is the resgen resume editor")
    i = None
    while i != 'exit':
        i = get_choice()
    sys.exit(0)

if __name__ == '__main__':
    main()
