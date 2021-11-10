from selenium.webdriver.common.by import By

class HomePageLocators(object):
    
    SEARCH_BOX = (By.CSS_SELECTOR, '#side > div.uwk68 > div > label > div > div._13NKt.copyable-text.selectable-text')
    SEARCH_RESULT = (By.CLASS_NAME, '_3q9s6')
    MESSAGE_TEXT_BOX = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    MESSAGE = (By.CSS_SELECTOR, '._2F01v > span')
    OPTION = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/div')
    LOG_OUT_OPTION = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]')