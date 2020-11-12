import random
class EmployeeWage:

    def __init__(self, company_name,  wage_per_hour,  part_time_hour,  full_time_hour,  monthly_working_days,  total_working_days):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.part_time_hour = part_time_hour
        self.full_time_hour = full_time_hour
        self.monthly_working_days = monthly_working_days
        self.total_working_days = total_working_days
        self.attendance_type = { 0:0,
                                 1: self.full_time_hour,
                                 2: self.part_time_hour }

    def calculate_monthly_wage(self):
        """
        When called upon an EmployeeWage type object, calculates and returns monthly salary.
        
        :parameter
        self
        
        :returns
        Total wage at the end of month.
        """
        monthly_wage = 0
        total_work_hrs = 0
        
        for i in range(1, self.monthly_working_days, 1):
            
            attendance_today = random.randint(0, 2)
            if total_work_hrs + self.attendance_type.get(attendance_today) > self.total_working_days:
                break
            monthly_wage = monthly_wage + self.attendance_type.get(attendance_today) * self.wage_per_hour
            total_work_hrs = total_work_hrs + self.attendance_type.get(attendance_today)
            
        return monthly_wage

flipkart_object = EmployeeWage("Flipkart", 25, 6, 10, 25, 80)
ibm_object = EmployeeWage("IBM", 20, 4, 8, 20, 100)

flipkart_salary = flipkart_object.calculate_monthly_wage()
ibm_salary = ibm_object.calculate_monthly_wage()

print(flipkart_object.company_name,'employee earned Rs:',flipkart_salary,'for this month')
print(ibm_object.company_name, 'employee earned Rs:',ibm_salary,'for this month')