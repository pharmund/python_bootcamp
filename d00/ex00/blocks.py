import sys
import re

data = []
new_data = []

def check(data):

    for n in data:
        if n[-1] == '\r':
            n = n[:-1]
        if re.match(r'^[0]{5}[a-z0-9]{27}', n) and len(n) == 32 and n[5] != '0':
            new_data.append(n)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            try:
                s = input()
            except EOFError:
                break
            data.append(s)

check(data)
        
for n in new_data:
    print (n)

