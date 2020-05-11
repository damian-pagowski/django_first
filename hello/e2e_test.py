import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, 10)
base_url = 'http://localhost:8000'

class WebpageTests(unittest.TestCase):        

    def test_title(self):
        driver.get(base_url)
        self.assertEqual(driver.title, "Flights")

    def test_flights_number_should_be_2(self):
        driver.get(base_url)
        flights = driver.find_elements_by_tag_name('li')
        self.assertEqual(len(flights), 2)

    def test_first_flight_details(self):
        driver.get(base_url)
        first_flight = driver.find_elements_by_tag_name('li')[0]
        first_flight.find_element_by_css_selector('a').click()
        self.assertEqual(driver.title, "Flight 1")

    @classmethod
    def tearDownClass(cls):
        driver.close()


if __name__ == "__main__":
    unittest.main()