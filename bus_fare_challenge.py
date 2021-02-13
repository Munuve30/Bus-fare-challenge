# WRITE YOUR CODE SOLUTION HERE


        ##Importing Date module
import datetime
import time
from datetime import date

date=date.today()
print("Date:",date)
print("Day:",datetime.date.today().strftime("%a"))

day=time.strftime("%a")
week = set(["Mon","Tue","Wed","Thur","Fri"])
Sat = set(["Sat"])
Sun = set(["Sun"])

if day in week:
    print("Fare: 100")
elif day in Sat :
    print("Fare: 60")

elif day in Sun:
    print("Fare: 80")