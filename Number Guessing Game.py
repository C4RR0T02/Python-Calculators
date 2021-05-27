#number Guessing
import random

print ("Welcome to Number Guessing Game")

#Generate number

number = random.randint(1,100)

#Guess
attempt = 1
while attempt <= 5:
    if attempt == 1:
        userinput = int(input("Try {:d} : Enter a number between 1 and 100 (or -1 to end): ".format(attempt)))
        if userinput < number:
            print ("{:d} is too low.".format(userinput))
            attempt += 1
            continue
        elif userinput > number:
            print ("{:d} is too high.".format(userinput))
            attempt += 1
            continue
        elif userinput == number:
            print ("Bingo, you've got it right!")
            break
        elif userinput == -1:
            break
    elif attempt > 1:
        userinput = int(input("Try {:d} : Guess again, enter a number between 1 and 100 (or -1 to end): ".format(attempt)))
        if userinput < number:
            print ("{:d} is too low.".format(userinput))
            attempt += 1
            continue
        elif userinput > number:
            print ("{:d} is too high.".format(userinput))
            attempt += 1
            continue
        elif userinput == number:
            print ("Bingo, you've got it right!")
            break
        elif userinput == -1:
            break
print ("The correct number is {}".format(number))
print ("Bye-bye!")
