#Chapter 2: WRITING SIMPLE PROGRAMS

#Programming Exercises

#No 1

print('This is an introductory message to the programming',end=' ')
print('exercises of this chapter')


#No 2
print('This program calculates the fahrenheit with an inputed celcius')

def main():

    celcius = int(input('Enter the value of the temperature in celcius: '))
    fahrenheit = 9/5 * celcius + 32

    print('The temperature in degrees Fahrenheit is ',fahrenheit)

    input('Press <Enter> to Quit')

main()


#No 3
print('This program calculates the average of 3 scores')

def main1():
    
    score1, score2, score3 = eval(input('Enter 3 scores seperated by comma: '))

    average = (score1 + score2 + score3) / 3

    print('The average of the scores is ',average)

main1()


#No 4
print('This program calculates the fahrenheit for an inputed celcius')

for i in range(5):
    
    celcius = int(input('Enter the value of the temperature in celcius: '))
    fahrenheit = 9/5 * celcius + 32

    print('The temperature in degrees Fahrenheit is ',fahrenheit)


#No 5
print('This program calculates the values of fahrenheit for a given celcius')

celcius = 0

print('\nCelcius      Fahrenheit')
print('-------------------------')

for celcius in range(celcius,110,10):
    fahrenheit = 9/5 * celcius + 32

    print('  ',celcius,'      ',fahrenheit)


#No 6
print('The program calculates the Future value of the investments')

principal = eval(input('Enter the initial investment: '))
apr = eval(input('Enter the annual percentage rate: '))
n = int(input('Enter the period of years you want calculated: '))

for i in range(n):
    principal = principal * (1 + apr)

print('The value accumulated over ',n,'years is',principal)


#No 7
print('The program calculates the Future value of the investments')

n = int(input('\nEnter the period of years you want calculated: '))
apr = eval(input('Enter the annual percentage rate: '))

for i in range(n):
    
    principal = eval(input('Enter the initial investment: '))

principal = principal * (1 + apr)

print('The value accumulated over ',n,'years is',principal)


#No 8
print('The program calculates the Future value of the investments')

principal = eval(input('Enter the initial investment: '))
rate = eval(input('Enter the yearly rate: '))
periods = eval(input('Enter the period the interest compounded every year: '))
n = int(input('Enter the period of years you want calculated: '))
apr = n * periods * rate / periods  #Not sure of this formula

for i in range(n):
    principal = principal * (1 + apr)

print('The value accumulated over ',n,'years is',principal)


#No 9
print('This program converts Fahrenheit to celcius')

fahrenheit = eval(input('Enter the Fahrenheit temperature: '))
celcius = 5/9 * fahrenheit - 32

print('The temperature in celcius is',celcius)


#No 10
print('This program converts distance in Kilometer to miles')

kilometer = eval(input('Enter the distance in kilometer: '))
miles = kilometer * 0.62

print('The distance in miles in',miles)


#No 11
print('This program converts inches to feet')

inch = eval(input('Enter the value of inch: '))
feet = inch / 12

print('The value in feet after convertion is',feet)


#No 12
print('This program allows a mathematical input and displays the result')

for i in range(20):

    print('Enter a mathematical expression')
    x = eval(input('\n'))

    print(x)
