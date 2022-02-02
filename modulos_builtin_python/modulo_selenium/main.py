from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_login(self):
        try:

            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.NAME, 'commit')

            input_login.send_keys('colvalan@hotmail.com')
            input_password.send_keys('kilder410')
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)

    def faz_logout(self):
        try:
            logout = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            logout.click()
        except Exception as e:
            print('Erro ao clicar em Sign Out:', e)

    def verifica_usuario(self, usuario):
        profile_link_html = self.chrome.find_element(By.CLASS_NAME, 'user-profile-link')
        profile_link_html = profile_link_html.get_attribute('innerHTML')
        print(profile_link_html)
        assert usuario in profile_link_html


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('http://github.com/')
    chrome.clica_sign_in()
    chrome.faz_login()
    chrome.clica_perfil()
    sleep(1)
    chrome.verifica_usuario('Colvalan')
    sleep(10)
    chrome.faz_logout()
    sleep(30)
    chrome.sair()
