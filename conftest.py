import pytest
from random import randint
from time import time
import logging

from Modules import Warning
from Modules import logger
import global_variables

@pytest.fixture(scope="function")
def random_number():
    return randint(1, 3), randint(1, 3)


@pytest.fixture(scope="function", autouse=True)
def timer(request):
    if "timer" in request.keywords:
        print("Start Function running")
        start = time()
        yield
        print("Function running ", time() - start)
    else:
        yield


@pytest.fixture(scope="session", autouse=True)
def setup():
    logger.setting_up_logger("info", "info", "log.log")
    # Init and adding Warning handler to logging
    warning_handler = Warning.WarningLogger(["SSH", "DB", "SERVER"])

    logging.Logger.warning_test = global_variables.warning_test
    warning = logging.getLogger(global_variables.warning_handler_name)
    yield
    warning_handler.

