def calSalary():
    emp_type = input("Enter employee type (Permanent/Temporary): ").strip().lower()

    if emp_type == "permanent":
        basic_salary = float(input("Enter Monthly Basic Salary: "))
        present_days = int(input("Enter number of days present: "))
        total_days = int(input("Enter total working days in month: "))
        incentives = float(input("Enter Incentives/Bonus: "))
        income_tax = float(input("Enter Income Tax amount: "))

        gross_salary = (basic_salary / total_days) * present_days + incentives
        net_salary = gross_salary - income_tax

        print(f"\nGross Salary: ₹{gross_salary:.2f}")
        print(f"Net Salary: ₹{net_salary:.2f}")

    elif emp_type == "temporary":
        hourly_rate = float(input("Enter Hourly Rate: ₹"))
        total_hours = float(input("Enter Total Hours Worked: "))
        bonus = float(input("Enter Bonus (if any): ₹"))
        income_tax = float(input("Enter Income Tax amount: ₹"))

        gross_salary = hourly_rate * total_hours + bonus
        net_salary = gross_salary - income_tax

        print(f"\nGross Salary: ₹{gross_salary:.2f}")
        print(f"Net Salary: ₹{net_salary:.2f}")

    else:
        print("Invalid employee type entered.")
