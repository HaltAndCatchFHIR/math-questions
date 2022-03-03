# I want to be able to choose the kind of math (i.e. addition or subtraction) and how difficult the math will be (i.e. how many digits each number will have)

# I think the parent loop will be a while loop, then for the children loops (addition and subtraction) they can have a 'back' option that lets the user go back to the parent loop

# The number generators will need the random module I think. For subtraction I will have to add a rule that the the second number generated will need to be less than the first number generated. At least until they start covering negative numbers

# Maybe the function will take arguments for what kind of math and how many digits

import random

def mathchoice(num_digits):
    """num_digits = enter the number of digits you would like in your questions"""
    
    plus_minus = input("Enter 'addition' or 'subtraction'")

    if plus_minus == 'addition':
        addition_flag = True
        subtraction_flag = False
    elif plus_minus == 'subtraction':
        subtraction_flag = True
        addition_flag = False

    while addition_flag:
        a = random.randint(0, 10**num_digits)
        b = random.randint(0, 10**num_digits)

        c = a + b

        guess = input(f"What is\n{a}\n+{b}\n\nOtherwise enter 'back' to change math or 'stop' to stop")

        if guess == 'stop':
            break

        elif guess == 'back':
            mathchoice(num_digits)
        
        elif int(guess) == c:
            print("That is correct!!!")
        
        else:
            print(f"Sorry. The correct answer is:\n{a} + {b} = {c}")

    while subtraction_flag:
        x = random.randint(0, 10**num_digits)
        y = random.randint(0, 10**num_digits)

        if x >= y:
            z = x - y
            prompt = f"What is\n{x}\n-{y}\n\nOtherwise enter 'back' to change math or 'stop' to stop"
        else:
            z = y - x
            prompt = f"What is\n{y}\n-{x}\n\nOtherwise enter 'back' to change math or 'stop' to stop"
        
        attempt = input(prompt)

        if attempt == 'stop':
            break

        elif attempt == 'back':
            mathchoice(num_digits)

        elif int(attempt) == z:
            print("That is correct!!!")

        else:
            print(f"Sorry. The correct answer is:\n{z}")