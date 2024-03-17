from ps1.ps1c_edit import bisection_search


def test_case_one():
    starting_salary = 150000
    expected_best_savings_rate = 0.4411
    expected_steps_in_bisection_search = 12
    actual_best_savings_rate, actual_steps_in_bisection_search = bisection_search(starting_salary)
    assert(round(expected_best_savings_rate, 3) == round(actual_best_savings_rate, 3))
    assert (expected_steps_in_bisection_search == expected_steps_in_bisection_search)

def test_case_two():
    starting_salary = 300000
    expected_best_savings_rate = 0.2206
    expected_steps_in_bisection_search = 9
    actual_best_savings_rate, actual_steps_in_bisection_search = bisection_search(starting_salary)
    assert (round(expected_best_savings_rate) == round(actual_best_savings_rate))
    assert (expected_steps_in_bisection_search == expected_steps_in_bisection_search)


def test_case_three():
    starting_salary = 10000
    expected_best_savings_rate = None
    expected_steps_in_bisection_search = None
    actual_best_savings_rate, actual_steps_in_bisection_search = bisection_search(starting_salary)
    assert (expected_best_savings_rate == actual_best_savings_rate)
    assert (expected_steps_in_bisection_search == expected_steps_in_bisection_search)
