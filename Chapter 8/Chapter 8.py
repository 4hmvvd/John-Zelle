#CHAPTER 8: LOOP STRUCTURES AND BOOLEANS

#No 1
'''
print('This program computes the nth term of a Fibonacci series\n')

nth = int(input('Enter a nth term of the Fibonacci series you want: '))

def fibo(nth):

    a, b = 0, 1

    for i in range(3,nth+1):
        c = a + b
        a = b
        b = c

    print('\n{0}'.format(c))

fibo(nth)

## USING while loop ##

nth = int(input('Enter a nth term of the Fibonacci series you want: '))

a,b = 0, 1
sum = 0
while nth-2 > sum:
    c = a + b
    a = b
    b = c
    sum += 1
print(c)


#No 2

print('This program prints a nicely formatted table of windchill values')

def windchill(temperature, windspeed):
    if windspeed > 3:
        
        windChill = 35.74 + 0.6215*temperature - 35.75*(windspeed**0.16) + 0.4275*temperature * (windspeed**0.16)
        #windChill = round(windChill,2)
    else:
        windChill = 0
        
    return windChill

print('\n{0:>10}  {1:6} {2:7} {3:7} {4:7} {5:7} {6:7} {7:7} {8:7}'.format(-20,-10,0,10,20,30,40,50,60))
print('-----------------------------------------------------------------------------')
for windspeed in range(5,50,5):
    print('{0:2}  {1:0.3f}  {2:0.3f}  {3:0.3f}  {4:0.3f}  {5:0.3f}  {6:0.3f}  {7:0.3f}  {8:0.3f}  {9:0.3f}'.format(windspeed,windchill(-20,windspeed),windchill(-10,windspeed),windchill(0,windspeed),windchill(10,windspeed),windchill(20,windspeed),windchill(30,windspeed),windchill(40,windspeed),windchill(50,windspeed),windchill(60,windspeed)))


#No 3

print('This program calculates the period it takes to double an investment')

apr = float(input('Enter the annualized interest rate: '))

principal = float(input('Enter the initial investment: '))
finalPrincipal = principal*2
years = 0

while principal < finalPrincipal:

    interest = principal * apr
    years += 1
    principal += interest

print(principal)
print(years)


#No 4

print('This program calculates the Syracuse sequence\n')

def syr(x):
    if x % 2 == 0:
        syrX = x / 2

    elif x % 2 == 1:
        syrX = 3 * x + 1

    return syrX

x = int(input('Enter a number to start the Syracuse sequence: '))
print('\n{}'.format(x),end=' ')

while x > 1:

    syrX = syr(x)
    x = syrX
    print(int(syrX),end=' ')

'''
#No 5

print('This program determine if an input is a prime number or not')

n = int(input('Enter the value of the number: '))
