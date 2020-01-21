from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#import pyautogui as pag
import time

driver = webdriver.Firefox('') #PATH of webdriver

def conectar(paginaInicial, paginaFinal):
    conectar = 0
    for i in range(paginaInicial, paginaFinal +1):
        time.sleep(1)
        driver.get("https://www.linkedin.com/search/results/people/?facetIndustry=%5B%22102%22%5D&facetNetwork=%5B%22S%22%5D&origin=FACETED_SEARCH&page="+str(i)) # here you should place the url of a 'specific work area.
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        conectButtons = driver.find_elements_by_xpath("//button[@class='search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary']")
        for button in conectButtons:
            time.sleep(1)
            if button.text == 'Connect':
                print(button.text)
                button.click()
                time.sleep(1)       
                driver.find_element_by_xpath("//button[@class='ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
                print('Invite sent')
                conectar = conectar + 1
            else:
                continue
        print(f'Page {i} done')
    print(f'{conectar} invites were sent')


def login(username, password):
    username = driver.find_element_by_id('username')
    username.send_keys(username)
    password = driver.find_element_by_id('password')
    password.send_keys(password)
    time.sleep(1)
    login = driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']")
    login.click()
    print('Logged in successfully')
    

def main():
    url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    print('Started Linkedin Script')
    driver.get(url)
    time.sleep(3)
    login('username', 'password')
    time.sleep(2)
    conectar(2,7)
    print('Script Linkedin done!')


if __name__ == "__main__":
    main()
