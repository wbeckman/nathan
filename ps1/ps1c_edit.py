"""
Again, your logic looks good and binary search is a good algo to
implement.

A few more things in this file
  - Typically, "magic numbers" are bad practice. When you are defining
    your loops like (6,37,6), you want to make it as clear as possible
    what these numbers actually mean
  - Naming conventions in python dictate not naming variables with capital
    letters. Python naming conventions are always snake_case <- lowercase,
    separated by underscores.
  - Notice how I break smaller units of functionality into small functions
    that do one thing. You did the same with your Savings_func function.
    It's usually good practice to have very small and concentrated functions.

Of course, these are all more guidelines for reusable/production code and
anything goes in school projects. I do think, however, coding by these
guidelines helps you clarify your thinking.
"""

def within_tolerance(target_num, my_num, tolerance=100):
    """Computes if my_num is within tolerance of target_num"""
    return abs(my_num - target_num) <= tolerance

def calculate_savings_for_num_months(num_months, salary, portion_saved, semiannual_raise_portion=0.07, r=0.04):
    """
    Calculates savings after num_months at salary and annual savings rate (r),
    assuming semi-annual raise
    """
    monthly_dollars_saved = portion_saved * (salary / 12)
    current_savings = 0

    for month_num in range(1, num_months+1):
        current_savings += monthly_dollars_saved + current_savings * (r / 12)

        if not month_num % 6:
            salary += (semiannual_raise_portion * salary)
            monthly_dollars_saved = portion_saved * (salary / 12)


    print(f"Current salary: {salary}")
    print(f"Savings after {num_months} months: {current_savings}")
    print(f"Savings rate: {portion_saved}")
    return current_savings

def bisection_search(
        salary, max_num_months=36, semiannual_raise_portion=0.07, r=0.04,
        portion_down_payment=0.25, total_cost=1000000):
    """
    Binary searches savings rates to find a savings rate that allows us to
    put a down payment on our house, given our salary. If we find one, we
    return the rate and the number of iterations it took to find it.
    If we can't find a savings rate that allows for this, we return None, None
    """
    num_steps = 0
    savings = 0.0
    low, high = 1,10000
    down_payment_cost = portion_down_payment * total_cost
    while not within_tolerance(down_payment_cost, savings) and not low == high:
        middle = (low + high) / 2
        savings = calculate_savings_for_num_months(
            max_num_months, salary, middle/10000, semiannual_raise_portion, r)
        print(f"Current salary: {salary}")
        print(f"Savings after {max_num_months} months: {savings}")
        print(f"Savings rate: {middle / 10000}")
        middle = (low + high) / 2
        num_steps += 1
        if savings < down_payment_cost:
            low = middle
        else:
            high = middle

    if low == high:
        # We can't find a savings rate that allows us to put $ down in <max_num_months :(
        return None, None
    return middle / 10000, num_steps
