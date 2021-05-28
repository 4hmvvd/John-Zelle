#CHAPTER 7: DECISION STRUCTURES

#No 1

print('This program calculate the total wages for a given working week')

workHour = int(input('\nEnter the number of hours worked: '))
hourlyRate = float(input('Enter the rate per hour in USD: '))

overtimeRate = (hourlyRate / 2) + hourlyRate
    
if workHour <= 40:
    wage = workHour * hourlyRate
    
else:
    normalWage = 40 * hourlyRate
    ExtraTime = workHour - 40
    wageXtra = ExtraTime * overtimeRate
    wage = normalWage + wageXtra
    
print('\nYour wage for the week is: ${0:0.2f}'.format(wage))


#No 2

print('this program displays Grades of a quiz based on input scores')

score = int(input('\nEnter the score you had in Quiz: '))

if score == 5:
    print('You had A')

elif score == 4:
    print('You had B')

elif score == 3:
    print('You had C')

elif score == 2:
    print('You had D')

else:
    print('You had F')


#No 3

print('this program displays Grades of an Exam based on input scores')

score = float(input('\nEnter the score you had in Exam: '))

if score >= 90 and score <= 100:
    print('You had A')

elif score >= 80 and score <= 89:
    print('You had B')

elif score >= 70 and score <= 79:
    print('You had C')

elif score >= 60 and score <= 69:
    print('You had D')

else:
    print('You had F')


#No 4

print('This program classify students based on credits earned')

credit = int(input('\nEnter the number of credit earned in college: '))

if credit < 7:
    print('The student is a Freshman')

elif credit >= 7 and credit < 16:
    print('The student is a Sophomore')

elif credit >= 16 and credit < 26:
    print('The student is a Junior')

else:
    print('The student is a Senior')


#No 5

print('This program calculates the Body Mass Index of a person')

height = float(input('\nEnter your height in meters: '))
weight = float(input('Enter your weight in Kilogram: '))

BMI = weight / (height ** 2)

if BMI >= 19 and BMI <= 25:
    print('\nYour body mass index is:',BMI,'. This is NORMAL WEIGHT.')

elif BMI < 19:
    print('Your body mass index is:',BMI,'. You are UNDER WEIGHT.')

else:
    print('Your body mass index is:',BMI,'. You are OVER WEIGHT.')


#No 6

print('This program calculates the speeding ticket fine in Podunksville')

speedLimit = int(input('\nEnter the speed limit: '))
speed = int(input('Enter the speed: '))

if speed > speedLimit:
    fine = 50 + 5*(speed - speedLimit)
    
    if speed > 90:
        fine = fine + 200
    print('\nYour Fine for overspeeding is: ${0}.'.format(fine))
        
else:
    print('\nYour speed is Legal')


#No 7

print('This program calculates Babysitter charges\n')

start = input('Enter the start time in (hh:mm): ')
end = input('Enter the end time in (hh:mm): ')

#start = '9:30'
#end = '23:30'

startMin = int(start[-2:])
startHr = int(start[0])
endMin = int(end[-2:])
endHr = int(end[0:2])

startTime = startHr + 1 / (60/startMin)
endTime = endHr + 1 / (60/endMin)
time = endTime - startTime

if endTime < 21:
    bill = time * 2.50
    
else:
    x = endTime - 21
    bill = (time - x) * 2.50 + (x * 1.75)

print("The Babysitter charge is: ${0}".format(round(bill, 2)))


#No 8

print('This program displays the eligibility for Senator and House candidacy\n')

age = int(input('Enter your age: '))
durationCitizen = int(input('Enter your years of citizenship: '))

if age >= 30 and durationCitizen >= 9:
    print('\nYou are Eligible to be a U.S Senator')

else:
    print('\nYou are not eligible to be a U.S Senator')

if age >= 25 and durationCitizen >= 7:
    print('\nYou are Eligible to be in the U.S House')

else:
    print('\nYou are not eligible to be in the U.S House')


#No 9

print('This program calculate the date of Easter for a range of years\n')

year = int(input('Enter the year you want the Easter date: '))

if year >= 1982 and year <= 2048:
    
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7
    print('\nThe date of Easter is March 22 + ',d,' + ',e)


#No 10

print('This program modifies the previous program considering extra conditions\n')

year = int(input('Enter the year you want the Easter date: '))

