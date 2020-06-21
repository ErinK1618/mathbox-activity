# basic arithmetic random problem generator
# Why? To create an activity for the 2nd and 3rd graders I tutor.

import random

countCorrect = 0
numberOfQuestions = 10
for i in range(0,numberOfQuestions):

    x = random.randint(1,10) #randomly picks an integer between 1-10 inclusively and assigns to x
    y = random.randint(1,10) #randomly picks an integer between 1-10 inclusively and assigns to y

    basicOperations = [x+y, x*y, x-y,  x/y] 
    index = random.randint(0,1) #only picking the first two because of the limitations for - and ÷
    z = basicOperations[index] #trying random operations

    #printing different strings based upon random generated operator. Will make more efficient later.
    if index == 0:
        print (str(i+1)+') '+ str(x) + ' + ' + str(y)+' = ?')
    elif index == 1:
         print (str(i+1)+') '+str(x) + ' × ' + str(y)+' = ?')
    elif index == 2: #this won't be used due to range on index
        print (str(x) + ' - ' + str(y)+' = ?')
    elif index == 3: #this won't be used due to range on index
        print (str(x) + ' ÷ ' + str(y)+' = ?')

    userInput = int(input())

    if userInput == z:
        countCorrect += 1
        print ('Correct') #How do I loop around a problem until the user types in the correct answer?
        #I assume we will need to assign the problem to a variable.
    else:
        print ('Better luck next time.')
    print()

print('You\'ve finished!')
if countCorrect == numberOfQuestions:
    print('Wow! You got them all right')
elif countCorrect >= 8 :
    print(f'Good job! You got {countCorrect} out of {numberOfQuestions} right.')
    # I believe the f is for a string that contains functions. Markus used it so I need to check with him.
else :
    print (f'You got {countCorrect} out of {numberOfQuestions} right.')
