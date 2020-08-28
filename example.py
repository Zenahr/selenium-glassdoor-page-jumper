from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GlassdoorBot():
    def __init__(self):
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)


    def init(self):
        self.driver.get("https://www.glassdoor.ca/Job/waterloo-python-jobs-SRCH_IL.0,8_IC2280158_KO9,15_IP4.htm?radius=12")

    def goto_next_page(self):
        """get button and click it"""
        next_page_button = self.driver.find_element_by_xpath('//*[@id="FooterPageNav"]/div/ul/li[6]')
        if next_page_button:
            print("Next Page Button Found!") # DEBUG LOG
            self.driver.execute_script("arguments[0].click();", next_page_button)

def runtime():
    bot = GlassdoorBot()
    bot.driver.get("https://www.glassdoor.ca/Job/waterloo-python-jobs-SRCH_IL.0,8_IC2280158_KO9,15_IP4.htm?radius=12")

