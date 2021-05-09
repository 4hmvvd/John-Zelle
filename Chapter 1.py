#Chapter 1: COMPUTERS AND PROGRAMS

#Programming Exercises

'''
Small changes, irrespective of how insignificant the change is can alter
the output of a chaotic program significantly. E.g, weather forecast program.
The butterfly effect.
'''

#No 1
print('Hello World')

#No 2
def main():
    print('This program displays chaotic behavior')
    x = eval(input('Enter a value between 0 and 1: '))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)
        
main()

#No 3
def main2():
    print('This program displays a chaotic bahavior')
    x = eval(input('Enter a value between 0 and 1: '))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)

main2()


#No 4
def main3():
    print('This program displays chaotic behavior')
    x = eval(input('Enter a value between 0 and 1: '))
    for i in range(20):
        x = 3.9 * x * (1-x)
        print(x)
        
main3()

#No 5
n = int(input('How many times should I print the result: '))

def main4(n):
    print('This program displays chaotic behavior')
    x = eval(input('Enter a value between 0 and 1: '))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)
        
main4(n)

#No 6
def main5():
    print('This program displays chaotic behavior')
    x = eval(input('Enter a value between 0 and 1: '))
    for i in range(20):
        x = 3.9 * x * (1-x)
        #x = 3.9 * (x - x * x)
        #x = 3.9x - 3.9x * x
        
        print(x)
        
main5()

#No 7
def main6():
    print('This program displays chaotic behavior between 2 input')
    x1 = eval(input('Enter a value between 0 and 1: '))
    x2 = eval(input('Enter a value between 0 and 1: '))
    print('\ninput','  ',x1,'      ',x2)
    print('----------------------------')
    
    for i in range(10):
        x1 = 3.9 * x1 * (1-x1)
        x2 = 3.9 * x2 * (1-x2)
        #x1 = round(x1, 4)  # This is beyond the scope of this lesson
        #x2 = round(x2, 4)  # This is beyond the scope of this lesson
        
        print('       ',x1,'     ',x2)
        
main6()
