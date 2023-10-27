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

def getFollowers(driver):
    try:
        driver.set_page_load_timeout(30)
        user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span")))
        user.click()

        followersBut = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")))
        followersNum = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span").text
        print(followersNum)

        followersBut.click()


        followersModal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_aano')))

        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", followersModal)
            time.sleep(1)
            elements = followersModal.find_elements(By.TAG_NAME, "div")

            # TODO Achar elemento correto para parar o codigo

            print("{}/{}".format(len(elements), followersNum))
            
            if len(elements) == int(followersNum):
                break


            #/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]
            #/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]

        #TODO Iterar pela lista de seguidores
        # depois iterar pelas divs do seguidor
        # até encontrar o span que contém o nome

        followersList = []

        # for item in followersModal:
        #     followersList.append(item)
        
        # for user in followersList:
        #     userName = WebDriverWait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div/div/span/span")))
        #     print(userName.text)

    except TimeoutException:
        print("Timeout")

    




def launch():

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")

    login(driver)
    getFollowers(driver)

    while(True):
        pass

launch()