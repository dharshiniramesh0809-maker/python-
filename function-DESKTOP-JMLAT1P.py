import random

num = random.randint(15,20)

guess = int(input("can you guess what's the number is: "))

while num != guess:
    if guess > num:
        print("you guess more")
    else:
        print("you guess less")
    guess = int(input("guess again:"))
    
print("won")
