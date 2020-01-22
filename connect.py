from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from getpass import getpass
from getpass import getuser
import time


def like():
    for i in range(0,3):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    botoes = driver.find_elements_by_xpath("//button[@class='react-button__trigger artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view']")
    
    for botao in botoes:
        botao.click()
        time.sleep(5)
        print('Publicação curtida')

def conectar(paginaInicial, paginaFinal):
    conectar = 0
    for i in range(paginaInicial, paginaFinal +1):
        time.sleep(1)
        driver.get("https://www.linkedin.com/search/results/people/?facetGeoRegion=[%22au%3A0%22%2C%22br%3A6034%22%2C%22br%3A6368%22%2C%22us%3A0%22]&facetIndustry=[%22102%22]&facetNetwork=[%22S%22]&origin=FACETED_SEARCH&page="+str(i))
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        conectButtons = driver.find_elements_by_xpath("//button[@class='search-result__action-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary']")
        for button in conectButtons:
            time.sleep(1)
            if button.text == 'Conectar':
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


def login():
    username = driver.find_element_by_id('username')
    username.send_keys(username_text)
    password = driver.find_element_by_id('password')
    password.send_keys(password_text)
    time.sleep(1)
    login = driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']")
    login.click()
    print('Logged in successfully')
    

def main():
    global username_text, password_text, driver
    print('Started Linkedin Script')
    username_text = input('Digite seu e-mail: ')
    password_text = getpass()
    print('Choose a specific script bellow: ')
    print('1 - Auto-Like \n2 - Auto-Connect \n3 - Both\n')
    option = input('Your choice: ')
    while option not in ['1', '2', '3']:
        option = input('You didnt choose a valid option, please, try again: ')
    driver = webdriver.Firefox('C:\\Users\\b8m7\\Desktop\\linkedinBot')
    url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
    driver.get(url)
    time.sleep(3)
    login()
    time.sleep(2)
    if option == '2':
        conectar(1,7)
    elif option == '1':
        like()
    elif option == '3':
        like()
        conectar(1,2)
    else:
        print('Não existe esta opção!')
    print('Script Linkedin done!')


if __name__ == "__main__":
    main()
