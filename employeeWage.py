import random

FULL_DAY_HRS = 8
WAGE_PER_HR = 20

print ("Welcome to employee wage program")
employeeAttendance = random.randint(0,1)

if employeeAttendance == 1:
    print("Salary for today is: ", FULL_DAY_HRS*WAGE_PER_HR )
else:
    print("Salary for today is: ", 0)