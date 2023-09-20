from selenium import webdriver
from selenium.webdriver.common.by import By
import config
import os
from time import sleep
option = webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome(r'C:/Users/Manav sharma/sparsh/.vscode/main/chromedriver.exe')
driver.maximize_window()
url= 'https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F'
driver.get(url)




def login(Email,Password):
    driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys(Email)
    driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(Password)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[3]/div[2]/button/div[1]/span').click()
    

def download():
    str1 ="spotdl"
    str2 =driver.current_url
    str = str1+str2
    os.system(str)
    print("downloading")

def playlist():
    driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/button[2]/svg').click()
    driver.find_element(By.XPATH,'/html/body/div[14]/div/ul/li[5]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[14]/div/ul/li[5]/div/ul/div/li[6]/button/span').click()


login(config.username,config.password)
sleep(3)
driver.get("https://open.spotify.com/track/5jpWl5m5SYXm7lBjGPaY7n")
#download()
playlist()
sleep(15)
driver.close()