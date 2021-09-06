import time ;
import datetime;
import calendar;
from datetime import datetime as dt;

print(time.time())   #print the number spend since 12 AM,1st january 1970.

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time()))) #local

print(datetime.datetime.now())  #date and time print hoga

print(datetime.datetime(2021,8,2)) #aap jab date aayega mujhe batao use code kara.

print(datetime.datetime(2021,8,2,12,4,5,1))

cal=calendar.month(2021,12)

print(cal)

if (dt.now().year,dt.now().month,dt.now()<dt.now()<dt.now().year,dt.now().
    month,dt.now().day,16):
    print('working time')
else :
    print('fun hours')

c=calendar.prcal(int(input("Enter year :"))) #user input calendar

print(c)    
'''
for x in range(1,11):
    print(x)

    time.sleep()

'''
