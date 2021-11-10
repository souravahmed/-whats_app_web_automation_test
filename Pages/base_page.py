class BasePage(object):
    """
    this Base class is serving basic attributes for every single page inherited from Page class
    
    """
    
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        
    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
     
         
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    
    def send_keys(self, element, text):
        element.send_keys(text)
          