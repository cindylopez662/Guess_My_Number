my_number = 3
is_incorrect_guess = True 
while is_incorrect_guess:
    guess = int(input('Guess my number from 1 to 5: '))
    if guess == my_number:
        print("You got it right")
        break 
    else:
        print("sorry try again") 