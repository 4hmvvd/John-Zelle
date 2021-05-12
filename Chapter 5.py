#Chapter 5: SEQUENCES: STRINGS, LISTS AND FILES

#No 1
'''
print('This program converts date into mm/dd/yyyy format')

date = input('\nEnter date in numerals in the format mm/dd/yyyy: ')

monthStr, dayStr, yearStr = date.split('/')

n = int(monthStr)

month = ['January','February','March','April','May','June','July','August',
         'September','October','November','December']

monthStr = month[n-1]

print("\nThe date is: {0} {1},{2}".format(monthStr,dayStr,yearStr))


#No 2

print('This program display your grade for a test')

score = int(input('\nEnter your score in the test: '))

grades = ['A','B','C','D','F','F']

grade = grades[5-score]

print('\nYour grade based on your score input is: ',grade)


#No 3

print('This program display your grade for a test')

score = int(input('\nEnter your score in the test: '))

grades = 'F'*60 + 'D'*10 + 'C'*10 + 'B'*10 + 'A'*11

print('\nYour grade based on your score input is: ',grades[score])


#No 4

print('This program forms an acronym based on th input text')

text = input('\nEnter the message you want the acronym of: ').split()

print()

for message in text:
    acronym = message[0].upper()
    print(acronym,end='')


#No 5

print('This program calculates the numeric value of a name or word')

name = input("\nEnter your name: ").lower()

value = []
    
for char in name:
    number = ord(char) - 96
    value.append(number)

numTotal = sum(value)   
print(numTotal)
print(name)


## ANOTHER APPROACH ##

print('This program calculates the numeric value of a name or word')

alpha = '0abcdefghijklmnopqrstuvwxyz'

name = input("\nEnter your name or a word to get the numeric value: ").lower()

value = 0
    
for char in name:
    value += alpha.find(char)
    
print(value)
print(name)


#No 6

print('This program calculates the numeric value of a full name or a phrase')
print('ignoring the spaces inbetween')

name = input("\nEnter your full name or a phrase: ").lower()
name = name.replace(" ","") #This would allow multiple input ignoring spaces 

value = [] 
for char in name:
    value.append(ord(char) - 96)

numTotal = sum(value)    
print(numTotal)
print(name)

## ANOTHER APPROACH ##

print('This program calculates the numeric value of a full name or a phrase')
print('ignoring the spaces inbetween')

name = input("\nEnter your full name or a phrase: ").lower()
value = 0
name = name.replace(" ","")
    
for char in name:
    value += int(char, 36) - 9
    
print(value)
print(name)

### ANOTHER APPROACH ###

print('This program calculates the numeric value of a name or word')

alpha = '0abcdefghijklmnopqrstuvwxyz'

name = input("\nEnter your name or a word to get the numeric value: ").lower()
name = name.replace(" ","")

value = 0
    
for char in name:
    value += alpha.find(char)
    
print(value)
print(name)


#No 7

print('This program encodes and decodes Caeser ciphers')

#### ENCODER ####

print('This is the encoder')
text = input('\nEnter the word or text you want to encode: ')
key = int(input('Enter the value of the key you want to encode with: '))

print()
for ch in text:
    message = chr(ord(ch) + key)
    
    print(message,end='')

##### DECODER #####

print('This is the decoder')

text = input('\nEnter the word or text you want to decode: ')
key = int(input('Enter the value of the key you want to use: '))

print()
for ch in text:
    message = chr(ord(ch) - key)
    
    print(message,end='')


#No 8

print('This program encodes Caeser cipher using positioning to shift')
print('in the sequence')

alphabets = 'abcdefghijklmnopqrstuvwxyzabcde'

text = input('\nEnter the message you want to encode: ')
key = int(input('Enter the key value (between 1 and 5) to encode: '))
print()
for char in text:
    posText = alphabets.find(char)
    
    message = alphabets[key + posText]
    
    print(message,end='')
    

#No 9

print('This program count the number of words in a sentence')

text = input('\nEnter the sentence to get the number of words therein:').split()

print('\nThe number of words in the sentence is:',len(text))


#No 10

print('This program calculate the average word length in a sentence')

text = input('\nEnter the sentence: ')

NumWords = text.split()

print('The average number of words is: ',int(len(text)/len(NumWords)))


#No 11

print('This program displays chaotic behavior between 2 input')
x1 = eval(input('\nEnter a value between 0 and 1: '))
x2 = eval(input('Enter a value between 0 and 1: '))
print('\ninput','  ',x1,'        ',x2)
print('------------------------------')
    
for i in range(1,11):
    x1 = 3.9 * x1 * (1-x1)
    x2 = 3.9 * x2 * (1-x2)
    x1 = round(x1, 6)
    x2 = round(x2, 6)
        
    #print(' ',i,'   ',x1,'     ',x2)
    #print(' {0}   {1:0.6f}     {2:0.6f}'.format(i,x1,x2))
    print('{0:>2}{1:13.6f}{2:15.6f}'.format(i,x1,x2))
    

#No 12

print('The program calculates the Future value of the investments')

principal = eval(input('\nEnter the initial investment: '))
apr = float(input('Enter the annual percentage rate: '))
n = int(input('Enter the period of years you want calculated: '))

print('\nYear     Value')
print('---------------')

for year in range(1,n):
    principal = principal * (1 + apr)
    
    print('{0:>2}     ${1:0.2f}'.format(year,principal))
    

#No 13

inFile = open('InFutValue.txt', 'w')
inFile.write('This file contains the returns of investing an initial amount')
inFile.write(" with an annual percentage rate for a given year\n")
inFile.close()

principal = eval(input('\nEnter the initial investment: '))
apr = float(input('Enter the annual percentage rate: '))
n = int(input('Enter the period of years you want calculated: '))

inFile = open('InFutValue.txt', 'a')

inFile.write('\nYear     Value') 
inFile.write('\n---------------')

for year in range(1,n):
    principal = principal * (1 + apr)
    
    inFile.write('\n{0:>2}     ${1:0.2f}'.format(year,principal))
    
inFile.close()


#No 14

print('This program simulates Word Count on Unix/Linux systems')

inFileName = input('Enter the name of the file: ')

inFile = open(inFileName, 'r')

char = inFile.read().replace(' ','')
print('The number of characters in the file is:',len(char))

inFile.close()

inFile = open(inFileName, 'r')

words = []
for line in range(13):
    word = inFile.readline()
    words.append(word)
    NumWords = str(words).split()
    
print('The number of words in the file is:',len(NumWords))

inFile.close()

inFile = open(inFileName, 'r')

line = inFile.readlines()
print('The number of lines in the file is:',len(line))

inFile.close()


#No 15

print('This program plot horizontal bar chart of students exam score')

from graphics import *

win = GraphWin('Exam Scores',640, 540)
win.setCoords(-20, -5, 100, 30)
win.setBackground('white')

Smith = Text(Point(-10,5),'Smith').draw(win)
Jones = Text(Point(-10,11),'Jones').draw(win)
Dibblebit = Text(Point(-10,17),'Dibblebit').draw(win)
Computewell = Text(Point(-10,23),'Computewell').draw(win)


inFile = open('ExamScores.txt','r')
lines = inFile.readlines()
smithLine = (lines[4]).split()      #readline is a string
smithScore = smithLine[1]
jonesLine = (lines[3]).split()
jonesScore = jonesLine[1]
dibblebitLine = (lines[2]).split()
dibblebitScore = dibblebitLine[1]
computewellLine = (lines[1]).split()
computewellScore = computewellLine[1]

smith = Rectangle(Point(0, 3),Point(smithScore, 6)).draw(win)
jones = Rectangle(Point(0, 9),Point(jonesScore, 12)).draw(win)
dibblebit = Rectangle(Point(0, 15),Point(dibblebitScore, 18)).draw(win)
computewell = Rectangle(Point(0, 21),Point(computewellScore, 24)).draw(win)

inFile.close()

'''
#No 16

