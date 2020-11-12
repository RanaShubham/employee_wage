import random
class EmployeeWage:

    def __init__(self, companyName,  wagePerHr,  partTimeHr,  fullTimeHr,  monthlyWorkingDays,  totalWorkingHrs):
        self.companyName = companyName
        self.wagePerHr = wagePerHr
        self.partTimeHr = partTimeHr
        self.fullTimeHr = fullTimeHr
        self.monthlyWorkingDays = monthlyWorkingDays
        self.totalWorkingHrs = totalWorkingHrs
        self.attendanceType = { 0:(0,0), 1:(self.fullTimeHr*self.wagePerHr, self.fullTimeHr), 2:(self.partTimeHr*self.wagePerHr, self.partTimeHr) }

    def calculateMonthlyWage(self):
        monthlyWage = 0
        totalWorkHours = 0
        for i in range(1, self.monthlyWorkingDays, 1):
            attendanceToday = random.randint(0, 2)
            if totalWorkHours + self.attendanceType.get(attendanceToday)[1] > self.totalWorkingHrs:
                break
            monthlyWage = monthlyWage + self.attendanceType.get(attendanceToday)[0]
            totalWorkHours = totalWorkHours + self.attendanceType.get(attendanceToday)[1]
        return monthlyWage

flipkartObject = EmployeeWage("Flipkart", 10, 6, 10, 25, 80)
IBMObject = EmployeeWage("IBM", 20, 4, 8, 20, 100)

flipkartSalary = flipkartObject.calculateMonthlyWage()
ibmSalary = IBMObject.calculateMonthlyWage()

print(flipkartObject.companyName,'employee earned Rs: ', flipkartSalary)
print(IBMObject.companyName, 'employee earned Rs: ',ibmSalary)