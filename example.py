from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class GlassdoorBot():
    def __init__(self):
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)


    def init(self):
        self.driver.get("https://www.glassdoor.ca/Job/waterloo-python-jobs-SRCH_IL.0,8_IC2280158_KO9,15.htm?radius=12")

    def goto_next_page(self):
        """get button and click it"""
        next_page_button = self.driver.find_element_by_xpath('//*[@id="FooterPageNav"]/div/ul/li[5]/a')
        if next_page_button:
            sleep(5) # Don't use this in production. Use selenium Wait instead.
            print("Next Page Button Found!") # DEBUG LOG
            self.driver.execute_script("arguments[0].click();", next_page_button) # Can't use regular click() since there is no easy way to scroll the element into view
            print("Clicked on next page button")

    def modal_handler(self):
        modal = self.driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]')
        if modal:
            print("Modal Appeared!")
            close_modal_button = self.driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/span')
            close_modal_button.click()
            print("Closed modal.")
    
    def run(self):
        self.init()
        while True:
                try:
                    self.modal_handler()
                except Exception:
                    self.goto_next_page()

def run():
    bot = GlassdoorBot()
    bot.run()

    
