
"""
This one is very similar to the last one. The only things I did to edit the
original code was to:
  - Add the current savings to the top of the loop. This fixed subtle bugs
  - Used the modulo operator (%) to calculate division more efficiently.

Reading user input and feeding it into the function is left as an exercise
for the reader :)
"""

def calculate_num_months_to_afford_dream_home_with_semiannual_raise(
        annual_salary, dream_home_cost, percentage_saved, semi_annual_raise_percent, r=0.04, portion_down_payment=0.25):
    """
    Calculates number of months of working at annual_salary assuming
    portion_saved per year to afford house at total_cost with bi-yearly
    raise
    """
    semi_annual_raise_decimal = semi_annual_raise_percent / 100
    decimal_saved = percentage_saved / 100
    monthly_dollars_saved = decimal_saved * (annual_salary / 12)
    down_payment_cost = portion_down_payment * dream_home_cost
    current_savings = 0
    months_needed = 0


    while current_savings < down_payment_cost:
        # Move this to the top of the loop to pass the test
        current_savings += monthly_dollars_saved + current_savings * (r / 12)
        months_needed += 1

        # This is a more efficient way to calculate divisibility by 6
        if not months_needed % 6:
            annual_salary += (semi_annual_raise_decimal * annual_salary)
            monthly_dollars_saved = decimal_saved * (annual_salary / 12)

    return current_savings, months_needed
