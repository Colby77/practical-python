import random

player_name = input('Welcome to the number guessing game (1-100).  Enter your name: \n')

number = random.randint(1, 100)

guessed = False
tries = 0

while guessed != True:
    guess = int(input('What is your guess? '))
    if guess == number:
        print('Well done', player_name, 'You found the number in', tries, 'tries')
        guessed = True
    elif guess > number:
        print('Your guess is too high, try again')
        tries += 1
    elif guess < number:
        print('Your guess is too low, try again')
        tries += 1