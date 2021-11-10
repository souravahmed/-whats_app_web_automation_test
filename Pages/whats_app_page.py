from Pages.base_page import BasePage
from Pages.config import ConstData
from utils import locators
from utils.message import MessageUtil
from utils.reader import ExcelUtil
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


class HomePage(BasePage):
    
    def __init__(self, driver):
        self.locators = locators.HomePageLocators
        super().__init__(driver, ConstData.BASE_URL)
    
    def search_number(self):
        self.open(ConstData.BASE_URL)
        print("please scan QR code you will have 10 sec")
        time.sleep(10)
        
        ExcelUtil.open()
        mobile_number = ExcelUtil.get_mobile_number()
        search_box = self.find_element(*self.locators.SEARCH_BOX)
        self.send_keys(search_box, mobile_number)
        time.sleep(10)
        
        return self.find_element(*self.locators.SEARCH_RESULT)
    
    
    def send_message(self):
        search_result = self.search_number()
        search_result.click()
        time.sleep(5)
        message_box = self.find_element(*self.locators.MESSAGE_TEXT_BOX)
        self.send_keys(message_box, MessageUtil.message["greeting"])
        self.send_keys(message_box, Keys.ENTER)
        time.sleep(10)
        
        return message_box
    
    
    def send_message_and_write_sent_message_in_excel(self):
        self.send_message()
        try:
            
            ExcelUtil.open()
            ExcelUtil.write_message(2,2, MessageUtil.excel_message["sent"])
            return True
            
        except Exception:
            return False    
        
    
    def send_message_and_write_status(self):
        self.send_message()
        
        try:
            ExcelUtil.open()
            value = self.find_element(*self.locators.MESSAGE).get_attribute('aria-label')
            print(value)
            
            if value == 'Read':
                ExcelUtil.write_message(2, 3, MessageUtil.excel_message["seen"])
                return True
            
            ExcelUtil.write_message(2, 3, MessageUtil.excel_message["not_seen"])
            return True
        
        except Exception:
            return False        
    
    
    def log_out(self):
        
        self.search_number()
        option_element = self.find_element(*self.locators.OPTION)
        option_element.click()
        log_out_element = self.find_element(*self.locators.LOG_OUT_OPTION)
        log_out_element.click()
        time.sleep(5)
        
        try:
            
            search_element = self.find_element(*self.locators.SEARCH_RESULT)
            return False # if search box element is found then log out faild
        
        except NoSuchElementException:
            return True
      
        
        