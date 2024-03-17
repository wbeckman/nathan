from ps1.ps1b_edit import calculate_num_months_to_afford_dream_home_with_semiannual_raise

def test_case_one():
    annual_salary = 120000
    dream_home_cost = 500000
    percent_salary_saved = 5
    percent_semiannual_raise = 3

    expected_num_months = 142
    _, actual_num_months = calculate_num_months_to_afford_dream_home_with_semiannual_raise(
        annual_salary, dream_home_cost, percent_salary_saved, percent_semiannual_raise)
    assert(actual_num_months == expected_num_months)

def test_case_two():
    annual_salary = 80000
    dream_home_cost = 800000
    percent_salary_saved = 10
    percent_semiannual_raise = 3

    expected_num_months = 159
    _, actual_num_months = calculate_num_months_to_afford_dream_home_with_semiannual_raise(
        annual_salary, dream_home_cost, percent_salary_saved, percent_semiannual_raise)
    assert(actual_num_months == expected_num_months)

def test_case_three():
    annual_salary = 75000
    dream_home_cost = 1500000
    percent_salary_saved = 5
    percent_semiannual_raise = 5

    expected_num_months = 261
    _, actual_num_months = calculate_num_months_to_afford_dream_home_with_semiannual_raise(
        annual_salary, dream_home_cost, percent_salary_saved, percent_semiannual_raise)
    assert(actual_num_months == expected_num_months)