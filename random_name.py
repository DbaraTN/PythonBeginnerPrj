import string
import random

name_lenth = int(input('Enter length of the name:'))
def name_gen():
    name = ''
    for i in range(name_lenth):
        if i == 0:
            name = name+random.choice(string.ascii_uppercase)
        else:
            name = name+random.choice(string.ascii_lowercase)
    return name

print(name_gen())