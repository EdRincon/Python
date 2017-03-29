#This is a guess if the next number is bigguer or smaller game.
import random
number1 = random.randint(1,20)
list = [str(number1)]
nG = 0
print('I am thinking of a number between 1 and 20, try to gues if the next \
        number is going to be smaller or bigger')

#Ask the player to guess
while True:
    number2 = random.randint(1,20)
    list = list + [str(number2)]
    print(str(number1) + ' is the current number, write 1 for smaller and \
            2 for bigger')
    guess = int(input())
    if guess == 1:
        if number2 < number1:
            number1 = number2
            nG += 1
        elif number2 > number1:
            break
        elif  number2 == number1:
            print('Lucky you, it was the same number')
    elif guess == 2:
        if number2 > number1:
            number1 = number2
            nG += 1
        elif number2 < number1:
            break
        elif  number2 == number1:
            nG += 1
            print('Lucky you, it was the same number')
    elif guess > 2 or gues < 1:
        print('Please follow the rules')

# Results
if nG == 0:
    print('You failed miserably')
else:
    print('Good job! you guessed ' + str(nG) + ' times')
    print('these are your numbers' + str(list))
