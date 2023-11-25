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
    password.send_keys('D9m5a2003')

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


        # Aguardar até que a div "aano" seja carregada (ajuste o seletor conforme necessário)
        divAano = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_aano')))

        # Encontrar a div "A" dentro da div "aano"
        divA = divAano.find_element(By.XPATH, "./div")

        # Inicializar a quantidade inicial de divsB
        divsB_anterior = len(divA.find_elements(By.XPATH, "./div"))

        print(f"A quantidade de divs dentro da div B é: {divsB_anterior}")

        i=1

        users=[]
        #users.extend(divA.find_elements(By.XPATH, "./div"))
        stringOr = ''
        while len(users) <= int(followersNum):
            # Rolar até o final da página
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", divA)

            # Aguardar um curto período de tempo para dar tempo às novas divs de carregarem
            driver.implicitly_wait(2)

            #users.extend(divA.find_elements(By.XPATH, "./div"))
            string = divA.find_elements(By.XPATH, "./div")
            
            if stringOr == string:
                break

            stringOr = string

            #elementText = element.text.split('\n')[0]

            #users.extend(elementText)
            
            i += 1

        print(stringOr)
        
        print(f"A quantidade de users  é: {int(followersNum)}")
        

        stringOr = stringOr[0].text.split('\n')

        print(stringOr)



        list = eval(stringOr)

        usernames = []

        #user = list[0] lookasnard
        #remover = list[1] Remover
        #user = list[2] oa.ganja.tele
        #ponto = list[3] .
        #seguir = list[4] Seguir
        #user = list[5] porto alegre ganja delivery

        usernames.extend(list[0])

        




        for user in users:
            print(user.text.split('\n')[0])
            usernames.append(user.text.split('\n')[0])

        for username in usernames:
            print(username)
        

        
    
        # i = 1
        # users = []

        # while len(users) <= int(followersNum):
            
        #     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll)
        #     time.sleep(1)

        #     user = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{}]".format(i))))
        #     # TODO Achar elemento correto para parar o codigo
          
        #     users.extend(user)

        #     print("{}/{}".format(len(users), followersNum))
            
        #     i += 1

        # for user in users:
        #     print(user.text.split('\n')[0])

        # close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x1lliihq x1n2onr6 x5n08af")))
        # close.click()

        # return users

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
    getFollowers(driver)
    #getFollowing(driver)

    while(True):
        pass

launch()