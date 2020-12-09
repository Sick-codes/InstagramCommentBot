from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from random import randrange
import random
from time import sleep

class Bot:
    def __init__(self):
    	self.comm1 = (input("Comment 1: "))
		self.comm2 = (input("Comment 2: "))
		self.comm3 = (input("Comment 3: "))

		print("Welcoime to ehouse's Instagram Spammer")
		self.link = (input("Link to photo: "))
		self.numOfComm = (int(input("Number of comments: ")))

		print("Starting chrome...")
		self.options = Options()
		self.options.add_argument("--headless")
		self.driver = webdriver.Chrome(options=options)

    
    def randComm():
        comms = [self.comm1, self.comm2, self.comm3]
        comm = random.choice(comms)
        if comm == '':
            self.randComm()
        else:
            spam()

    def spam():
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys("yourPW")
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys("yourUN")
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        self.driver.get(self.link)
        sleep(1)
        for i in range(self.numOfComm):
            randSleep = randrange(30,90)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[2]/button').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/form/textarea').send_keys(self.comm)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[3]/div/form/button').click()
            sleep(randSleep)
            randSleep = 0

if __name__ == '__main__':
	myBot = Bot()
