import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


login1="" #You need to enter your Instgram login here
pass1="" #You need to enter your Instgram password here

acc = "apple" #You need to enter name of Instagram account whose followers you want to follow.
              #In this example,program will follow Apple followers.
url="https://www.instagram.com/"+acc+"/followers/"

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
#Login into account
login_button_ = browser.find_element_by_xpath(
    "//form[@class='HmktE']")
login_button_.click()
time.sleep(5)



while True:
    browser.get(url)
    #Show Followers
    followers_button = browser.find_element_by_xpath("//ul[@class='k9GMp ']/li[2]/a")
    followers_button.click()
    time.sleep(3)
    #Scroll
    pyautogui.moveTo(660, 430, 1)
    pyautogui.scroll(-500)
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(1)
    pyautogui.scroll(2600)
    time.sleep(3)
    
    i = 1
    while i <= 50:
        print(i)
        x = "//div[@class='PZuss']/li["+str(i)+"]/div/div[2]/button"
        y = "//div[@class='PZuss']/li["+str(i)+"]/div/div[1]/div[2]/div[1]"
        log_name = browser.find_element_by_xpath(y)
        follow_button = browser.find_element_by_xpath(x)
        check = follow_button.get_attribute("class")
        if(check == "sqdOP  L3NKy   y3zKF     "):
            follow_button.click()
            print(log_name.text)
            i+=1
        else:
            print("Skipped:"+log_name.text+"\n")
            continue
        time.sleep(3)
    #Close Followers
    close_button = browser.find_element_by_xpath("//div[@class='WaOAr']/button")
    close_button.click()
    time.sleep(3600)



browser.close()