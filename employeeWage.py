import json
import random
from abc import ABC
from functools import reduce
from typing import List

class EmployeeWage :
    employee_wage_object_list = []

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

    @staticmethod
    def get_emp_wage_object(company_dict):
        employee_wage_object = EmployeeWage(
            company_dict.get("company_name"),
            company_dict.get("wage_per_hour"),
            company_dict.get("part_time_hour"),
            company_dict.get("full_time_hour"),
            company_dict.get("monthly_working_days"),
            company_dict.get("max_working_hrs"),
            company_dict.get("daily_wage_list")
        )
        return  employee_wage_object

def main():
    with open ('.//CompanyDetails.json', 'r') as data:
        company_dictionary_list = json.load(data)
        for company_dict in company_dictionary_list:
            emp_wage_obj =    EmployeeWage.get_emp_wage_object(company_dict)
            EmployeeWage.employee_wage_object_list.append(emp_wage_obj)
            print("{} employee earned Rs {}".format(emp_wage_obj.company_name, emp_wage_obj.get_monthly_wage()))


if __name__ == "__main__":
    main()