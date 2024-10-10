import re
import time
import logging
from lib.input_data import *
from appium import webdriver
from lib.common_utils import CommonUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.options import ArgOptions
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class MiniTv(CommonUtils):
    def __init__(self, driver):
        self.driver = driver
        # settings = driver.get_settings()
        driver.update_settings({"allowInvisibleElements": True})
    
    def click_on_magnifier_icon(self):
        """
        Method to click magnifier icon
        """
        try:
            logger.info("Clicking on Magnifier icon")
            self.wait_and_perform_click_by_xpath(xpath_for_magnifier_icon)
        except Exception as e:
            logger.error("Failed to click_on_magnifier_icon due to: " + repr(e))
            raise
    
    def send_text_to_search_box(self, name=series_name):
        """
        Method to send text to search box.
        :param name: Series name
        """
        try:
            logger.info(f"Entering: {name}")
            self.wait_and_perform_click_by_xpath(xpath_for_search_box)
            self.send_text_by_xpath(xpath_for_search_box, name)
            time.sleep(WAIT_FOR_3_SEC)
        except Exception as e:
            logger.error("Failed to send_text_to_search_box due to: " + repr(e))
            raise

    def select_and_open_series_details(self):
        """
        Method to select the series from the dropdown and fetch the details
        """
        try:
            self.click_on_magnifier_icon()
            self.send_text_to_search_box()
            logger.info("Select first row")
            self.wait_and_perform_click_by_xpath(xpath_for_highway_series, WAIT_FOR_7_SEC)
            logger.info("Selecting series again")
            self.wait_and_perform_click_by_xpath(xpath_for_searched_series, WAIT_FOR_7_SEC)
            logger.info("Expanding list of availble seasons by icon")
            self.wait_and_perform_click_by_xpath(xpath_for_series_expand, WAIT_FOR_7_SEC)
            logger.info("Get Total Series details")
            self.wait_and_perform_click_by_xpath(xpath_for_series_expand, WAIT_FOR_7_SEC)
            self.total_series = self.get_texts(xpath_for_seasons)
            logger.info("Total number of availble seasons: "+ str(len(self.total_series)))
            self.sleep_before_next_click(WAIT_FOR_3_SEC)
            logger.info("Checking if the season page is reached")
            assert len(self.total_series) > 0, "Failed, to open series"
            return self.total_series
        except Exception as e:
            logger.error("Failed to select_and_open_series_details due to: " + repr(e))
            raise
    
    def play_first_episodes(self):
        try:
            self.total_series = sorted(self.total_series)
            for season in self.total_series:
                logger.info(f"=================== {season} ==================")
                logger.info("Expanding the series dropdown")
                self.wait_and_perform_click_by_xpath(xpath_for_series_expand2, WAIT_FOR_7_SEC)
                logger.info(f"Selecting {season} from the dropdown.")
                self.wait_and_perform_click_by_xpath(xpath_for_season(season), WAIT_FOR_7_SEC)
                self.sleep_before_next_click(WAIT_FOR_3_SEC)
                logger.info(f"Reading list of episodes in {season}")
                self.episodes = self.get_texts(xpath_for_all_episode_element)
                logger.info("Applying regex")
                episodes_list = re.findall(r'E\d+', self.episodes[0])
                logger.info(f"{season} has {str(len(episodes_list))}")
                logger.info(f"Playing Episode 1 of {season} successfully")
                logger.info("Checking if episodes are available")
                assert len(episodes_list) > 0, f"Failed, to fetch episodes of {season}"
        except Exception as e:
            logger.error("Failed to play_first_episodes due to: " + repr(e))
            raise