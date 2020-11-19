import json
import pytest
from com.bridgelabz.employeewage.employeeWage import EmployeeWage

def get_test_data_list():
    test_data = './test_data_companies.json'
    with open(test_data, "r") as data:
        test_data_list: [EmployeeWage] = json.load(data)
    return  test_data_list

@pytest.fixture( params = get_test_data_list())
def get_my_test_data(request):
    '''
        My custom fixture. By using this fixture pytest executes the test method for each element in the list params.

        :param request: A request for a fixture from a test or fixture function.  A request object gives access to the requesting test context and has an optional param attribute in case the fixture is parametrized indirectly.
        :type request: fixture
        :return: request.param
        :rtype:dict
    '''
    return  request.param