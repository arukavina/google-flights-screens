#!/usr/bin/python
# -*- coding: utf-8-*-

# Generic/Built-in
import os
import time
import logging

from datetime import datetime

# Libs
from selenium import webdriver

__author__ = "Andrei Rukavina"
__copyright__ = "Copyright 2020"
__credits__ = ["Andrei Rukavina"]
__license__ = "MPL 2.0"
__version__ = "0.1.0"
__maintainer__ = "Andrei Rukavina"
__email__ = "rukavina.andrei@gmail.com"
__status__ = "Dev"

SCREEN_OUTPUT = r'./screens'

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def scroll(browser, dim):
    return browser.execute_script('return document.body.parentNode.scroll' + dim)


def google_flight_screen_capture(driver, from_date, to_date, from_place, to_place, currency='USD'):
    base_url = 'https://www.google.com/flights?hl=en-US#flt={0}.{1}.{2}*{1}.{0}.{3};c:{4};e:1;sd:1;t:f'
    url = base_url.format(from_place, to_place, from_date, to_date, currency)

    logger.info('Getting URL: {}'.format(url))
    driver.get(url)

    logger.info('Loading...')
    time.sleep(2.5)

    screenshot_fn = '{}_google-flights_roundtrip_{}-{}_dates_{}-{}_{}.png'.format(
        datetime.now().strftime("%Y-%m-%d_%H-%M"),
        from_place,
        to_place,
        from_date,
        to_date,
        currency)

    logger.info('Saving evidence')
    driver.set_window_size(scroll(driver, 'Width'), scroll(driver, 'Height'))
    driver.find_element_by_tag_name('body').screenshot(os.path.join(SCREEN_OUTPUT, screenshot_fn))


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.headless = True

    driver = webdriver.Chrome('./chromedriver', options=options)

    from_date = datetime.date(datetime.strptime("2020-03-02", "%Y-%m-%d"))
    to_date = datetime.date(datetime.strptime("2020-03-13", "%Y-%m-%d"))

    google_flight_screen_capture(driver, from_date, to_date, 'JFK', 'SFO', 'USD')

    driver.close()
