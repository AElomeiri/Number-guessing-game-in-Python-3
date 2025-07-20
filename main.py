import random
print('Wellcom to The Number Guessing Game!')
print('choose the range of numbers you want to guess from')
lower_limit = int(input('Enter the lower limit: '))
upper_limit = int(input('Enter the upper limit: '))
number_to_guess = random.randint(lower_limit, upper_limit)
print(f'Guess a number between {lower_limit} and {upper_limit}')
while True:
    quss = int(input('Enter your quess: '))
    if quss < lower_limit or quss > upper_limit:
        print(f'please enter a number between {lower_limit} and {upper_limit}')
    elif quss < number_to_guess:
        print('Your queess is too low, try again!')
    elif quss > number_to_guess:
        print('Your number is too high, try again!')
    else:
        print('congratulations! you quessed the number!')
        break

print('Try again? (yes/no)')
