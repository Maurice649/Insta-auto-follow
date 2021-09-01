from selenium import webdriver 
from time import sleep
from selenium.webdriver.support.ui import Select
import warnings

class Instabot:
    def __init__(self):
        warnings.filterwarnings("ignore")
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://instagram.com")
        #log in
        sleep(1.2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(input("username or email:"))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(input("password:"))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        sleep(7)
        try:
            elem = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/button[2]")
            if elem.is_displayed:
                elem.click()
                sleep(3)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button").click()
                sleep(3)
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()
                sleep(1.5)
         #on wayy to follow people
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
                sleep(5)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[2]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[3]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[4]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[5]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[6]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[7]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[8]/div[3]/button").click()
                sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[9]/div[3]/button").click()
                sleep(2.5)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[10]/div[3]/button").click()
        

        except:
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/section/div/button").click()
         sleep(3)
         self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()
         sleep(1.5)
         #on wayy to follow people
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div").click()
         sleep(5)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[1]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[2]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[3]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[4]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[5]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[6]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[7]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[8]/div[3]/button").click()
         sleep(2)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[9]/div[3]/button").click()
         sleep(2.5)
         self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[10]/div[3]/button").click()
        

Instabot()


