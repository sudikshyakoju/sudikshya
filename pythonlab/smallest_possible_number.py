'''A school decided to replace the desks in three classrooms. Each desksits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes a,b and respectively.
In the first test there are three groups. The first group has 20 students and thus, need 10 desks.
The second group has21 students, so they can get by with no fewer than 11 desks. 11 desk are also enough for the
third of 22 students. So, we need 32 desk in total.'''

no. of students class1=int(input("enter the no. of students in first class:"))
no. of students class2=int(input("enter the no. of students in second class:"))
no. of students class3=int(input("enter the no. of students in third class:"))
desk for class1 = (no. of students class1//2)
print('the required no. of desk for class1 is'{desk for class1})
desk for class1 = (no. of students class2//2)
print('the required no. of desk for class2 is'{desk for class2})
desk for class1 = (no. of students class3//2)
print('the required no. of desk for class3 is'{desk for class3})
remain in class1 = no. of students class1 % 2
print('the remaining no. of desk in class1 is'{remain in class1})
remain in class2 = no. of students class2 % 2
print('the remaining no. of desk in class2 is'{remain in class2})
remain in class3 = no. of students class3 % 2
print('the remaining no. of desk in class3 is'{remain in class3})