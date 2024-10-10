import time
import logging
from lib.input_data import *
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# logger = logging.getLogger()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class CommonUtils:

    def initialize_parameter(self):
        logger.info("====== INITIALIZING PARAMETER =====")
        self.driver = None
        options = ArgOptions()
        options.platform_name = "Android"
        options.device_name = "Android Emulator"
        options.app_package = "com.google.android.apps.nexuslauncher"
        options.app_activity = "com.google.android.apps.nexuslauncher.NexusLauncherActivity"
        logger.info("Initialising driver")
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
        logger.info("Driver Obj: " + str(self.driver))
        logger.info("Initialising driver successful")
        logger.info("====================================")
        return self.driver
    
    def wait_and_click_by_accessibility_id(self, a_id, w_time=10):
        """
        Method to perform click by accessibility id
        """
        try:
            logger.info(f"Explicit waiting for {w_time} by accessibility id")
            wait = WebDriverWait(self.driver, w_time)
            element = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, a_id)))
            self.driver.find_element(By.ACCESSIBILITY_ID, a_id).click()
            return True
        except:
            logger.info("Element not present. Returned False")
            return False
    
    def wait_for_element_by_id(self, id, w_time=20):
        """
        Method to wait for element to be present
        :param id: ID
        :param w_time: Wait time. Default wait time is 20 seconds
        """
        try:
            logger.info(f"Explicit waiting for {w_time} by id")
            wait = WebDriverWait(self.driver, w_time)
            element = wait.until(EC.presence_of_element_located((By.ID, id)))
            return True
        except Exception as e:
            logger.error("Failed due to attribute error : " + repr(e))
            raise
    
    def wait_for_element_by_xpath(self, xpath, w_time=20):
        """
        Method to wait for element to be present by xpath
        :param xpath: xpath
        :param w_time: Wait time. Default wait time is 20 seconds
        """
        try:
            logger.info(f"Explicit waiting for {w_time} by xpath")
            wait = WebDriverWait(self.driver, w_time)  
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        except Exception as e:
            logger.error("Failed, wait_for_element_by_xpath : " + repr(e))
            raise

    def send_text_by_xpath(self, xpath, text, w_time=10):
        """
        Method to send text by xpath
        """
        try:
            logger.info(f"Explicit waiting for {w_time} before sending text")
            wait = WebDriverWait(self.driver, w_time)
            input_element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            input_element.clear()
            logger.info("Sending text to the input field")
            input_element.send_keys(text)
        except Exception as e:
            logger.error("Failed, send_text_by_xpath : " + repr(e))
            raise
    
    def perform_click_by_action_chains(self, x_loc, y_loc):
        """
        Method to perform click using location.
        """
        try:
            logger.info("Performing click using action chains.")
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(x_loc, y_loc)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(x_loc, y_loc)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        except Exception as e:
            logger.error("Failed to perform_click_by_action_chains"+ repr(e))
            raise
    
    def sleep_before_next_click(self, wait_time):
        """
        Method to sleep
        """
        try:
            logger.info(f"Sleeping for {wait_time} sec.")
            time.sleep(wait_time)
        except Exception as e:
            logger.error("Failed to sleep_before_next_click "+ repr(e))
            raise
    
    def wait_and_perform_click_by_id(self, id, w_time=20):
        """
        Method to wait and perform click on element by id
        """
        try:
            self.wait_for_element_by_id(id, w_time)
            logger.info(f"Performing click using id")
            self.driver.find_element(By.ID, id).click()
        except Exception as e:
            logger.error("Failed to wait_and_perform_click_by_id "+ repr(e))
            raise
    
    def wait_and_perform_click_by_xpath(self, xpath, w_time=20):
        """
        Method to wait and perform click on element by xpath
        """
        try:
            self.wait_for_element_by_xpath(xpath, w_time)
            logger.info(f"Performing click using xpath")
            self.driver.find_element(By.XPATH, xpath).click()
            self.sleep_before_next_click(WAIT_FOR_2_SEC)
        except Exception as e:
            logger.error("Failed to wait_and_perform_click_by_xpath "+ repr(e))
            raise
    
    def is_element_present_by_id(self, id):
        """
        Method to return True if the element is visible
        """
        try:
            logger.info("Checking if the element is present by id")
            self.driver.find_element(By.ID, id).click()
            logger.info("Element present. Returned True")
            return True
        except:
            logger.info("Element not present. Returned False")
            return False

    def is_element_present_by_xpath(self, xpath):
        """
        Method to return True if the element is visible by xpath
        """
        try:
            logger.info("Checking if the element is present by xpath")
            return self.driver.find_element(By.XPATH, xpath).is_displayed()
        except:
            logger.info("Element not present. Returned False")
            return False

    def launch_amazon_app(self):
        try:
            logger.info("Launching the Amazon app")
            self.wait_and_click_by_accessibility_id(a_id_for_amazon_app, WAIT_FOR_7_SEC)
            self.sleep_before_next_click(WAIT_FOR_25_SEC)
            logger.info("Checking the presence of home icon after launching")
            logger.info( self.is_element_present_by_xpath(xpath_for_home_icon))
            assert self.is_element_present_by_xpath(xpath_for_home_icon), "Failed. To open amazon app"
        except AttributeError:
            logger.error("Failed due to attribute error")
            raise
        except Exception as e:
            logger.error("Failed due to attribute error : " + repr(e))
            raise

    def navigate_to_mini_tv(self):
        """
        Method to naviagate to mini tv
        """
        try:
            logger.info("Navigating to the Mini Tv app")
            self.wait_and_perform_click_by_xpath(xpath_for_mx_player, WAIT_FOR_7_SEC)
            self.sleep_before_next_click(WAIT_FOR_10_SEC)
            logger.info("Checking navigation to Mini TV")
            assert self.is_element_present_by_xpath(xpath_for_magnifier_icon), "Failed. To open navigate to Mini Tv app"
        except Exception as e:
            logger.error("Failed due to attribute error : " + repr(e))
            raise
    
    def get_text(self, xpath):
        """
        Method for getting text
        """
        try:
            logger.info("Getting associated texts")
            self.wait_for_element_by_xpath(xpath)
            logger.info("Searching element using xpath")
            elements = self.driver.find_element(By.XPATH, xpath)
            text = [ele.text for ele in elements]
            logger.info("Text found: " + str(text))
            return text
        except Exception as e:
            logger.error("Failed to get_text : " + repr(e))
            raise
    
    def get_texts(self, xpath):
        """
        Method for getting texts
        """
        try:
            logger.info("Getting associated texts")
            self.wait_for_element_by_xpath(xpath)
            logger.info("Searching element using xpath")
            elements = self.driver.find_elements(By.XPATH, xpath)
            texts = [ele.text for ele in elements]
            logger.info("Texts found: " + str(texts))
            return texts
        except Exception as e:
            logger.error("Failed to get_texts : " + repr(e))
            raise
    
    def handle_crash(self, trial=3, id=id_for_crash):
        """
        Method to handle crash.
        :param id_for_crash: ID for crash
        :param trail: No. of trial
        """
        try:
            trial = 0
            while(trial<3):
                if self.is_element_present_by_id(id_for_crash):
                    self.wait_and_perform_click_by_id(id_for_crash, WAIT_FOR_10_SEC)    
                self.sleep_before_next_click(WAIT_FOR_3_SEC)
                trial = trial + 1
        except Exception as e:
            logger.error("Failed to handle_crash : " + repr(e))
            raise
        