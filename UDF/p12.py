# Program 12 : Calculate and display the Net monthly salary for the two categories of employees, permanent and temporary, based on following inputs from the user – monthly salary, hourly rate, present/absent days’ count, incentives/bonus, income tax, etc

def calSalary():
    emp_type = input( "Enter employee type (Permanent/Temporary): ").strip().lower()

    if emp_type == "permanent":
        basic_salary = float(input("Enter Monthly Basic Salary: "))
        present_days = int(input("Enter number of days present: "))
        total_days = int(input("Enter total working days in month: "))
        incentives = float(input("Enter Incentives/Bonus: "))
        income_tax = float(input("Enter Income Tax amount: "))

        gross_salary = (basic_salary/ total_days)*present_days + incentives
        net_salary= gross_salary - income_tax

    elif emp_type=="temporary":
        hourly_rate = float(input("Enter Hourly Rate: ₹"))
        total_hours = float(input("Enter Total Hours Worked: "))
        bonus = float(input("Enter Bonus (if any): ₹"))
        income_tax = float(input("Enter Income Tax amount: ₹"))