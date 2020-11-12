import random
class EmployeeWage:
    FULL_DAY_HRS = 8
    WAGE_PER_HR = 20
    PART_TIME_HRS = 4
    MONTHLY_WORKING_DAYS = 20
    TOTAL_WORKING_HRS = 100
    ATTENDANCE = {
        0 : (0,0),
        1 : (FULL_DAY_HRS*WAGE_PER_HR, FULL_DAY_HRS),
        2 : (PART_TIME_HRS*WAGE_PER_HR, PART_TIME_HRS)
    }

    @staticmethod
    def calculateMonthlyWage():
        monthlyWage = 0
        totalWorkHours = 0
        for i in range(1, EmployeeWage.MONTHLY_WORKING_DAYS, 1):
            employeeAttendance = random.randint(0, 2)
            if totalWorkHours + EmployeeWage.ATTENDANCE.get(employeeAttendance)[1] > EmployeeWage.TOTAL_WORKING_HRS:
                break
            monthlyWage = monthlyWage + EmployeeWage.ATTENDANCE.get(employeeAttendance)[0]
            totalWorkHours = totalWorkHours + EmployeeWage. ATTENDANCE.get(employeeAttendance)[1]
        return monthlyWage

wage = EmployeeWage.calculateMonthlyWage()
print(wage)