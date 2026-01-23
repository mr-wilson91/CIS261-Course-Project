# Name: Tyquan Wilson
# Class: CIS261
# Lab: Course Project Phase 1
# Date: January 22, 2026

def get_input(prompt, min_val=0, max_val=float('inf')):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print("Value out of range.")
        except ValueError:
            print("Invalid input. Enter a number.")

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def display_employee(name, hours, rate, gross, tax_rate, tax, net):
    print("\nEmployee:", name)
    print("Hours Worked:", hours)
    print("Hourly Rate: $", format(rate, ".2f"))
    print("Gross Pay: $", format(gross, ".2f"))
    print("Tax Rate:", format(tax_rate * 100, ".2f"), "%")
    print("Income Tax: $", format(tax, ".2f"))
    print("Net Pay: $", format(net, ".2f"))

def display_totals(emps, hours, gross, tax, net):
    print("\n--- Payroll Summary ---")
    print("Total Employees:", emps)
    print("Total Hours:", hours)
    print("Total Gross Pay: $", format(gross, ".2f"))
    print("Total Income Tax: $", format(tax, ".2f"))
    print("Total Net Pay: $", format(net, ".2f"))

def main():
    total_emps = total_hours = total_gross = total_tax = total_net = 0

    while True:
        name = input("\nEnter employee name (or End to finish): ")
        if name.lower() == "end":
            break

        hours = get_input("Enter hours worked: ", 0, 168)
        rate = get_input("Enter hourly rate: ", 0)
        tax_rate = get_input("Enter tax rate (as decimal): ", 0, 1)

        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        display_employee(name, hours, rate, gross, tax_rate, tax, net)

        total_emps += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

    if total_emps > 0:
        display_totals(total_emps, total_hours, total_gross, total_tax, total_net)

if __name__ == "__main__":
    main()
