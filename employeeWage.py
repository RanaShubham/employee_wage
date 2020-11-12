import random

FULL_DAY_HRS = 8
WAGE_PER_HR = 20
PART_TIME_HRS = 4

print ("Welcome to employee wage program")
employeeAttendance = random.randint(0,2)

if employeeAttendance == 1:
    print("Salary for today is: ", FULL_DAY_HRS*WAGE_PER_HR )
elif employeeAttendance == 2:
    print("Salary for today is: ", PART_TIME_HRS*WAGE_PER_HR)
else:
    print("Salary for today is ", 0)