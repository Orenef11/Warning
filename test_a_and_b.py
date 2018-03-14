import pytest
import logging

import global_variables

warning = logging.getLogger(global_variables.warning_handler_name)


@pytest.mark.timer
def test_a(random_number):
    first_num, second_num = random_number
    warning.warning_test("ssh: Connection testing")
    # print("ddddddddddddddddddddddddd", global_variables.warning_handler_name)
    # assert first_num == second_num == 1, "Test A Failed"


# @pytest.mark.timer
def test_b(random_number):
    first_num, second_num = random_number
    warning.warning_test("Connection testing")
    # assert first_num == second_num == 2, "Test A Failed"

