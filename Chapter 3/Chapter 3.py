#Chapter 3: COMPUTING WITH NUMBERS

import math

#No 1
print('This program calculates the Volume and Surface area of a sphere')

radius = int(input('\nEnter the radius of the sphere: '))
volume = 4/3 * math.pi * radius**3
area = 4 * math.pi * radius**2

print('The volume is ',volume)
print('The surface area is ',area)


#No 2
print('This program calculates the cost per inch of pizza')

diameter = int(input('\nEnter the diameter of the pizza: '))
price = float(input('Enter the price of the pizza: '))
radius = diameter / 2

area = math.pi * radius**2
costPerSqrInch = area / price

print('\nThe cost per square inch of the pizza is: ',costPerSqrInch)


#No 3
print('This program calculates the molecular weight of carbohydrate')

carbon = int(input('\nEnter the number of carbon atom: '))
hydrogen = int(input('Enter the number of hydrogen atom: '))
oxygen = int(input('Enter the number of oxygen atom: '))

molWeightCarb =(carbon * 12.0107)+(hydrogen * 1.00794)+(oxygen * 15.9994)

print('The molecular weight of the carbohydrate is:',molWeightCarb)


#No 4
print('The program calculates the distance between the lightning and time')

time = int(input('\nEnter the time in seconds between the light and the sound : '))
speed = 1100
distance = speed * time

print('\nThe distance in feet to a lightning strike is:',distance)


#No 5
print('This program calculates the cost of an order of coffee')

coffShip = 10.50
ship = 0.86 + 1.50

costCoff = coffShip - ship

print('\nThe cost of an order is:',costCoff)


#No 6
print('This program calculates the slope of line')

x1 = float(input('\nEnter the value of the first x coordinate: '))
x2 = float(input('Enter the value of the second x coordinate: '))
y1 = float(input('Enter the value of the first y coordinate: '))
y2 = float(input('Enter the value of the second y coordinate: '))

slope = (y2 - y1) / (x2 - x1)

print('\nThe slope of the line is:',slope)


#No 7
print('This program calculates the distance between two lines')

x1 = float(input('\nEnter the value of the first x coordinate: '))
x2 = float(input('Enter the value of the second x coordinate: '))
y1 = float(input('Enter the value of the first y coordinate: '))
y2 = float(input('Enter the value of the second y coordinate: '))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print('\nThe distance of the line is:',distance)


#No 8
print('This program calculate the Gregorian epact to figure out Easter')

year = int(input('Enter a 4 digit year: '))
c = year // 100
epact = (8 + (c//4) - c + ((8*c + 13)//25) + 11 * (year % 19)) % 30

print('The epact is:',epact)


#No 9
print('This program calculates the area of a triangle')

a = int(input('\nEnter the length of side a: '))
b = int(input('Enter the length of side b: '))
c = int(input('Enter the length of side c: '))

s = (a + b + c) / 2
area = math.sqrt * (s*(s-a)*(s-b)*(s-c))

print('\nThe area of the triangle is:',area)


#No 10
print('This program calculates the length of a ladder to reach a given height')

height = int(input('Enter the height to be attained:'))
angle = int(input('Enter the angle in degrees of the ladder:'))

radians = math.pi * angle / 180

length = height / math.sin * radians

print('\nThe length of the ladder is:',length)


#No 11
print('This program calculates the sum of natural numbers starting from 0')

n = int(input('\nEnter a natural number: '))
N = []

for i in range(n):
    N.append(i)
sumN = sum(N)

print('\nThe sum of the first',n,'number is:',sumN)

####ANOTHER APPROACH

n = int(input('Enter a natural number: '))
sum = 0
for i in range(n):
    sum += i
    
print('\nThe sum of the first',n,'number is:',sum)


#No 12
print('This program calculates the sum of cubes of natural numbers')

n = int(input('\nEnter a natural number: '))

sumCube = 0

for i in range(n):
    cube = i ** 3
    sumCube += cube

print('\nThe sum of the first',n,'number cubes is:',sumCube)


#No 13
print('This program summed up series of numbers')

n = int(input('\nEnter the total number you want to sum: '))

sum = 0

for i in range(n):
    a = int(input('Enter number: '))
    sum += a

print('The total sum of numbers is:',sum)


#No 14
print('This program finds the average of series of numbers')

n = int(input('\nEnter the total number you want the average: '))

sum = 0

for i in range(n):
    a = int(input('Enter number: '))
    sum += a

average = float(sum / n)
print('\nThe average of numbers is:',average)


#No 15
#Gregory Leibniz series
print('This program approximate the value of pi using sum of terms of a series')

total = 0
n = int(input('\nEnter the total number of series you want to sum: '))

for i in range(0,n,2):
    total += (1 / (i+i+1)) - (1 / (i+i+3))

value = 4 * total

print('The sum of the',n,'terms of the series is:',value)

compare = math.pi - value

print('\nThe difference between the sum of',n,'terms of the series')
print('and pi from math library is:',compare)


#No 16
#Fibonacci series
print('This program calculates the nth term of a Fibonacci series')

a = 0
b = 1
nth = int(input('\nEnter the nth term of the fibonacci series you seek: '))

for i in range(nth-2):
    c = a + b
    a = b
    b = c
    
print('\nThe',nth,'term of the Fibonacci series you seek is:',c)


#No 17
#Newton's method of guess

print("This program implement the Newton's method to determine the square root")

x = int(input('\nEnter the number you want the square root of: '))
n = int(input('How many times do you want to improve the guess: '))

guess = x / 2          #guess represent the initial guess

for i in range(n):
    Nguess = (guess + (x/guess)) / 2      #Nguess represent the new guess
    guess = Nguess
    
rootX = Nguess

print("\nThe root of",x,"using the Newton's method is: ",rootX)

compare = math.sqrt(x) - rootX

print('\nThe difference between the Guess method and the')
print('square root from the math library is:',compare)
