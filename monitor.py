"""
A worker which provides periodic monitoring and testing.
"""
import time
import logging

# import our tester object
from integration.base import WebTest

# record events using python logging
log = logging.getLogger('seltest')
# set formatter to show line numbers
_formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)-7s " +
    "(%(filename)s:%(lineno)3s) %(message)s",
    "%Y-%m-%d %H:%M:%S")
# print log events to terminal
_handler = logging.StreamHandler()
_handler.setFormatter(_formatter)
log.addHandler(_handler)
log.setLevel(logging.DEBUG)


def integration_test(period):
    """
    Will run an integration test every `period`.

    Parameters
    --------------
    period: float, time to wait between tests
    """
    while True:
        # will open chromedriver
        tester = WebTest()
        with tester:
            try:
                tic = time.time()
                tester.test_base()
            except BaseException:
                log.error('Integration test failed!',
                          exc_info=True)
                continue
        log.debug('Successfully tested in {:0.3f}'.format(
            time.time() - tic))
        log.debug('Sleeping for {}s'.format(period))
        time.sleep(period)


if __name__ == "__main__":
    # start the integration test
    integration_test(period=500.0)
