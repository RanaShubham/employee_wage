import json
import random
import functools
from typing import List, Dict, Any
from com.bridgelabz.employeewage.employeeWageException import EmployeeWageException

class EmployeeWage :
    #List to store various company objects.
    employee_wage_object_list = []

    def __init__ (self, **kwargs):
        self . company_name = kwargs ["company_name"]
        self . wage_per_hour = kwargs ["wage_per_hour"]
        self . part_time_hour = kwargs ["part_time_hour"]
        self . full_time_hour = kwargs ["full_time_hour"]
        self . monthly_working_days = kwargs ["monthly_working_days"]
        self . max_working_hrs = kwargs ["max_working_hrs"]
        self . daily_wage_list = []

    def hours_worked_today(self):
        '''
            To get the number of hours work was done today .
            :return: integer signifying hours of work done today
            :rtype: int
        '''
        attendance_today = random . randint(0, 2)
        return 0 if attendance_today == 0\
            else self.full_time_hour if attendance_today == 1\
            else self.part_time_hour

    def create_daily_wage_list(self):
        '''
            Creates a daily salary list of employee for the company .
            :return: List of daily salaries .
            :rtype: List
        '''
        work_hours_count = 0
        for _ in range(0, self . monthly_working_days, 1):
            work_hrs_today = self.hours_worked_today()
            if (work_hours_count + work_hrs_today >= self . max_working_hrs):
                break
            self.daily_wage_list.append(work_hrs_today * self.wage_per_hour)
            work_hours_count = work_hours_count + work_hrs_today

    def get_monthly_wage(self):
        '''
            Calculates total wage from the wage list.
            :return: Total wage
            :rtype: int
        '''
        self.create_daily_wage_list()
        return functools.reduce(lambda x, y : x + y, self . daily_wage_list)

    @staticmethod
    def get_emp_wage_object(company_dict):
        """
            :param Dictionary of EmployeeWage  object data
            :return: EmployeeWage object
        """
        employee_wage_object = EmployeeWage(
            company_name = company_dict.get("company_name"),
            wage_per_hour = company_dict.get("wage_per_hour"),
            part_time_hour = company_dict.get("part_time_hour"),
            full_time_hour = company_dict.get("full_time_hour"),
            monthly_working_days = company_dict.get("monthly_working_days"),
            max_working_hrs = company_dict.get("max_working_hrs"),
            daily_wage_list = company_dict.get("daily_wage_list"))
        return  employee_wage_object

    @staticmethod
    def get_data_from_file(str):
        '''
            Parses through a json file to create a list of EmployeeWage type objects.
            :param str: File path
            :type str:  str
            :return:  EmployeeWage object list.
            :rtype:  list
        '''
        if not str.lower().endswith('.json'):
            raise EmployeeWageException("Not a json file.")
        try:
            with open(str, 'r') as data:
                company_dictionary_list = json.load(data)
                for company_dict in company_dictionary_list:
                    emp_wage_obj = EmployeeWage.get_emp_wage_object(company_dict)
                    EmployeeWage.employee_wage_object_list.append(emp_wage_obj)

            return  EmployeeWage.employee_wage_object_list
        except FileNotFoundError:
            raise  EmployeeWageException("File not found.")


def driver_function(file):
    '''
        Prints the total monthly wage for employees of different companies.
        :param file:
        :type file:
    '''
    for emp_wage_obj in EmployeeWage.get_data_from_file(file):
        print("{} employee earned Rs {}".format(emp_wage_obj.company_name, emp_wage_obj.get_monthly_wage()))

if __name__ == "__main__":
    driver_function('./CompanyDetails.json')