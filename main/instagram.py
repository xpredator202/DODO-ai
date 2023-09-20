from selenium import webdriver
from selenium.webdriver.common.by import By

def instagram_message():
    browser = webdriver.Chrome(r"C:\\Users\\Manav sharma\\sparsh\\.vscode\\main\\chromedriver_win32\\chromedriver.exe")
    browser.get("https://www.instagram.com/")
