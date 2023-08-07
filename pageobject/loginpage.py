from selenium.webdriver.common.by import By


class LoginPage:
    username_inp_name = (By.NAME, 'userName')
    password_inp_name = (By.NAME, 'password')
    login_btn_name = (By.NAME, 'submit')
    verify_text_xpath = (By.XPATH, '//html//body')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.username_inp_name).clear()
        self.driver.find_element(*LoginPage.username_inp_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.password_inp_name).clear()
        self.driver.find_element(*LoginPage.password_inp_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.login_btn_name).click()

    def verify_login(self):
        contain = self.driver.find_element(*LoginPage.verify_text_xpath).text
        if 'Thank you for Loggin.' in contain:
            assert True
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\mercury\screenshots\login_pass.png')
        else:
            self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\mercury\screenshots\login_fail.png')
            assert False

