import random

FULL_DAY_HRS = 8
WAGE_PER_HR = 20
PART_TIME_HRS = 4
MONTHLY_WORKING_DAYS = 20

print ("Welcome to employee wage program")

attendance = {
    0 : 0,
    1 : FULL_DAY_HRS*WAGE_PER_HR,
    2 : PART_TIME_HRS*WAGE_PER_HR
}
monthlyWage = 0
for i in range (1,MONTHLY_WORKING_DAYS,1):
    employeeAttendance = random.randint(0, 2)
    monthlyWage = monthlyWage + attendance.get(employeeAttendance)

print("Monthly salary is: ", monthlyWage)