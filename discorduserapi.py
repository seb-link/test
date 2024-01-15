
import time
from selenium import webdriver
from myby import by
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
        validate_button = self.driver.find_element(by.xpath, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]')

        username_input.send_keys(mail)
        password_input.send_keys(password)
        validate_button.click()

        while not "app" in self.driver.current_url:
            pass

    def send_dm(self, id_recv: str, msg_to_send: str):

        self.wait.until(EC.visibility_of_element_located((by.xpath, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/nav/div[2]/ul/li[1]/div/a/div/div[2]/div/div')))

        time.sleep(2)
        # Récupérer tous les éléments <a>
        elements_a = self.driver.find_elements(by.class_name, 'link__2e8e1')

        # Parcourir tous les éléments <a> et cliquer sur celui avec href égal à "/salut"
        for a in elements_a:
            if id_recv in a.get_attribute("href"):
                a.click()
                break
        
        self.wait.until(EC.visibility_of_element_located((by.xpath, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/form/div/div/div/div[3]/div/div[2]')))
        msg_input = self.driver.find_element(by.xpath, '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/form/div/div/div/div[3]/div/div[2]')
        msg_input.send_keys(msg_to_send)
        msg_input.send_keys(Keys.ENTER)

        self.driver.get("https://discord.com/channels/@me")
        
    
    def send_channel(self, id_serv: str, id_channel: str, msg_to_send: str):
        self.driver.get(f"https://discord.com/channels/{id_serv}/{id_channel}")

        self.wait.until(EC.visibility_of_element_located((by.css_selector, '.markup_a7e664.editor__66464.slateTextArea__0661c.fontSize16Padding__48818')))
        msg_input = self.driver.find_element(by.css_selector, '.markup_a7e664.editor__66464.slateTextArea__0661c.fontSize16Padding__48818')
        msg_input.send_keys(msg_to_send)
        msg_input.send_keys(Keys.ENTER)

        self.driver.get("https://discord.com/channels/@me")