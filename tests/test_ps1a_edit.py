from ps1.ps1a_edit import calculate_num_months_to_afford_dream_home

def test_case_one():
    annual_salary = 120000
    dream_home_cost = 1000000
    percent_salary_saved = 10
    expected_num_months = 183
    actual_num_months = calculate_num_months_to_afford_dream_home(annual_salary, dream_home_cost, percent_salary_saved)
    assert(actual_num_months == expected_num_months)

def test_case_two():
    annual_salary = 80000
    dream_home_cost = 500000
    percent_salary_saved = 15
    expected_num_months = 105
    actual_num_months = calculate_num_months_to_afford_dream_home(annual_salary, dream_home_cost, percent_salary_saved)
    assert(actual_num_months == expected_num_months)
