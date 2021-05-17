#Chapter 6: DEFINING FUNCTIONS
import math

#No 1

print('This program prints the lyrics of Old MacDonald for 5 domestic animals\n')
print()

def oldMac():
    return 'Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n'

def Eeigh():
    return 'Ee-igh, Ee-igh, Oh!\n'

def third():
    lyrics = 'With a moo, moo here and a moo, moo there.\n'
    lyrics1 = 'Here a moo,there a moo,everywhere a moo, moo.\n'
    lyrics2 = lyrics + lyrics1
    return lyrics2

def verseFor(animal):
    song = oldMac() + 'And on that farm he had a '+ animal +', ' + Eeigh()
    song1 = third() + oldMac()
    song2 = song + song1

    return song2

def main():
    for animal in ['cow','rabbit','sheep','donkey','goat']:
        print(verseFor(animal))

main()


#No 2

print('Lyrics for 10 verses of The Ants Go Marching\n')
print()

def song(number):
    first = 'The ants go marching ' + number + ' by ' + number +',' +' hurrah! hurrah!\n'
    thirdLine = 'The ants go marching ' + number + ' by ' + number +',\n'
    fourth = 'The little one stops to suck his thumb,\n'
    fifth = 'And they all go marching down...\nIn the ground ...\n'
    sixth = 'To get out ...\nOf the rain.\n' + 'Boom!'*3 + '\n'
    
    lyrics = first*2 + thirdLine + fourth + fifth + sixth
    
    return lyrics

def main():
    for number in ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']:
        print(song(number))

main()


#No 3

print('This program defines a function to calculates the surface Area and Volume of a sphere')

radius = int(input('\nEnter the radius of the sphere: '))

def sphereArea(radius):
    return round((math.pi * 4/3 * radius **3),4)

def sphereVolume(radius):
    return math.pi * 4 * radius **2

def main():
    print('\nThe surface area of the sphere is: ',sphereArea(radius))
    print('The radius of the sphere is: ',sphereVolume(radius))

main()


#No 4
print('Defined a function to calculate the sum and cubes of natural numbers\n')

n = int(input('Enter a natural number: '))

def sumN(n):
    count = 0
    for i in range(1,n+1):
        count += i
    return count
    
def sumNcubes(n):
    count = 0
    for i in range(1,n+1):
        cube = i**3
        count += cube
    return count

print('\nThe sum of natural numbers up to ',n,'is',sumN(n))
print('The sum of cube of natural numbers up to ',n,'is',sumNcubes(n))


#No 5

print('A function that calculate the area of pizza and cost per square inch\n')

radius = float(input('Enter the radius of the pizza: '))
cost = float(input('Enter the price to get the box of pizza: '))

def area(radius):
    return math.pi * radius**2

def inch(cost):
    return area(radius) / cost

print('\nThe area of the pizza is ',area(radius))
print('The cost per square inch is ',inch(cost))


#No 6
print('A function that calculates the area of a triangle\n')

def triangle():
    a = int(input('Enter the value of side A: '))
    b = int(input('Enter the value of side B: '))
    c = int(input('Enter the value of side C: '))

    s = (a + b + c) / 2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print('\nThe area of the triangle is: ',area)

triangle()


#No 7

nth = int(input('Enter the nth term you want in the sequence: '))

def fibo(nth):
    print('\nThis program calculate the nth term of fibonacci sequence')

    a, b = 0, 1

    for i in range(3,nth+1):
        c = a + b
        a = b
        b = c
    print('The '+str(nth)+'th'+' term of the sequence is: ',c)

fibo(nth)


#No 8

print('A program defining a function to implement Newton method in guessing square root of a number')

x = float(input('\nEnter the value you want the root of: '))
n = int(input('Enter the number of times you want to improve the guess: '))
guess = x / 2

def nextGuess(guess,x):
    return (guess + (x/guess)) / 2

for i in range(n):
    guess = nextGuess(guess,x)
    FinalGuess = guess

print(FinalGuess)


#No 9

print('This program defines a function to calculate the grade of a score\n')

score = int(input('Enter the score you want the grade of: '))

def grade(score):
    grades = 'F'*60 + 'D'*10 + 'C'*10 + 'B'*10 + 'A'*11
    grade = grades[score]
    
    print(grade)
    
grade(score)
    

#No 10

print('This program defines a function to determine the acronym of a phrase\n')

phrase = input('Enter the the phrase of which you want the acronym of: ').split()

def acronym(phrase):
    for i in phrase:
        acronym = i[0].upper()
         
        print(acronym, end='.')

acronym(phrase)


#No 11

nums = [1,2,3,4,5,6,7,8]

def squareEach(nums):
    print('This function modifies a list by squaring each number\n')
    for num in nums:
        nums = num**2
        print(nums, end=' ')
    
squareEach(nums)


#No 12

nums = [1,2,3,4,5,6,7,8,9,10]
total = 0

def sumList(nums,total):
    print('This function modifies a list by suming each number\n')
    for num in nums:
        total += num
    print('The sum of numbers in the list is: ',total)

