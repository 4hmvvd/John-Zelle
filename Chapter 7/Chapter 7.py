#CHAPTER 7: DECISION STRUCTURES

#No 1
'''
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

'''
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
