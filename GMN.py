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
magic_number = random.randrange(1,5)

while True:
    guess = int(input('Guess my number from 1 to 5: '))
    if guess == magic_number:
        print("You got it right")
        break 
    else:
        print("Sorry, try again") 