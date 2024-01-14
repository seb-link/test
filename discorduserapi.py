from click import pass_context
from selenium import webdriver
from myby import by
from selenium.webdriver.edge.options import Options

class DiscordUserAPI:
    
    def __init__(self, headless: bool = True) -> None:
        
        options = Options()
        if headless:
            options.add_argument("headless")
        else:
            options.add_argument("start-maximized")

        self.driver = webdriver.Edge(options=options)

    def login(self, mail: str, password: str):
        self.driver.get("https://discord.com/login")
        username_input = self.driver.find_element(by.id, 'uid_5')
        password_input = self.driver.find_element(by.id, 'uid_7')

        username_input.send_keys(mail)
        password_input.send_keys(password)
        