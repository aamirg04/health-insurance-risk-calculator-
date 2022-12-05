print("Welcome to the health insurance risk calculator")
totalrisk = 0
#calculates age 
age = int(input('Please enter a persons age.'))
if age < 30:
    print('age is less than 30')
elif age < 45:
    print('age is less than 45')
    totalrisk = totalrisk + 10
elif age < 60:
    print('age is less than 60')
    totalrisk = totalrisk + 20 
else:
    print('age is over 60')
    totalrisk = totalrisk + 30 
height1 = int(input("enter the first part of your height (feet without remaing inches"))
height1 = height1 * 12 
print(height1)
height2 = int(input("enter the second part of your height (the inches remaing"))
totalheight= height1 + height2 
totalheight = totalheight * totalheight
weight = int(input('eneter your weight in Pounds'))
weight = weight/totalheight
bmi = weight * 703
print(bmi)
if bmi > 18.4 and bmi < 25:
    print ('normal bmi')
elif bmi > 24.9 and bmi < 30:
    totalrisk = totalrisk + 30
else :
    totalrisk = totalrisk + 75
    print ( 'the next step we are going to find out information about your blood pressure, I recomennd going to your local physican to recieve the answers to these questions')
    sylositc = int(input("enter your silostic pressure (it is the higher number"))
    dilostic = int(input("enter your dilostic pressure (it is the lower number "))
if sylositc < 120 and dilostic < 80:
    print ('normal blood pressure')
elif sylositc >= 120 and sylositc <= 129 and dilostic < 80:
    totalrisk = totalrisk + 15
elif sylositc >= 130 and sylositc <= 139 or dilostic >= 80 and dilostic <= 89:
    totalrisk = totalrisk + 30
elif sylositc <= 180 or dilostic <= 120:
    totalrisk = totalrisk + 75
else: 
    totalrisk = totalrisk + 100

diabetes = False
cancer = False 
alzhimer = False 

#q1 asks if your family has a history of diabetes 
q1 = input('Does your family have a history of diabetes (yes/no): ')

if q1.lower() == 'yes':
    diabetes = True 
    totalrisk = totalrisk + 10 
    print(totalrisk)
elif q1.lower() == 'no':
    print('user typed no')
else:
    print('Type yes or no')

#q2 asks if your family has a history of cancer
q2 = input('Does your family have a history of cancer (yes/no): ')

if q2.lower() == 'yes':
    cancer = True 
    totalrisk = totalrisk + 10 
    print(totalrisk)
elif q2.lower() == 'no':
    print('user typed no')
else:
    print('Type yes or no')

#q3 asks if your family has a history of alzhimers 
q3 = input('Does your family have a history of alzhimers (yes/no): ')

if q3.lower() == 'yes':
    alzhimer = True 
    totalrisk = totalrisk + 10 
    print(totalrisk)
elif q3.lower() == 'no':
    print('user typed no')
else:
    print('Type yes or no')
if totalrisk <= 20:
    print ('you are a low risk customer')
elif totalrisk <= 50:
    print('you are a moderate risk customer')
elif totalrisk <= 75:
    print('you are a high risk customer')
else:
    print('you are uninsurable')
