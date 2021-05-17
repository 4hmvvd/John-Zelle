
#Chapter 4: OBJECTS AND GRAPHICS

from graphics import *

#No 1a
def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
        
    win.close() 
main()

#No 1b
def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        shape2 = Rectangle(Point(p.getX(),p.getY()), Point(c.getX(),c.getY()))
        shape2.setFill('green')
        shape2.draw(win)
        
    win.close() 
main()

#No 1c
def main():
    win = GraphWin()
    shape = Rectangle(Point(50, 50), Point(100,100))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        shape2 = Rectangle(Point(p.getX(),p.getY()), Point(c.getX(),c.getY()))
        shape2.setFill('green')
        shape2.draw(win)

    Text(Point(100,100),'Click again to Quit').draw(win)
    
    win.getMouse()
    win.close() 
main()


#No 2
print('This program draws an archery target')

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

win.close()


#No 3
print('This program draws a sort of face')

win = GraphWin('A sort of face',320,240)
win.setCoords(0, 0, 10, 10)
win.setBackground('white')

face = Circle(Point(5, 5),2)
face.draw(win)
eye = Circle(Point(3.95, 6),0.3)
eye.setFill('red')
eye.draw(win)
leftEye = eye.clone()
leftEye.move(2.1,0)
leftEye.draw(win)
nose = Polygon(Point(5,5.5),Point(4.8,4.6),Point(5.2,4.6))
nose.draw(win)
mouth = Oval(Point(4.6,4.1),Point(5.4,3.7))
mouth.setFill('blue')
mouth.draw(win)

win.close()


#No 4
print('This program prints a winter scene with a snowman and a somewhat tree')

win = GraphWin('Winter scene',640,480)
win.setCoords(0, 0, 10, 10)
win.setBackground('white')

#tree
t1 = win.getMouse()
t1.draw(win)
t2 = win.getMouse()
t2.draw(win)
t3 = win.getMouse()
t3.draw(win)
t4 = win.getMouse().draw(win)
t5 = win.getMouse().draw(win)
t6 = win.getMouse().draw(win)
t7 = win.getMouse().draw(win)
t8 = win.getMouse().draw(win)
t9 = win.getMouse().draw(win)
t10 = win.getMouse().draw(win)
t11 = win.getMouse().draw(win)
    
tree = Polygon(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)
tree.setFill('green')
tree.draw(win)

#snowman
face = Circle(Point(7,6),0.5).draw(win)
eye = Circle(Point(6.8, 6.2),0.08).draw(win)
pupil = win.getMouse().draw(win)
leftEye = eye.clone()
leftEye.move(0.4,0)
leftEye.draw(win)
pupil = win.getMouse().draw(win)

trunk = Oval(Point(6,5.5),Point(8,2.3)).draw(win)
h1 = win.getMouse().draw(win)
h2 = win.getMouse().draw(win)
hand = Line(h1,h2).draw(win)
h3 = win.getMouse().draw(win)
h4 = win.getMouse().draw(win)
hand2 = Line(h3,h4).draw(win)

l1 = win.getMouse().draw(win)
l2 = win.getMouse().draw(win)
leg = Line(l1,l2).draw(win)
l3 = win.getMouse().draw(win)
l4 = win.getMouse().draw(win)
leg2 = Line(l3,l4).draw(win)

win.close()


#No 5
print('This program draws 5 dice')

win = GraphWin('5 Dice',480, 480)
win.setCoords(0,0,10,10)
win.setBackground('white')

#squares
face1 = Rectangle(Point(1,6),Point(3,8))
face1.setWidth(4)
face1.draw(win)
face2 = face1.clone()
face2.move(3,0)
face2.draw(win)
face3 = face2.clone()
face3.move(3,0)
face3.draw(win)

face4 = face1.clone()
face4.move(1.5,-4)
face4.draw(win)
face5 = face4.clone()
face5.move(3,0)
face5.draw(win)

#dots
dot1 = Circle(Point(2,7),0.17)
dot1.setFill('black')
dot1.draw(win)
dot2 = dot1.clone()
dot2.move(2.4,0.55)
dot2.draw(win)
dot3 = dot1.clone()
dot3.move(3.6,-0.55)
dot3.draw(win)
dot4 = dot2.clone()
dot4.move(3,0)
dot4.draw(win)
dot5 = dot1.clone()
dot5.move(6,0)
dot5.draw(win)
dot6 = dot3.clone()
dot6.move(3,0)
dot6.draw(win)

