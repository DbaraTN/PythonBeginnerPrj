import string
import random


def name_gen():
    l1 = random.choice(string.ascii_uppercase)
    l2 = random.choice(string.ascii_lowercase)
    l3 = random.choice(string.ascii_lowercase)
    l4 = random.choice(string.ascii_lowercase)
    return l1+l2+l3+l4

print(name_gen())