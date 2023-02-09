#instagram user bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class Instagram:
    
    def login(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.passaword = password

    def singIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        #usenameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        usenameInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        #passwordInput = self.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        usenameInput.send_keys(self.username)
        passwordInput.send_keys(self.passaword)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_jY']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        followers = self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul").find_elements(By.CSS_SELECTOR,"li")

        for user in followers:
            link = user.find_element(By.CSS_SELECTOR ,"a").get_attribute("href")
            print(link)

username = "your username"
password = "your  password"
instagram = Instagram()

instagram.login(username,password)
instagram.singIn()
instagram.getFollowers()

