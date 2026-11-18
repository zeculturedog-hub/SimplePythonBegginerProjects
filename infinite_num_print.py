import random

def random_pin():
    i = 0
    password = []
    while i < 11:                   
        password.append(random.randint(0, 9))
        i += 1
    print(f"\
    {password[0]}\
    {password[1]}\
    {password[2]}\
    {password[3]}\
    {password[4]}\
    {password[5]}\
    {password[6]}\
    {password[7]}\
    {password[8]}\
    {password[9]}\
    {password[0]}\
    {password[1]}\
    {password[2]}\
    {password[3]}\
    {password[4]}\
    {password[5]}\
    {password[6]}\
    {password[7]}\
    {password[8]}\
    {password[9]}\
    {password[5]}\
    {password[6]}\
    {password[7]}\
    {password[8]}\
    {password[9]}\
    {password[10]}")
    
def pin_random():
    while True:
        random_pin()

pin_random()