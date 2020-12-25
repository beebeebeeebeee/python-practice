import random

def gen_single(length):
    s = set(range(1, 49))
    choose = []
    while length > 0:
        out = random.choice(list(s))
        s.remove(out)
        choose.append(out)
        length -= 1
    choose.sort()
    return choose

def get_lists(length, each_length):
    choose = []
    while length > 0:
        choose.append(gen_single(each_length))
        length -= 1
    return choose

print(get_lists(2,6))