dot7 = Circle(Point(2.9,3.55),0.17)
dot7.setFill('black')
dot7.draw(win)
dot8 = dot7.clone()
dot8.move(1.2,0)
dot8.draw(win)
dot9 = dot7.clone()
dot9.move(0,-1)
dot9.draw(win)
dot10 = dot9.clone()
dot10.move(1.2,0)
dot10.draw(win)

dot11 = dot7.clone()
dot11.move(3,0)
dot11.draw(win)
dot12 = dot8.clone()
dot12.move(3,0)
dot12.draw(win)
dot13 = dot9.clone()
dot13.move(3,0)
dot13.draw(win)
dot14 = dot10.clone()
dot14.move(3,0)
dot14.draw(win)

dot15 = Circle(Point(6.5,3),0.17)
dot15.setFill('black')
dot15.draw(win)

win.close()


#No 6: Modify future value investment in a graphical format

def futVal():
    #Introduction
    print('This program plots a graph calculating the increment of investment in a graphical interface')

    #Create graph window
    win = GraphWin('Investment Growth', 640, 480)
    win.setCoords(-1.75, -200, 11.5, 10400)
    win.setBackground('white')

    #Insert labels
    Text(Point(-1, 0),' 0.0K').draw(win)
    Text(Point(-1, 2500),' 2.5K').draw(win)
    Text(Point(-1, 5000),' 5.0K').draw(win)
    Text(Point(-1, 7500),' 7.5K').draw(win)
    Text(Point(-1, 10000),'10.0K').draw(win)

    #Get inputs of Principal and interest
    Text(Point(5, 9500),'Enter the value of the initial investment:').draw(win)
    inputPrincipal = Entry(Point(5, 8800), 6)
    inputPrincipal.setText('')
    inputPrincipal.draw(win)
    Text(Point(5, 8000),'Enter the value of the annual percentage increase:').draw(win)
    inputApr = Entry(Point(5, 7300), 5)
    inputApr.setText('')
    inputApr.draw(win)

    #Create button just for formalities(so the user click on the screen to proceed)
    button = Text(Point(5, 6500), 'click to PROCEED')
    button.draw(win)
    Oval(Point(3.7, 6750), Point(6.2, 6300)).draw(win)

    #getMouse request the user to click anywhere on the window to proceed the calculation
    win.getMouse()

    #Draw bar for the initial principal
    principal = float(inputPrincipal.getText())
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    #Draw bar for successive years
    for year in range(1,11):
        #Calculate the value for the next year
        apr = float(inputApr.getText())
        principal = principal * (1 + apr)
        
        #Draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill('blue')
        bar.setWidth(2)
        bar.draw(win)

    input('Press <Enter> to quit')
    
    win.close()

futVal()


#No 7
import math

print('This program computes the intersection of a circle and a line')

win = GraphWin('Circle Intersection',300,300)
win.setCoords(-10,-10,10,10)

Text(Point(0,7),'The intersection of a circle and a line').draw(win)

r = float(input('Enter the radius of the circle: '))
y = float(input('Enter the y-intercept of the line: '))

circ = Circle(Point(0,0),r).draw(win)
line = Line(Point(6,y),Point(-6,y)).draw(win)

discRoot = math.sqrt((r**2)-(y**2))
x1 = discRoot
x2 = -(discRoot)
x11 = win.getMouse()
x21 = win.getMouse()
x111 = Circle(Point(x11.getX(),x11.getY()),0.2)
x111.setOutline('red')
x111.draw(win)
x211 = Circle(Point(x21.getX(),x21.getY()),0.2)
x211.setOutline('red')
x211.draw(win)

Text(Point(0,-6),'The first point of intersection is:').draw(win)
Text(Point(0,-7),x1).draw(win)
Text(Point(0,-8),'The second point of intersection is:').draw(win)
Text(Point(0,-9),x2).draw(win)

print('The two points of intersections are:',x1,'and',x2)

win.close()


#No 8
import math

print('This program calculate the slope and length of a line segment')

