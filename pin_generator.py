import random

def random_pin():
    i = 0
    password = []
    while i < 6:                   
        password.append(random.randint(0, 9))
        i += 1
    print(f"\
    {password[0]}\
    {password[1]}\
    {password[2]}\
    {password[3]}\
    {password[4]}\
    {password[5]}")
    
def pin_random():
    j = 0
    while j < 10:
        random_pin()
        j += 1

pin_random()
           