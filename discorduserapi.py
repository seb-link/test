from selenium import webdriver
from myby import by
from selenium.webdriver.edge.options import Options

class DiscordAPI:
    
    def __init__(self, headless: bool = True) -> None:
        
        options = Options()
        if headless:
            options.add_argument("headless")
        else:
            options.add_argument("start-maximized")

        self.driver = webdriver.Edge(options=options)

    def login(self, userame: str, password: str):
        self.driver.get("https://discord.com/login")
        