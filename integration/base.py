# -*- coding: utf-8 -*-
from selenium import webdriver

import os
import time
import logging

log = logging.getLogger('seltest')
log.addHandler(logging.NullHandler())


class WebTest(object):
    """
    A tester object which can be entered and exited:

    tester = WebTest()
    with tester:
       test_base()
    """

    def __enter__(self):
        log.debug('Starting Chrome')

        # start a headless chrome webdriver
        # options are so that it works in Docker
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        log.debug('Started Chrome')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        log.debug('Exited Chrome')

    def test_base(self):
        """
        An example test.

        The easiest way to generate these tests is to get the
        rough idea using Katalon Recorder, and then embeding
        yourself in an interactive terminal to nail down the
        specifics by inserting:


        from IPython import embed
        embed()
        """
        driver = self.driver

        # LANDING PAGE
        driver.get("http://www.google.com/")

        # google's home page has a link to their privacy policy
        privacy = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Privacy')]")

        # it should return a list with something in it
        assert len(privacy) == 1

        # get the element
        element = privacy[0]
        # it should be displayed
        assert element.is_displayed()
        # it should have nonzero size
        assert element.size['height'] > 10
        assert element.size['width'] > 10

        log.debug('All Checks Succeeded!')


if __name__ == "__main__":
    tester = WebTest()
    with tester:
        tester.test_base()
