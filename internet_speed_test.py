from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SPEED_TEST_URL = "https://fast.com"
CHROME_DRIVER_LOCATION = "/Users/hanklo/Development/chromedriver"


class InternetSpeedBot:

    def __init__(self):
        super().__init__()
        # Connect using Selenium
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION, options=self.options)
        self.driver.get(SPEED_TEST_URL)
        self.detail_button = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.ID, "show-more-details-link")))
        self.detail_button.click()

    def get_internet_speed(self):
        time.sleep(45)
        self.down_speed = float(self.driver.find_element(By.ID, "speed-value").text)
        # print(self.down_speed)
        self.up_speed = float(self.driver.find_element(By.ID, "upload-value").text)
        # print(self.up_speed)


    def keep_log(self, content):
        with open("speed_log.txt", mode='a') as file:
            file.writelines(f"{content}\n")

