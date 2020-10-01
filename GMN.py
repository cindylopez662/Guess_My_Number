'''
Notes:
integer - int
float - 1.0
string - 'a string'
index - kinda like a table of contents
two loops: for and while 
for <item> in [list]:
    <do something>
while loops:
    while [something true]:
        do something 
        [break or true to false]
    else statements, use true or false statements - break also works for false 
'''
import random
magic_number = random.randrange(1,20)

while True:
    guess = int(input('Guess my number from 1 to 20: \n'))
    if guess > magic_number:
        print("Your guess is a little too high!")
    elif guess < magic_number:
        print("You guess is a little too low! ")
    elif guess == magic_number:
        print("You got it right")
        break 
