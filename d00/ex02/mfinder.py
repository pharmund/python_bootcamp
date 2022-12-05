data = []

def check(data):
    if len(data) != 3:
        print('Error')
        return
    
    for line in data:
        if line[-1] == '\r':
            line = line[:-1]

        if len(line) != 5:
            print ('Error')
            return


    if (data[0][0] and data[0][4] == '*') and (data[0][1] and data[0][2] and data [0][3] != '*') \
        and (data[1][0] and data[1][1] and data[1][3] and data [1][4] == '*') and (data[1][2]  != '*') \
            and (data[2][0] and data[2][2] and data[2][4]  == '*') and (data[2][1] and data [2][3] != '*'):
            print ('True')
    else:
        print ('Error')
        return


if __name__ == '__main__':
    while 1:
        try:
            s = input()
        except EOFError:
            break
        data.append(s)

check(data)
