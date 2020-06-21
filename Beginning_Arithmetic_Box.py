#This is an arithmetic box game.
#Need to enter errors and many other things.

#Following is a dictionary data set to define the values of each part of the arithmetic box. Dictionaries can only use same types (I think).
#Later the user will define the values.
valuesBox = {'operator' : ' × ', ' a ' : ' a ', ' b ' : ' b ',
                   ' c ' : ' c ', 'a × c' : 'a × c' ,'b × c': 'b × c',
                   ' d ' : ' d ', 'a × d' : 'a × d','b × d' : 'b × d'}

def printBox(box):
    print(box['operator']+ '|' + box[' a '] + '|' + box[' b '])
    print('---------')
    print(box[' c ']+ '|' + box['a × c'] + '|' + box['b × c'])
    print('---------')
    print(box[' d ']+ '|' + box['a × d'] + '|' + box['b × d'])

print('Blank box.')
printBox(valuesBox)

print('Do you understand the box structure?')
response = input()
if response.lower == 'yes':
    print('Great! Let\'s continue.')
else:
    print('Too bad. We\'re continuing anyhow.')

import random    
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
d = random.randint(1,10)

#arithmeticBox = [[' × ', str(a) , str(b)], [str(c), 'a × c' ,'b × c'], [str(d),'a × d','b × d']]
#print(arithmeticBox)

valuesBox[' a '] = str(a)
valuesBox[' b '] = str(b)
valuesBox[' c '] = str(c)
valuesBox[' d '] = str(d)

print()
print('Random values for a, b, c, and d have been picked.')
printBox(valuesBox)

print()
print('Input the correct answers.')
print('a × c = ?')
valuesBox['a × c'] = input()

print('b × c = ?')
valuesBox['b × c'] = input()

print('a × d = ?')
valuesBox['a × d'] = input()

print('b × d = ?')
valuesBox['b × d'] = input()

print()
print('Below is your filled in box.')
printBox(valuesBox)

# def pickValues(): Want to use definitions to simplify.

if valuesBox['a × c'] == str(a*c) and valuesBox['b × c'] == str(b*c) and valuesBox['a × d'] == str(a*d) and valuesBox['b × d'] == str(b*d):
    print('You got it right!')
else :
    print('Better luck next time.')
    