win = GraphWin('Line segment',300,300)
win.setCoords(0,0,10,10)
win.setBackground('white')

Text(Point(5,8.5),'This slope and length of a line segment').draw(win)

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

slope = dy / dx

p3 = Circle(Point(midX,midY),0.1)
p3.setOutline('cyan')
p3.draw(win)

Text(Point(5,3.5),'The length of the line segment is:').draw(win)
Text(Point(5,3),length).draw(win)
Text(Point(5,2.5),'The slope of the line segment is:').draw(win)
Text(Point(5,2),slope).draw(win)
print('The length of the line segment is:',length)
print('The slope of the line segment is:',slope)

win.close()


#No 9
#Draw Rectangle using mouse clicks to get two opposite points

def rectangle():
    print('This program displays information about a rectangle drawn by the user')

    win = GraphWin('Drawing a Rectangle', 480, 320)
    win.setCoords(0, 0, 10, 10)
    win.setBackground('white')

    Text(Point(5, 0.5),'Click Two points to draw a Rectangle').draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    rec = Rectangle(p1, p2)
    rec.draw(win)
    
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()

    length = float(x2 - x1)
    width = float(y2 - y1)
     
    perimeter = round(2 * (length + width),2)
    area = round((length * width),2)

    Text(Point(5, 9.5),'Your Perimeter is below:').draw(win)
    Text(Point(5, 9), perimeter).draw(win)
    Text(Point(5, 8.5),'Your Area is below:').draw(win)
    Text(Point(5, 8),area).draw(win)
    win.getMouse()
    win.close()

rectangle()


#No 10

import math

def triangle():
    print('This program displays information about a triangle drawn by the user')
    
    win = GraphWin('Drawing a Triangle', 480, 320)
    win.setCoords(0, 0, 10, 10)
    win.setBackground('white')

    Text(Point(5, 0.5),'Click Three points to draw a Triangle').draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    triang = Polygon(p1, p2, p3)
    triang.draw(win)

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    a = math.sqrt(dx**2 + dy**2)

    dx = p3.getX() - p2.getX()
    dy = p3.getY() - p2.getY()
    b = math.sqrt(dx**2 + dy**2)

    dx = p3.getX() - p1.getX()
    dy = p3.getY() - p1.getY()
    c = math.sqrt(dx**2 + dy**2)

    perimeter = round((a + b + c),2)
    
    s = (a+b+c) / 2
    area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)

    Text(Point(5, 9.5),'Your Perimeter is below:').draw(win)
    Text(Point(5, 9), perimeter).draw(win)
    Text(Point(5, 8.5),'Your Area is below:').draw(win)
    Text(Point(5, 8),area).draw(win)
    win.getMouse()
    
    win.close()
    
triangle()


#No 11

print('This program draws a simple house with just 5 mouse clicks')

win = GraphWin('Five Click House',640,480)
win.setCoords(0,0,10,10)
win.setBackground('white')

p1 = win.getMouse()
p2 = win.getMouse()

rec = Rectangle(p1,p2)
rec.draw(win)

recx1 = min(p1.getX(),p2.getX())
recx2 = max(p1.getX(),p2.getX())
recy1 = min(p1.getY(),p2.getY())
recy2 = max(p1.getY(),p2.getY())

p3 = win.getMouse()

recLength = abs(p1.getX() - p2.getX())

doorW = recLength * 0.2
doorH = p3.getY()
doorP1 = Point(p3.getX() - doorW * 0.5, p1.getY())     #recy1
doorP2 = Point(p3.getX() + doorW * 0.5, p3.getY())

Rectangle(doorP1, doorP2).draw(win)

p4 = win.getMouse()

windowH = doorW * 0.5
winP1 = Point(p4.getX() - (0.5 * windowH), p4.getY() - (0.5 * windowH))
winP2 = Point(p4.getX() + (0.5 * windowH), p4.getY() + (0.5 * windowH))
Rectangle(winP1, winP2).draw(win)

p5 = win.getMouse()

roofP1 = p5
roofP2 = p2
roofP3 = Point(p1.getX(), p2.getY()) #p2.getX() - recLength

Polygon(roofP1,roofP2,roofP3).draw(win)


Text(Point(5,9),'Click anywhere on this Graphical User Interface to Quit').draw(win)

win.getMouse()

win.close()
