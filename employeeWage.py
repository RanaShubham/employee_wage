import json
import random
from abc import ABC
from functools import reduce
from typing import List, Any

class IBM(ABC):
    COMPANY_NAME = "IBM"
    WAGE_PER_HOUR = 40
    FULL_DAY_HRS = 8
    PART_TIME_HRS = 4
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HRS = 100

class MICROSOFT(ABC):
    COMPANY_NAME = "MICROSOFT"
    WAGE_PER_HOUR = 50
    FULL_DAY_HRS = 9
    PART_TIME_HRS = 5
    MAX_WORKING_DAYS = 16
    MAX_WORKING_HRS = 120

class FLIPKART(ABC):
    COMPANY_NAME = "FLIPKART"
    WAGE_PER_HOUR = 30
    FULL_DAY_HRS = 12
    PART_TIME_HRS = 6
    MAX_WORKING_DAYS = 25
    MAX_WORKING_HRS = 120

class EmployeeWage (MICROSOFT, FLIPKART, IBM):
    companyList: List[Any] = []

    def __init__ (self, *args):
        self . company_name = args[0]
        self . wage_per_hour = args[1]
        self . part_time_hour = args[2]
        self . full_time_hour = args[3]
        self . monthly_working_days = args[4]
        self . max_working_hrs = args[5]
        self . daily_wage_list = []

    def hours_worked_today(self, part_time_hr, full_day_hr):
        '''
        To get the number of hours work was done today . 
        :return: integer signifying hours of work done today
        :rtype: int
        '''
        attendance_today = random . randint(0, 2)
        return 0 if attendance_today == 0\
            else full_day_hr if attendance_today == 1\
            else part_time_hr

    def create_daily_wage_list(self):
        '''
        Creates a daily salary list of employee for the company . 
        :return: List of daily salaries . 
        :rtype: List
        '''
        work_hours_count = 0
        for _ in range(0, self . monthly_working_days, 1):
            if (work_hours_count >= self . max_working_hrs):
                break
            work_hrs_today = self . hours_worked_today(self . part_time_hour, self . full_time_hour)
            work_hours_count = work_hours_count + work_hrs_today
            self . daily_wage_list . append(work_hrs_today * self . wage_per_hour)
        
    def get_monthly_wage(self):
        '''
        Calculates total wage from the wage list.
        :return: Total wage
        :rtype: int
        '''
        self.create_daily_wage_list()
        return reduce(lambda x,y : x+y, self . daily_wage_list)

def main():
    flipakrt = EmployeeWage(FLIPKART . COMPANY_NAME,
                    FLIPKART . WAGE_PER_HOUR,
                    FLIPKART . PART_TIME_HRS,
                    FLIPKART . FULL_DAY_HRS,
                    FLIPKART . MAX_WORKING_DAYS,
                    FLIPKART . MAX_WORKING_HRS)
    print("Flipkart employee earned ", flipakrt.get_monthly_wage())
    flipakrt_emp_dict = flipakrt.__dict__

    EmployeeWage.companyList.append(flipakrt)

    ibm = EmployeeWage(IBM.COMPANY_NAME,
                            IBM.WAGE_PER_HOUR,
                            IBM.PART_TIME_HRS,
                            IBM.FULL_DAY_HRS,
                            IBM.MAX_WORKING_DAYS,
                            IBM.MAX_WORKING_HRS)
    print("Ibm employee earned ", ibm.get_monthly_wage())
    ibm_emp_dict = ibm.__dict__

    EmployeeWage.companyList.append(ibm)

    microsoft = EmployeeWage(MICROSOFT.COMPANY_NAME,
                            MICROSOFT.WAGE_PER_HOUR,
                            MICROSOFT.PART_TIME_HRS,
                            MICROSOFT.FULL_DAY_HRS,
                            MICROSOFT.MAX_WORKING_DAYS,
                            MICROSOFT.MAX_WORKING_HRS)
    print("Microsoft employee earned ", microsoft.get_monthly_wage())
    microsoft_emp_dict = microsoft.__dict__

    EmployeeWage.companyList.append(microsoft)

    with open ('.//CompanyDetails.json') as myFile:
        json.dump(ibm_emp_dict, myFile, indent= 4)
        json.dump(microsoft_emp_dict, myFile, indent=4)
        json.dump(flipakrt_emp_dict, myFile, indent=4)

if __name__ == "__main__":
    main()