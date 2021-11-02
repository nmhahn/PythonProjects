# loading library
import random

# generating a random integer
y = random.randint(1,10)

# getting info from user
print('Guess a number from 1 to 10:')
x = int(input())

# answer based on user's guess
if x == y:
    print('Your number is correct!')
else:
    print('Wrong!')
    print('The right number was', str(y))
