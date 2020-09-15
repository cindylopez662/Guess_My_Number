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
my_number = 3
is_incorrect_guess = True 
while is_incorrect_guess:
    guess = int(input('Guess my number from 1 to 5: '))
    if guess == my_number:
        print("You got it right")
        break 
    else:
        print("sorry try again") 