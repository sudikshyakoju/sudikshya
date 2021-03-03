'''A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes a,b and respectively.
In the first test there are three groups. The first group has 20 students and thus, need 10 desks.The second
group has21 students, so they can get by with no fewer than 11 desks. 11 desk are also enough for the third of
22 students. So, we need 32 desk in total.'''

students class1= int(input('enter the no. of students in first class:'))
students class2= int(input('enter the no. of students in second class:'))
students class3= int(input('enter the no. of students in third class:'))

desk class1 = (students class1//2)
print(f"the required no. of desk for class1 is {desk class1}")
desk class1 = (students class2//2)
print(f"the required no. of desk for class2 is {desk class2}")
desk class1 = (students class3//2)
print(f"the required no. of desk for class3 is {desk class3}")

remain class1 = (students class1%2)
print(f"the remaining no. of desk in class1 is {remain class1}")
remain class2 = (students class2%2)
print(f"the remaining no. of desk in class2 is {remain class2}")
remain class3 = (students class3%2)
print(f"the remaining no. of desk in class3 is {remain class3}")

total=desk class1 + desk class2 + desk class3 + remain class1 + remain class2 +remain class3
print(total)


