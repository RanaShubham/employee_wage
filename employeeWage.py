import random

FULL_DAY_HRS = 8
WAGE_PER_HR = 20
PART_TIME_HRS = 4

print ("Welcome to employee wage program")
employeeAttendance = random.randint(0,2)

attendance = {
    0 : 0,
    1 : FULL_DAY_HRS*WAGE_PER_HR,
    2 : PART_TIME_HRS*WAGE_PER_HR
}
print('Salary today is :  ', attendance.get(employeeAttendance))