if year >= 1900 and year <= 2099:
    
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7

    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        
        print('\nThe date of Easter is March 15 + ',d,' + ',e)

    else:
        print('\nThe date of Easter is March 22 + ',d,' + ',e)
        

#No 11

print('This program if a year is a leap year\n')

year = int(input('Enter a year: '))

if year%4 == 0:
    print(year,'is a leap year.')

else:
    print(year,'is not a leap year.')


#No 12

print('This program checks the validity of a date inputted by the user\n')

date = input('Enter date in mm/dd/yyyy format: ')

dayStr, monStr, yearStr = date.split('/')

day = int(dayStr)
month = int(monStr)
year = int(yearStr)

def leapYear(year):
    
    if year%4 == 0:
        return True
    else:
        return False

if month <= 12 or day <= 31:

    if day <= 28:
        print('Date is VALID')

    elif month == 2 and day == 29:
        if leapYear(year) == True:
            print('Date is VALID')
        else:
            print('Date is INVALID')

    elif month == 4 or 6 or 9 or 11:
        if day <= 30:
            print('\nDate is VALID')
        else:
            print('Date is INVALID')

    else:
        print('Date is INVALID')
else:
    print('\nThe Date is INVALID')


#No 13

print('This program checks validity of date and dispays day number\n')

def leapYear(year):
    
    if year%4 == 0:
        return True
    else:
        return False
    
def dateValid(month, day, year):
    
    if month <= 12 or day <= 31:

        if day <= 28:
            return True

        elif month == 2 and day == 29:
            if leapYear(year) == True:
                return True
            else:
                return False
            
        elif month == 4 or 6 or 9 or 11:
            if day <= 30:
                return True
            else:
                return False
            
        else:
            return False
    else:
        return False

date = input('Enter date in mm/dd/yyyy format: ')

dayStr, monStr, yearStr = date.split('/')

day = int(dayStr)
month = int(monStr)
year = int(yearStr)

if dateValid(month, day, year) == True:
    dayNum = 31 * (month - 1) + day
    if month == 2:
        if leapYear(year) == True:
            dayNum = dayNum - (4 * (month) + 23)//10 + 1

        else:
            dayNum = dayNum - (4 * (month) + 23)//10

    else:
        dayNum = 31 * (month - 1) + day
    print('The numeric value of the date is:',dayNum)
    
else:
    print('Date is INVALID')
    

#No 14

from graphics import *
import math

print('This program finds the intersection of a circle and a line with a condition\n')

win = GraphWin('Circle Intersection',300,300)
win.setCoords(-10,-10,10,10)

Text(Point(0,7),'The intersection of a circle and a line').draw(win)

r = float(input('Enter the radius of the circle: '))
y = float(input('Enter the y-intercept of the line: '))

circ = Circle(Point(0,0),r).draw(win)
line = Line(Point(6,y),Point(-6,y)).draw(win)

if r > y:
    
    discRoot = math.sqrt((r**2)-(y**2))
    x1 = discRoot
    x2 = -(discRoot)
    x11 = Circle(Point(x1, y),0.2)
    x11.setOutline('red')
    x11.draw(win)
    x22 = Circle(Point(x2, y),0.2)
    x22.setOutline('red')
    x22.draw(win)
    
    Text(Point(0,-6),'The first point of intersection is:').draw(win)
    Text(Point(0,-7),x1).draw(win)
    Text(Point(0,-8),'The second point of intersection is:').draw(win)
    Text(Point(0,-9),x2).draw(win)

    print('\nThe two points of intersections are:',x1,'and',x2)
    
else:
    print('\nThe line does not intersect')
    
win.close()


#No 15

from graphics import *
import math

print('This program calculate the slope and length of a line segment')

win = GraphWin('Line segment',300,300)
win.setCoords(0,0,10,10)

Text(Point(5,8.5),'click on two points to create a line').draw(win)

p1 = win.getMouse().draw(win)
p2 = win.getMouse().draw(win)

line = Line(p1,p2)
line.setOutline('black')
line.draw(win)

dx = p2.getX() - p1.getX()
dy = p2.getY() - p1.getY()
length = math.sqrt(dx**2 + dy**2)
midX = (p2.getX() + p1.getX()) / 2
midY = (p2.getY() + p1.getY()) / 2

