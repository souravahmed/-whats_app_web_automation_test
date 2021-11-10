import pytest
from Pages.whats_app_page import HomePage
from Tests.base_test import BaseTest



class Test_Home_page(BaseTest):
    

    def test_tc_00_1(self):
        home_page = HomePage(self.driver)
        search_result = home_page.search_number()
        assert True if search_result else False
        
        
    def test_tc_00_2(self):
        home_page = HomePage(self.driver)
        message_box = home_page.send_message()
        assert True if message_box else False
    
    def test_tc_00_3(self):
        home_page = HomePage(self.driver)
        is_message_written = home_page.send_message_and_write_sent_message_in_excel()
        assert is_message_written
        
    
    
    def test_tc_00_4(self):
        home_page = HomePage(self.driver)
        is_message_status_written = home_page.send_message_and_write_status()
        assert is_message_status_written
    
    def test_tc_005(self):
         home_page = HomePage(self.driver)
         is_loged_out = home_page.log_out()
         assert is_loged_out
            
        
               