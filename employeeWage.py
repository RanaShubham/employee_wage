import random

FULL_DAY_HRS = 8
WAGE_PER_HR = 20
PART_TIME_HRS = 4
MONTHLY_WORKING_DAYS = 20
TOTAL_WORKING_HRS = 100

print ("Welcome to employee wage program")

attendance = {
    0 : (0,0),
    1 : (FULL_DAY_HRS*WAGE_PER_HR, FULL_DAY_HRS),
    2 : (PART_TIME_HRS*WAGE_PER_HR, PART_TIME_HRS)
}
monthlyWage = 0
totalWorkHours = 0
for i in range (1,MONTHLY_WORKING_DAYS,1):
    employeeAttendance = random.randint(0, 2)
    if totalWorkHours + attendance.get(employeeAttendance)[1]  > TOTAL_WORKING_HRS :
        break
    monthlyWage = monthlyWage + attendance.get(employeeAttendance)[0]
    totalWorkHours = totalWorkHours + attendance.get(employeeAttendance)[1]

print("Monthly salary is: ", monthlyWage)