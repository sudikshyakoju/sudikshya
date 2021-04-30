'''Given three integers, print the smallest one.(Three integers should be user input)'''

num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
num3=int(input('enter third number:'))
if (num1<num2)and(num1<num3):
    print('the first entered number is the smallest one')
elif (num2<num1)and(num2<num3):
    print('the second entered number is the smallest one')
else:
    print('the third entered number is the smallest one')