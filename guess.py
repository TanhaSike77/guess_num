import random
def whats_code():
    code = random.randint(1, 1000)
    attempt = 10
    while attempt > 0:
        guess = int(input("Guess the code (1-1000) within 10 attempts for access :"))
        if guess == code:
            print("Welcome! You have accessed the system.")
        elif guess < code:
            print("Try higher.")
            attempt -= 1
        elif guess > code:
            print("Try lower.")
            attempt -= 1
        else:
            print("You have failed to guess the code.")
            print("The code was:", code)
            break
whats_code()