import random

while True:
    your_name = input("Enter your desired name: ")
    choices = ["robot","psycho","omni","crank","toxic"]

    nickname = your_name + " " + random.choice(choices)

    print(nickname)

    try_again = input("Try another name(y/n): ").lower()
    if try_again == "y":
        continue
    else:
        break