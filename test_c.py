import pytest


@pytest.mark.timer
def test_c(random_number):
    first_num, second_num = random_number
    assert first_num == second_num == 3, "Test C Failed"
