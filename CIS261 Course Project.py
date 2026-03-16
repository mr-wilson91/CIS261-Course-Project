# ********************************************************
# Name: Tyquan Wilson
# Class: CIS261
# Lab: Course Project Phase 4
# ********************************************************

from datetime import datetime

USERS_FILE = "Users.txt"
EMPLOYEES_FILE = "Employees.txt"

def load_user_ids():
    user_ids = []
    try:
        with open(USERS_FILE, "a+") as file:
            file.seek(0)
            for line in file:
                user_data = line.strip().split("|")
                if len(user_data) >= 1:
                    user_ids.append(user_data[0])
    except Exception as e:
        print("Error loading users:", e)
    return user_ids

def get_user_name():
    return input("Enter user name or 'End' to quit: ").strip()

def get_user_password():
    return input("Enter password: ").strip()

def get_user_role():
    while True:
        role = input("Enter role (Admin or User): ").strip()
        if role.upper() == "ADMIN" or role.upper() == "USER":
            return role.title()
        else:
            print("Invalid role. Enter Admin or User.")

def create_users():
    print("##### Create users, passwords, and roles #####")
    user_ids = load_user_ids()

    with open(USERS_FILE, "a") as user_file:
        while True:
            username = get_user_name()
            if username.upper() == "END":
                break

            if username in user_ids:
                print("User name already exists. Enter a different user name.")
                continue

            password = get_user_password()
            role = get_user_role()

            user_detail = username + "|" + password + "|" + role + "\n"
            user_file.write(user_detail)
            user_ids.append(username)
            print("User added successfully.\n")

def print_user_info():
    print("\n##### Current Users #####")
    try:
        with open(USERS_FILE, "r") as user_file:
            has_users = False
            for line in user_file:
                user_detail = line.strip().split("|")
                if len(user_detail) == 3:
                    has_users = True
                    print("User Name:", user_detail[0], " Password:", user_detail[1], " Role:", user_detail[2])
            if not has_users:
                print("No users found.")
    except FileNotFoundError:
        print("No users found.")

def login():
    login_list = []

    try:
        with open(USERS_FILE, "r") as user_file:
            for line in user_file:
                user_detail = line.strip().split("|")
                if len(user_detail) == 3:
                    login_list.append(user_detail)
    except FileNotFoundError:
        return "None", "None"

    user_name = input("\nEnter User Name: ").strip()
    password = input("Enter Password: ").strip()

    for user in login_list:
        if user_name == user[0]:
            if password == user[1]:
                return user[2], user[0]
            else:
                print("Invalid password.")
                return "None", user_name

    print("Invalid user ID.")
    return "None", user_name

def get_emp_name():
    return input("Enter employee name or 'End' to quit: ").strip()

def get_dates_worked():
    while True:
        from_date = input("Enter Start Date (mm/dd/yyyy): ").strip()
        to_date = input("Enter End Date (mm/dd/yyyy): ").strip()

        try:
            datetime.strptime(from_date, "%m/%d/%Y")
            datetime.strptime(to_date, "%m/%d/%Y")
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Try again.\n")

def get_hours_worked():
    while True:
        try:
            hours = float(input("Enter amount of hours worked: "))
            if hours < 0:
                print("Hours must be 0 or greater.")
            else:
                return hours
        except ValueError:
            print("Invalid number. Try again.")

def get_hourly_rate():
    while True:
        try:
            rate = float(input("Enter hourly rate: "))
            if rate < 0:
                print("Hourly rate must be 0 or greater.")
            else:
                return rate
        except ValueError:
            print("Invalid number. Try again.")

def get_tax_rate():
    while True:
        try:
            tax_rate = float(input("Enter tax rate (decimal): "))
            if tax_rate < 0:
                print("Tax rate must be 0 or greater.")
            else:
                return tax_rate
        except ValueError:
            print("Invalid number. Try again.")

