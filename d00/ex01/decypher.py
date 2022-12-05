import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:

        print("".join(word[0].upper() for word in sys.argv[1].split()))
