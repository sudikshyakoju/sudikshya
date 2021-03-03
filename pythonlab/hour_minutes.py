'''Given the integer N - the number of minutes that is passed since midnight- how many hours and minutes are
displayed on the 24hr digital clock? the program should print 2 numbers: the number of hours(between 0 and 23)
and the  number of minutes (between 0 and 59)'''

n=int(input('enter the number:'))
hrs=(n//60)
min=(n%60)
print(f"the hours is {hrs}")
print(f"The minutes is {min}")
print(f"It is {hrs}:{min}")
