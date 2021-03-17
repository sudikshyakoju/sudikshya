'''A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes a,b and respectively.
In the first test there are three groups. The first group has 20 students and thus, need 10 desks.The second
group has21 students, so they can get by with no fewer than 11 desks. 11 desk are also enough for the third of
22 students. So, we need 32 desk in total.'''

students_class1= int(input('enter the no. of students in first class:'))
students_class2= int(input('enter the no. of students in second class:'))
students_class3= int(input('enter the no. of students in third class:'))

desk_class1 = (students_class1//2)
print(f"the required no. of desk for class1 is {desk_class1}")
desk_class1 = (students_class2//2)
print(f"the required no. of desk for class2 is {desk_class2}")
desk_class1 = (students_class3//2)
print(f"the required no. of desk for class3 is {desk_class3}")

remain_class1 = (students_class1%2)
print(f"the remaining no. of desk in class1 is {remain_class1}")
remain_class2 = (students_class2%2)
print(f"the remaining no. of desk in class2 is {remain_class2}")
remain_class3 = (students_class3%2)
print(f"the remaining no. of desk in class3 is {remain_class3}")

total=desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 +remain_class3
print(total)


