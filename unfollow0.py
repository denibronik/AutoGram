import time
from datetime import datetime
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


login1="" #You need to enter your Instgram login here
pass1="" #You need to enter your Instgram password here


url="https://www.instagram.com/"+login1+"/following/"

browser = webdriver.Chrome()
browser.get(url)

browser.maximize_window()

wait = WebDriverWait(browser, 10)

second_page_flag = wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "KPnG0")))  # until login page appear

user = browser.find_element_by_name("username")
passw = browser.find_element_by_name('password')
ActionChains(browser)\
    .move_to_element(user).click()\
    .send_keys(login1)\
    .move_to_element(passw).click()\
    .send_keys(pass1)\
    .perform()
#Login Button
login_button_ = browser.find_element_by_xpath(
    "//form[@class='HmktE']")
login_button_.click()
time.sleep(5)

    
    
while True:
    print((datetime.now()).strftime("%d/%m/%Y %H:%M:%S"))
    browser.get(url)
    #Followers Button
    followers_button = browser.find_element_by_xpath("//ul[@class='k9GMp ']/li[3]/a")
    followers_button.click()
    #scroll
    pyautogui.moveTo(660, 430, 1)
    pyautogui.scroll(-500)
    time.sleep(2)
    pyautogui.scroll(-1000)
    time.sleep(2)
    pyautogui.scroll(-1000)
    time.sleep(2)
    pyautogui.scroll(2600)
    time.sleep(4)
    
    
    for i in range(1,20):
        print(i)
        x = "//div[@class='PZuss']/li["+str(i)+"]/div/div[2]/button"
        unfollow_button = browser.find_element_by_xpath(x)
        unfollow_button.click()
        time.sleep(3)
        confirm_unfollow = browser.find_element_by_xpath("//div[@class='piCib']/div[3]/button[1]")
        confirm_unfollow.click()
        time.sleep(2)
    #Close Followers
    close_button = browser.find_element_by_xpath("//div[@class='WaOAr']/button")
    close_button.click()
    time.sleep(3600)


#browser.close()