def calc_tax_and_net_pay(hours, hourly_rate, tax_rate):
    gross_pay = hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def write_employee_to_file(file_handle, from_date, to_date, emp_name, hours, hourly_rate, tax_rate):
    emp_detail = f"{from_date}|{to_date}|{emp_name}|{hours}|{hourly_rate}|{tax_rate}\n"
    file_handle.write(emp_detail)

def display_employee(from_date, to_date, emp_name, hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
    print(from_date, to_date, emp_name,
          f"{hours:,.2f}",
          f"{hourly_rate:,.2f}",
          f"{gross_pay:,.2f}",
          f"{tax_rate:,.1%}",
          f"{income_tax:,.2f}",
          f"{net_pay:,.2f}")

def display_totals(emp_totals):
    print()
    print(f'Total Number Of Employees: {emp_totals["TotEmp"]}')
    print(f'Total Hours Worked: {emp_totals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {emp_totals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {emp_totals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {emp_totals["TotNetPay"]:,.2f}')

def print_info(details_printed, user_name, user_role):
    tot_employees = 0
    tot_hours = 0.00
    tot_gross_pay = 0.00
    tot_tax = 0.00
    tot_net_pay = 0.00
    emp_totals = {}

    while True:
        run_date_input = input("Enter start date for report (MM/DD/YYYY) or All for all data in file: ").strip()
        if run_date_input.upper() == "ALL":
            run_date = "ALL"
            break
        try:
            run_date = datetime.strptime(run_date_input, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.\n")

    print("\nUser ID:", user_name)
    print("Authorization Code:", user_role)
    print()
    print("From Date  To Date    Employee Name   Hours    Rate    Gross Pay   Tax Rate   Tax Amount   Net Pay")

    try:
        with open(EMPLOYEES_FILE, "r") as emp_file:
            while True:
                emp_detail = emp_file.readline()
                if not emp_detail:
                    break

                emp_detail = emp_detail.strip()
                emp_list = emp_detail.split("|")

                if len(emp_list) != 6:
                    continue

                from_date = emp_list[0]

                if run_date != "ALL":
                    check_date = datetime.strptime(from_date, "%m/%d/%Y")
                    if check_date < run_date:
                        continue

                to_date = emp_list[1]
                emp_name = emp_list[2]
                hours = float(emp_list[3])
                hourly_rate = float(emp_list[4])
                tax_rate = float(emp_list[5])

                gross_pay, income_tax, net_pay = calc_tax_and_net_pay(hours, hourly_rate, tax_rate)

                display_employee(from_date, to_date, emp_name, hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)

                tot_employees += 1
                tot_hours += hours
                tot_gross_pay += gross_pay
                tot_tax += income_tax
                tot_net_pay += net_pay

                emp_totals["TotEmp"] = tot_employees
                emp_totals["TotHrs"] = tot_hours
                emp_totals["TotGrossPay"] = tot_gross_pay
                emp_totals["TotTax"] = tot_tax
                emp_totals["TotNetPay"] = tot_net_pay

                details_printed = True

        if details_printed:
            display_totals(emp_totals)
        else:
            print("No detail information to print")

    except FileNotFoundError:
        print("No employee data file found.")

if __name__ == "__main__":
    create_users()
    print_user_info()

    print("\n##### Data Entry #####")
    user_role, user_name = login()

    details_printed = False

    if user_role == "None":
        print(user_name, "is invalid.")
    else:
        if user_role.upper() == "ADMIN":
            with open(EMPLOYEES_FILE, "a+") as emp_file:
                while True:
                    emp_name = get_emp_name()
                    if emp_name.upper() == "END":
                        break

                    from_date, to_date = get_dates_worked()
                    hours = get_hours_worked()
                    hourly_rate = get_hourly_rate()
                    tax_rate = get_tax_rate()

                    write_employee_to_file(emp_file, from_date, to_date, emp_name, hours, hourly_rate, tax_rate)

            print_info(details_printed, user_name, user_role)

        elif user_role.upper() == "USER":
            print_info(details_printed, user_name, user_role)


