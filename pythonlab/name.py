#WAP to print name and age entered by users in different printing code.

name=input('enter your name:')
age=int(input('enter your age:'))
print(f'My name is {name} and my age is {age}.')
print("My name is" ,name, "and my age is" ,age,)
print("My name is %s and my age is %d" % (name,age))
print("My name is" +name+ "and my age is" +str(age)+)
print("My name is {} and my age is {}".format(name, age))