sumList(nums,total)


#No 13

print('This program defines a function that modifies a string to a number\n')

strList = ['0ne','Two','Three','Four','Five','Six','Seven','Eight']

def toNumbers(strList):
    for i in range(1,len(strList)+1):
        number = i
        print(number, end=' ')

toNumbers(strList)


#No 14

def squareEach(nums):
    for num1 in nums:
        nums = int(num1)**2
        print(nums, end=", ")
    
def sumList(numss,total):
    for num in numss:
        total += int(num)

    print(total)

print('This program prints sum of squares of numbers in a file into the file')

inFile = input('\nEnter the name of the file: ')
total = 0
numbers = open(inFile, 'r')

number = numbers.readlines()
numberList = []
for i in range(len(number)):
    number2 = number[i][:-1]
    numberList.append(number2)

    
squareList = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

sumList(squareList, total)

numbers.close()


#No 15
from graphics import *

print('A function that draws smiley face')

win = GraphWin('Smiley Faces',480, 320)
win.setCoords(0, 0, 400, 400)
win.setBackground('white')

def drawFace(center,size,win):
    face = Circle(center,size*20)
    face.setFill('green')
    face.draw(win)

    mouth = Circle(center,size*13)
    mouth.setFill('black')
    mouth.setOutline('red')
    mouth.draw(win)
    smile = Circle(center, size*14)
    smile.move(0, size*4)
    smile.setFill('green')
    smile.setOutline('green')
    smile.draw(win)
    
    eye = Circle(center,size*4)
    eye.move(-size*8, size*10)
    eye.setFill('white')
    eye.draw(win)
    eye2 = eye.clone()
    eye2.move(size*16,0)
    eye2.draw(win)
    
    pupil = Circle(center, size*1.3)
    pupil.setFill('black')
    pupil.move(-size*8, size*9)
    pupil.draw(win)
    pupil2 = pupil.clone()
    pupil2.move(size*16, 0)
    pupil2.draw(win)

    nose = Circle(center, size*3)
    nose.move(0, -size*2)
    nose.setOutline('yellow')
    nose.setFill('yellow')
    nose.draw(win)


def faces():
    i = 0
    for i in range(1,5):
        center = Point(-20+i*85,-20+i*90) #bottom left to top right
        Face = drawFace(center, 3-(i*0.5), win)  #with radius decreasing
        
        '''
        center = Point(340-i*75,-65+i*100) #bottom right to top right
        Face = drawFace(center, i, win) #with radius increasing

        center = Point(350,490-i*110)   #top to bottom 
        Face = drawFace(center, i*0.8, win)  #with radius increasing
        '''
        
    win.getMouse()
    win.close()

faces()


#No 16
from graphics import *

print('This program defines a function that serves as an image anonymizer')

def drawFace(center,size,win):
    face = Circle(center,size*20)
    face.setFill('green')
    face.draw(win)

    mouth = Circle(center,size*13)
    mouth.setFill('black')
    mouth.setOutline('red')
    mouth.draw(win)
    smile = Circle(center, size*14)
    smile.move(0, size*4)
    smile.setFill('green')
    smile.setOutline('green')
    smile.draw(win)
    
    eye = Circle(center,size*4)
    eye.move(-size*8, size*10)
    eye.setFill('white')
    eye.draw(win)
    eye2 = eye.clone()
    eye2.move(size*16,0)
    eye2.draw(win)
    
    pupil = Circle(center, size*1.3)
    pupil.setFill('black')
    pupil.move(-size*8, size*9)
    pupil.draw(win)
    pupil2 = pupil.clone()
    pupil2.move(size*16, 0)
    pupil2.draw(win)

    nose = Circle(center, size*3)
    nose.move(0, -size*2)
    nose.setOutline('yellow')
    nose.setFill('red')
    nose.draw(win)

def main():
    filename = input('Enter the name of the file: ')
    inFile = Image(Point(50, 50), filename)
    Width = inFile.getWidth()
    Height = inFile.getHeight()
    
    win = GraphWin('Image Anonymizer', Width, Height)
    win.setCoords(0, 0, 100, 100)
    inFile.draw(win)

    n = eval(input("How many faces are to be blocked: "))

    for i in range(n):
        point = win.getMouse()
        drawFace(point, 1, win)

    win.getMouse()
    win.close()
main()


#No 17
from graphics import *

print('This program defines a function that moves a graphics object with a mouse-click')
    
def moveTo(shape, newCenter, oldCenter):
    
    dx = newCenter.getX() - oldCenter.getX()
    dy = newCenter.getY() - oldCenter.getY()
        
    shape.move(dx,dy)
    
def main():
    win = GraphWin('Move Graphics Object', 400, 400)
    win.setCoords(0, 0, 100, 100)

    oldCenter = win.getMouse()
    shape = Circle(oldCenter, 4)
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        newCenter = win.getMouse()
        oldCenter = shape.getCenter()
        
        moveTo(shape, newCenter, oldCenter)

    win.getMouse()
    win.close()
    
main()
