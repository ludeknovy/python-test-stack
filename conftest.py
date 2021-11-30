import logging
import os
import uuid
from datetime import datetime
from time import time

import pytest

from endpoints.api_tester import ApiTester  # type: ignore

logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)


@pytest.fixture()
def api_tester(request):
    # UUID used for request(s) tracing
    global x_test_id
    x_test_id = str(uuid.uuid4())

    return ApiTester(x_test_id=x_test_id)


def pytest_addoption(parser):
    parser.addoption(
        "--local-logs",
        action="store_true",
        help="Logs all communication into local log file for each test"
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "property_test(): mark property based api tests"
    )


@pytest.fixture(autouse=True)
def file_logger(request):
    log_communication = request.config.getoption("--local-logs")
    if log_communication:
        test_name = request.node.name.replace("/", ".")
        time_info = datetime.fromtimestamp(time()).strftime('%Y-%m-%d__%H-%M-%S')

        if not os.path.exists("logs"):
            try:
                os.makedirs("logs")
            except OSError:
                logging.error("logs folder was not created")
                pass
        file_handler = logging.FileHandler(f'logs/{test_name}__{time_info}.log')
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        yield
        logger.removeHandler(file_handler)
    else:
        yield


def pytest_exception_interact(node, call, report):
    if 'x_test_id' in globals():
        debug_id_str = F'debug id: {x_test_id}'
        # This is only for local console output - for some reason ReportPortal does not log it
        report.longrepr.chain[0][0].extraline = f"\n{debug_id_str}"
        # This is needed in order to propagate this information in ReportPortal
        logger.error(debug_id_str)
