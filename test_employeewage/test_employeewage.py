import pytest

from com.bridgelabz.employeewage.employeeWage import EmployeeWage
from com.bridgelabz.employeewage.employeeWageException import EmployeeWageException

empwage = EmployeeWage(
    company_name="xyz",
    wage_per_hour=10,
    part_time_hour=5,
    full_time_hour=10,
    monthly_working_days=20,
    max_working_hrs=100)

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

def test_hours_worked_today():
    for _ in range(1, 20, 1):
        time = empwage.hours_worked_today()
        assert (time == 0 or time == 10 or time == 5)

def test_create_daily_wage_list():
    assert  empwage.daily_wage_list.__len__() == 0
    empwage.create_daily_wage_list()
    assert  empwage.daily_wage_list.__len__() > 0

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