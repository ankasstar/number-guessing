import random
print("Welcome to the numerical guessing game")
def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100
def num_isvalid():
    while True:
        n = input("Please enter a number: ")
        if is_valid(n):
            return int(n)
            break
        else:
            print("Can we still enter an integer from 1 to 100?")
            continue
        
def game():
    num = random.randint(1, 100)
    count = 8
    while count>0:
        n = num_isvalid()
        count-=1
        if n > num:
            print("Too much, try again")
        if n < num:
            print("Too little, try again")
        if n == num:
            print("You guessed it, congratuls!")
            break
        print(f"There are {count} attempts left")
    again = input("Would you like to play more? Press '1' if yes, and '0' if no: ")
    while True:
        if again == "1":
            return game()
        else:
            break
game()
print("Thanks for playing the number guessing game. I'll see you around...")