import string
import random

name_lenth = int(input('Enter length of the name:'))
def name_gen():
    name = ''
    for i in range(name_lenth):
        name = name+random.choice(string.ascii_lowercase)
    name = name[0].upper()+name[1:name_lenth]
    return name

print(random.randint(1,3))

#commit from ubuntu
