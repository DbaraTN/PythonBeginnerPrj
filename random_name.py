import string
import random


def name_gen():
    name = ''
    for i in range(4):
        if i == 0:
            name = name+random.choice(string.ascii_uppercase)
        else:
            name = name+random.choice(string.ascii_lowercase)
    return name

print(name_gen())