if dx == 0:
    
    Text(Point(5,6),'The line is a vertical').draw(win)

else:
    
    slope = dy / dx
    Text(Point(5,2.5),'The slope of the line segment is:').draw(win)
    Text(Point(5,2),slope).draw(win)
    print('The slope of the line segment is:',slope)

#win.plot(midX,midY,"cyan")

p3 = Circle(Point(midX,midY),0.1)
p3.setOutline('cyan')
p3.draw(win)

Text(Point(5,3.5),'The length of the line segment is:').draw(win)
Text(Point(5,3),length).draw(win)
print('The length of the line segment is:',length)

win.getMouse()
win.close()


#No 16

from graphics import *
import math

print('This program draws an archery target and calculates the points')

win = GraphWin('Archery Target',300, 300)
win.setCoords(0,0,10,10)
win.setBackground('gray')

white = Circle(Point(5,5),4.5)
white.setFill('white')
white.draw(win)

black = Circle(Point(5,5),3.5)
black.setFill('black')
black.draw(win)

blue = Circle(Point(5,5),3)
blue.setFill('blue')
blue.draw(win)

red = Circle(Point(5,5),2.5)
red.setFill('red')
red.draw(win)

yellow = Circle(Point(5,5),2)
yellow.setFill('yellow')
yellow.draw(win)

green = Circle(Point(5,5),1)
green.setFill('green')
green.draw(win)

point = 0

for i in range(5):
    arrow = win.getMouse()
    x = arrow.getX()
    y = arrow.getY()
    z = math.sqrt(x**2 + y**2)

    if z > 3 and z <= 3.5:
        y = 1
        point = point + y
        
    elif z > 2.5 and z <= 3:
        y = 3
        point = point + y
        
    elif z > 2 and z <= 2.5:
        y = 5
        point = point + y
        
    elif z > 1.5 and z <= 2:
        y = 7
        point = point + y
        
    elif z > 1 and z <= 1.5:
        y = 9
        point = point + y

    else:
        y = 0
        print('You MISSED!')

    print('Point: ',y,   'Total: ',point)
        
win.getMouse()
win.close()


#No 17

from graphics import *

print('LG Television Bouncing Ball')

win = GraphWin('Bouncing Ball', 640, 480)
win.setCoords(0, 0, 100, 100)
win.setBackground('black')

shape = Circle(Point(50, 30), 10)
shape.setFill('green')
shape.draw(win)

dx = 1
dy = 1

for i in range(10000):
    c = shape.getCenter()

    if c.getX() > 90:
        shape.setFill('cyan')
        dx = -1
        
    elif c.getX() < 10:
        shape.setFill('red')
        dx = 1
        
    elif c.getY() > 90:
        shape.setFill('yellow')
        dy = -1
        
    elif c.getY() < 10:
        shape.setFill('blue')
        dy = 1
        
    update(10)
    shape.move(dx,dy)

win.close()


#No 18

from graphics import *
import math

print('This program is same as No 14, however, will not crash on any input\n')

win = GraphWin('Circle Intersection',300,300)
win.setCoords(-10,-10,10,10)

Text(Point(0,7),'The intersection of a circle and a line').draw(win)

try:
    
    r = float(input('Enter the radius of the circle: '))
    y = float(input('Enter the y-intercept of the line: '))

    circ = Circle(Point(0,0),r).draw(win)
    line = Line(Point(6,y),Point(-6,y)).draw(win)

    if r > y:
        
        discRoot = math.sqrt((r**2)-(y**2))
        x1 = discRoot
        x2 = -(discRoot)
        x11 = Circle(Point(x1, y),0.2)
        x11.setOutline('red')
        x11.draw(win)
        x22 = Circle(Point(x2, y),0.2)
        x22.setOutline('red')
        x22.draw(win)

        Text(Point(0,-6),'The first point of intersection is:').draw(win)
        Text(Point(0,-7),x1).draw(win)
        Text(Point(0,-8),'The second point of intersection is:').draw(win)
        Text(Point(0,-9),x2).draw(win)

        print('\nThe two points of intersections are:',x1,'and',x2)
        
    else:
        print('\nThe line does not intersect')

except ValueError:
    print('Your input is wrong, ENTER A NUMBER')

except:
    print('Sorry for the inconviniences')

win.getMouse()   
win.close()
