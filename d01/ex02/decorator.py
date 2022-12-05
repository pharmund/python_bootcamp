from copy import deepcopy

def decor(func):
    def wraper(args):
        print('SQUEAK')
        return func(args)
    return wraper

@decor
def add_ingot(purse:dict):
    new = deepcopy(purse)
    for key, v in new.items():
        if key != "gold_ingots":
            return
        new[key] += 1
    return new

@decor
def get_ingot(purse:dict):
    new = deepcopy(purse)
    for key, v in new.items():
        if key != "gold_ingots":
            return
        if new[key] == 0:
            return new
        new[key] -= 1
    return new

@decor
def empty(purse:dict):
    new = deepcopy(purse)
    for key, v in new.items():
        if key != "gold_ingots":
            return
        new[key] = 0
    return new

if __name__ == '__main__':
    purse = {"gold_ingots": 1}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))