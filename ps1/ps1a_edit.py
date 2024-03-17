"""
Your code looks good in terms of logic. There are a few small structural things
I would change.

Breaking down a few things in my file:
  - if __name__ == '__main__': - runs this code IF this file is being run as
    the entry point to the application (e.g. python ps1_edit.py). Otherwise
    (e.g., this file is being imported as "from ps1 import ps1a_edit"), the
    code in 'main' won't run
  - Breaking logic into a function with descriptive name - often better practice to write
    logic in functions, and often ones that are as small as possible.
  - Condition in "while" clause - "while True"/break is often bad practice
    (unless it yields considerable optimizations in a particular case). It's
    better to define a while statement with a definite end clause in the "while".
    This is a bt of a nitpick, but it makes things clearer, in my opinion.
  - Default arguments for assumptions we are making, but could change under
    different circumstances
"""

def calculate_num_months_to_afford_dream_home(
        annual_salary, total_cost, percentage_saved, portion_down_payment=0.25, r=0.04):
    """
    Calculates number of months of working at annual_salary assuming
    portion_saved per year to afford house at total_cost
    """
    current_savings = 0
    months_needed = 0
    portion_saved = percentage_saved / 100
    monthly_dollars_saved = portion_saved * (annual_salary / 12)

    down_payment_cost = portion_down_payment * total_cost

    while current_savings < down_payment_cost:
        current_savings += monthly_dollars_saved + current_savings * (r/12)
        months_needed += 1
    return months_needed


if __name__ == '__main__':
    annual_salary = float(input("What is your annual salary? "))
    total_cost = float(input("What is the cost of your dream home? "))
    percentage_saved = float(input("What percentage of your monthly pay do you put towards the down payment? "))

    months_needed = calculate_num_months_to_afford_dream_home(annual_salary, total_cost, percentage_saved)
    print("Number of months:", months_needed)




