'''WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more then 70% ->distinction, more than 60% ->first, more than 40% ->pass, less than 40% -.fail'''

eng=int(input('enter marks of english:'))
math=int(input('enter marks of maths:'))
sci=int(input('enter marks of science:'))
nep=int(input('enter marks of nepali:'))

total_marks=eng+math+sci+nep
percentage=(total_marks/400)*100

if (percentage>=70):
    print("distinction")
elif (percentage>=60):
    print("first division")
elif (percentage>=40):
    print("pass")
else:
    print("fail")
