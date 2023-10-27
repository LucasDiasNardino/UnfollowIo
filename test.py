from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time


def login(driver):
    login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")))
    login.click()
    login.send_keys('lucas__nardino')

    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")))
    password.click()
    #passwEntry = str(input("Enter your password: "))
    password.send_keys('d9m5a2003')

    ok = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]")))
    ok.click()

    notNow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")))
    notNow.click()

    notNow2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
    notNow2.click()

    user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span")))
    user.click()

def getFollowers(driver):
    try:
        driver.set_page_load_timeout(30)
        

        followersBut = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")))
        followersNum = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span").text
        print(followersNum)

        followersBut.click()


        scroll = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_aano')))
    
        i = 1
        users = []

        while len(users) <= int(followersNum):
            
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll)
            time.sleep(1)

            user = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{}]".format(i))))
            # TODO Achar elemento correto para parar o codigo
          
            users.extend(user)

            print("{}/{}".format(len(users), followersNum))
            
            i += 1

        for user in users:
            print(user.text.split('\n')[0])

        close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x1lliihq x1n2onr6 x5n08af")))
        close.click()

        return users

    except TimeoutException:
        print("Timeout")

def getFollowing(driver):
    try:

        driver.set_page_load_timeout(30)


        followingBut = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span")))
        followingNum = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span").text
        print(followingNum)

        followingBut.click()


        scroll = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_aano')))
    
        i = 1
        j = 4
        users = []

        while len(users) <= 4:
            
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll)
            time.sleep(1)

            user = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[{j}]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{}]".format(j,i))))
            # TODO Achar elemento correto para parar o codigo

            #/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[1]
            #/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[2]

            users.extend(user)

            print("{}/{}".format(len(users), followingNum))
            
            i += 1
            j += 1

        for user in users:
            print(user.text.split('\n')[0])

        return users

    except TimeoutException:
        print("Timeout")

def launch():

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")

    login(driver)
    #getFollowers(driver)
    getFollowing(driver)

    while(True):
        pass

launch()