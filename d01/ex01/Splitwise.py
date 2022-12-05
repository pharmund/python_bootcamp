from copy import deepcopy

def empty(purse:dict):
    new = deepcopy(purse)
    for key, v in new.items():
        if key != "gold_ingots":
            return
        new[key] = 0
    return new

def add_ingot(purse:dict):
    new = deepcopy(purse)
    for key, v in new.items():
        if key != "gold_ingots":
            return
        new[key] += 1
    return new

def get_ingot(purse:dict):
    new = deepcopy(purse)
    for key, v in new.items():
        if key != "gold_ingots":
            return
        if new[key] == 0:
            return new
        new[key] -= 1
    return new

def split_booty(*purses):
    i = 0
    d = {"gold_ingots": 0}
    for p in purses:
        for key, v in p.items():
            if key == "gold_ingots":
                d = empty(p)
                i += p[key]
    a = empty(d)
    b = empty(d)
    c = empty(d)
    if i == 0:
        return a, b, c
    if i % 3 == 0:
        x = i / 3
        while x != 0:
            a = add_ingot(a)
            b = add_ingot(b)
            c = add_ingot(c)
            x -= 1
        return a, b, c
    else:
        x = round(i / 3)
        while x != 0:
            a = add_ingot(a)
            b = add_ingot(b)
            c = add_ingot(c)
            x -= 1
        a = get_ingot(a)
        return a, b, c

if __name__ == '__main__':
    print(split_booty({"gold_ingots":3}, {"gold_ingots":2} , {"apples":10}))
    print(split_booty({"gold_ingots": 3}, {"gold_ingots": 3}, {"apples": 10}))
    print(split_booty({"gold_ingots": 3}, {"gold_ingots": 3}, {"apples": 10}, {"gold_ingots": 8}))