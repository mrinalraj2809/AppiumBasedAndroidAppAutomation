
import time
import pytest
import logging
from lib.input_data import *
from lib.common_utils import CommonUtils
from lib.page_mini_tv import MiniTv
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import ArgOptions

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestAmazonMiniTV:
    @pytest.fixture(scope="class")
    def setup_driver(self):
        logger.info("================== SETUP ================= ")
        self.com_obj = CommonUtils()
        self.driver = self.com_obj.initialize_parameter()
        self.mini_tv_obj = MiniTv(self.driver)
        logger.info("============================================")
        return self.driver, self.mini_tv_obj

    def test_open_amazon_app(self, setup_driver):
        logger.info("================== LAUNCH AMAZON APP ================= ")
        self.driver, self.mini_tv_obj = setup_driver
        self.mini_tv_obj.handle_crash()
        self.mini_tv_obj.launch_amazon_app()
        logger.info("=======================================================")

    def test_open_mini_tv(self, setup_driver):
        logger.info("================== OPEN MINI TV ====================== ")
        self.driver, self.mini_tv_obj = setup_driver
        self.mini_tv_obj.handle_crash()
        self.mini_tv_obj.navigate_to_mini_tv()
        logger.info("=======================================================")

    def test_select_series(self, setup_driver):
        logger.info("================= SELECT SERIES ====================== ")
        self.driver, self.mini_tv_obj = setup_driver
        self.mini_tv_obj.handle_crash()
        self.mini_tv_obj.select_and_open_series_details()
        logger.info("=======================================================")

    def test_play_first_episode(self, setup_driver):
        logger.info("================= PLAY EPISODES ====================== ")
        self.driver, self.mini_tv_obj = setup_driver
        self.mini_tv_obj.handle_crash()
        self.mini_tv_obj.play_first_episodes()
        logger.info("=======================================================")

    def cleanup(self, setup_driver):
        try:
            self.driver, self.mini_tv_obj = setup_driver
            self.driver.quit()
        except Exception as e:
            print("Clean up failed")

if __name__ == "__main__":
    pytest.main()

# from appium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.options import ArgOptions
# import time
# def setup_driver():
#     options = ArgOptions()
#     options.platform_name = "Android"
#     options.device_name = "Android Emulator"
#     options.app_package = "com.google.android.apps.nexuslauncher"
#     options.app_activity = "com.google.android.apps.nexuslauncher.NexusLauncherActivity"
    
#     desired_caps = {
#         "platformVersion": "15",  # Ensure the platform version exists
#         "automationName": "UiAutomator2"
#     }
    
#     return webdriver.Remote('http://localhost:4723/wd/hub', options=options)

# driver = setup_driver()
# # driver.find_element("By.XPATH", "//android.widget.TextView[@content-desc='Predicted app: Amazon']").click()

# id_for_crash = "android:id/aerr_wait"
# def is_element_present(driver, id):
#     """
#     Method to return True if error popup present and selects "wait"
#     :param: driver: Web driver
#     :id
#     :returns True: True if popup present
#     """
#     try:
#         driver.find_element("id",id)
#         return True
#     except Exception as e:
#         print("Popup not present")
#         return False

# def perform_click(driver, id):
#     """
#     Method to perform click
#     :param driver: Web driver
#     :param xpath: Xpath locator to perform click
#     """
#     try:
#         # driver.wait_for_elememt()
#          driver.find_element("id",id).click()
#     except Exception as e:
#         print("perform_click failed")
#         raise

# def open_amazon_app(driver):
#     trial = 0
#     while(trial<3):
#         if is_element_present(driver, id_for_crash):
#             perform_click(driver, id_for_crash)    
#         time.sleep(3)
#         trial = trial + 1
#     driver.find_element("accessibility id", "Predicted app: Amazon").click()
#     time.sleep(15)  # Wait for the app to load

# def select_series(driver, series_name):
#     # Locate the MiniTV section and click on it
#     mini_tv_button = driver.find_element_by_accessibility_id("MiniTV")
#     mini_tv_button.click()
#     time.sleep(3)

#     # Find and click on the series
#     series = driver.find_element_by_xpath(f"//android.widget.TextView[@text='{series_name}']")
#     series.click()
#     time.sleep(3)

# def play_first_episode(driver):
#     seasons = driver.find_elements_by_id("season_list_id")  # Replace with actual ID
#     for season in seasons:
#         first_episode = season.find_element_by_xpath(".//android.widget.TextView[1]")
#         first_episode.click()
#         time.sleep(5)  # Wait for video to start playing
        
#         # Verify playback status (this may vary based on implementation)
#         assert driver.find_element_by_id("playback_status_id").is_displayed()  # Replace with actual ID

# def test_amazon_minitv():
#     driver = setup_driver()
    
#     try:
#         open_amazon_app(driver)
#         select_series(driver, "The Office")  # Change to your chosen series
#         play_first_episode(driver)
        
#         print("Test completed successfully.")
        
#     except Exception as e:
#         print(f"Test failed: {e}")
    
#     finally:
#         driver.quit()

# test_amazon_minitv()