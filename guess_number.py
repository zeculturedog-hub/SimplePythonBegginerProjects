import random

correct_number = random.randint(0, 100)

print("guess correct number or die!\n")

while True:
    try:
        user_input = int(input("what is your guess: "))

        if user_input == correct_number:
            print("you survive!")
            break
        elif user_input < correct_number:
            print("ohh! too low try again")
        else:
            print("ohh! too high try again")
    except ValueError:
        print("invalid input")

    

    




