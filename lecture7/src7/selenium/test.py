import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

class WebpageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title(self):
        self.driver.get(file_uri("counter.html"))
        self.assertEqual(self.driver.title, "Counter")

    def test_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        increase.click()
        wait = WebDriverWait(self.driver, 10)
        h1_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(h1_element.text, "1")

    def test_decrease(self):
        self.driver.get(file_uri("counter.html"))
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        wait = WebDriverWait(self.driver, 10)
        h1_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(h1_element.text, "-1")

    def test_multiple_increase(self):
        self.driver.get(file_uri("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        for i in range(3):
            increase.click()
        wait = WebDriverWait(self.driver, 10)
        h1_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(h1_element.text, "3")

if __name__ == "__main__":
    unittest.main()