import json

import pytest

from com.bridgelabz.employeewage.employeeWage import EmployeeWage
from com.bridgelabz.employeewage.employeeWageException import EmployeeWageException

corrupt_empwage = EmployeeWage(
    company_name=123,
    wage_per_hour="Ten",
    part_time_hour="Five",
    full_time_hour="Ten",
    monthly_working_days="Twenty",
    max_working_hrs="Hundred")

empwage_large_working_hrs = EmployeeWage(
     company_name="xyz",
     wage_per_hour=10,
     part_time_hour=5,
     full_time_hour=10,
     monthly_working_days=20,
     max_working_hrs=100000000)

empwage_large_working_days = EmployeeWage(
    company_name="xyz",
    wage_per_hour=10,
    part_time_hour=5,
    full_time_hour=10,
    monthly_working_days=100000000,
    max_working_hrs=20)

absent_file = './NoFile.json'
wrong_type_file = './WrongType.txt'

def test_hours_worked_today(get_my_test_data):
    company_test_object = EmployeeWage.get_emp_wage_object(get_my_test_data)
    time = company_test_object.hours_worked_today()
    assert (time == 0 or time == company_test_object.full_time_hour or time == company_test_object.part_time_hour)

def test_create_daily_wage_list(get_my_test_data):
    company_test_object = EmployeeWage.get_emp_wage_object(get_my_test_data)
    assert  company_test_object.daily_wage_list.__len__() == 0
    company_test_object.create_daily_wage_list()
    assert  company_test_object.daily_wage_list.__len__() > 0

def test_create_daily_wage_list_when_data_type_from_file_unexpected_should_throw_EmployeeWageException():
    with pytest.raises(EmployeeWageException) as error_type:
        corrupt_empwage.create_daily_wage_list()
    assert str(error_type.value) == "Data corrupt."

def test_create_daily_wage_list_when_large_maximum_working_hours_should_create_list_of_size_max_working_days():
    assert  empwage_large_working_hrs.daily_wage_list.__len__() == 0
    empwage_large_working_hrs.create_daily_wage_list()
    assert empwage_large_working_hrs.daily_wage_list.__len__() == 20

def test_get_monthly_wage_when_large_maximum_working_days_should_return_sal_less_or_equal_to_sal_for_max_working_hours():
    total_wage = empwage_large_working_days.get_monthly_wage()
    assert total_wage <= 1000

def test_get_data_file_when_json_file_to_read_company_data_not_found_should_raise_EmployeeWageException():
    with pytest.raises(EmployeeWageException) as error_type:
        EmployeeWage.get_data_from_file(wrong_type_file)
    assert  str(error_type.value) == "Not a json file."

def test_get_data_file_when_json_type_but_not_present_should_raise_EmployeeWageException():
    with pytest.raises(EmployeeWageException) as error_type:
        EmployeeWage.get_data_from_file(absent_file)
    assert  str(error_type.value) == "File not found."