#CHAPTER 8: LOOP STRUCTURES AND BOOLEANS

#No 1

print('This program computes the nth term of a Fibonacci series')

nth = int(input('Enter a nth term of the Fibonacci series you want: '))

def fibo(nth):

    a, b = 0, 1

    for i in range(3,nth+1):
        c = a + b
        a = b
        b = c

    print(c)

fibo(nth)
