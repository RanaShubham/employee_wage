import random
from functools import reduce
from typing import List, Any

class IBM:
    COMPANY_NAME = "IBM"
    WAGE_PER_HOUR = 30
    FULL_DAY_HRS = 8
    PART_TIME_HRS = 4
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HRS = 100

class MICROSOFT:
    COMPANY_NAME = "MICROSOFT"
    WAGE_PER_HOUR = 50
    FULL_DAY_HRS = 9
    PART_TIME_HRS = 5
    MAX_WORKING_DAYS = 25
    MAX_WORKING_HRS = 120

class FLIPKART:
    COMPANY_NAME = "FLIPKART"
    WAGE_PER_HOUR = 50
    FULL_DAY_HRS = 9
    PART_TIME_HRS = 5
    MAX_WORKING_DAYS = 25
    MAX_WORKING_HRS = 120

class EmployeeWage(MICROSOFT,FLIPKART,IBM):
    companyList: List[Any] = []

    def __init__(self, company_name, wage_per_hour, part_time_hour, full_time_hour, monthly_working_days, total_working_hrs):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.part_time_hour = part_time_hour
        self.full_time_hour = full_time_hour
        self.monthly_working_days = monthly_working_days
        self.total_working_hrs = total_working_hrs
        self.attendance_type = {0: 0,
                                1: self.full_time_hour,
                                2: self.part_time_hour}
        self.daily_office_time_list = []

    def attendance(self):
        """
        When called upon an EmployeeWage type object, returns a list of daily salary for employee.

        :parameter
        self

        :returns
        Daily wage list.
        """
        total_work_hrs = 0
        for i in range(1, self.monthly_working_days, 1):
            attendance_today = random.randint(0, 2)
            if total_work_hrs + self.attendance_type.get(attendance_today) > self.total_working_hrs:
                break
            self.daily_office_time_list.append(self.attendance_type.get(1))
            total_work_hrs = total_work_hrs + self.attendance_type.get(1)

        return reduce(lambda x, y: x + y, self.daily_office_time_list)

    def get_total_wage(self):
        """
        Call this method on a EmployeeWage type to get total wage of the employee for a month.

        :returns: Total wage for a month
        """
        return self.attendance() * self.wage_per_hour


flipkart_object = EmployeeWage(
    FLIPKART.COMPANY_NAME,
    FLIPKART.WAGE_PER_HOUR,
    FLIPKART.PART_TIME_HRS,
    FLIPKART.FULL_DAY_HRS,
    FLIPKART.MAX_WORKING_DAYS,
    FLIPKART.WAGE_PER_HOUR
)
print(flipkart_object.get_total_wage())
EmployeeWage.companyList.append(flipkart_object)

ibm_object = EmployeeWage(
    IBM.COMPANY_NAME,
    IBM.WAGE_PER_HOUR,
    IBM.PART_TIME_HRS,
    IBM.FULL_DAY_HRS,
    IBM.MAX_WORKING_DAYS,
    IBM.WAGE_PER_HOUR
)
print(ibm_object.get_total_wage())
EmployeeWage.companyList.append(ibm_object)

microsoft_object = EmployeeWage(
    MICROSOFT.COMPANY_NAME,
    MICROSOFT.WAGE_PER_HOUR,
    MICROSOFT.PART_TIME_HRS,
    MICROSOFT.FULL_DAY_HRS,
    MICROSOFT.MAX_WORKING_DAYS,
    MICROSOFT.WAGE_PER_HOUR
)
print(microsoft_object.get_total_wage())
EmployeeWage.companyList.append(microsoft_object)
