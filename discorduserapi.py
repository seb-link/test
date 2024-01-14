
from selenium import webdriver
from myby import by
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DiscordUserAPI:
    
    def __init__(self, headless: bool = True) -> None:
        
        options = Options()
        if headless:
            options.add_argument("headless")
        else:
            options.add_argument("start-maximized")

        self.driver = webdriver.Edge(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, mail: str, password: str):
        self.driver.get("https://discord.com/login")
        self.wait.until(EC.visibility_of_element_located((by.id, 'uid_5')))
        
        username_input = self.driver.find_element(by.id, 'uid_5')
        password_input = self.driver.find_element(by.id, 'uid_7')

        username_input.send_keys(mail)
        password_input.send_keys(password)
        