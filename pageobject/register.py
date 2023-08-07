from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Register:
    register_link_link_text = (By.XPATH, '//a[@href="register.php"]//parent::td')
    first_name_inp_xpath = (By.XPATH, "//input[@name='firstName']")
    last_name_inp_xpath = (By.XPATH, "//input[@name='lastName']")
    phone_inp_xpath = (By.XPATH, "//input[@name='phone']")
    email_inp_xpath = (By.XPATH, "//input[@id='userName']")
    address_inp_xpath = (By.XPATH, "//input[@name='address1']")
    city_inp_xpath = (By.XPATH, "//input[@name='city']")
    state_inp_Xpath = (By.XPATH, "//input[@name='state']")
    post_inp_xpath = (By.XPATH, "//input[@name='postalCode']")
    country_inp_xpath = (By.XPATH, "//select[@name='country']")
    username_inp_xpath = (By.XPATH, "//input[@id='email']")
    password_inp_xpath = (By.XPATH, "//input[@name='password']")
    conform_pass_inp_xpath = (By.XPATH, "//input[@name='confirmPassword']")
    register_verify_inp_xpath = (By.XPATH, '//html//body')

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        self.driver.find_element(*Register.register_link_link_text).click()

    def first_name_enter(self, first_name):
        self.driver.find_element(*Register.first_name_inp_xpath).clear()
        self.driver.find_element(*Register.first_name_inp_xpath).send_keys(first_name)

    def last_name_enter(self, last_name):
        self.driver.find_element(*Register.last_name_inp_xpath).clear()
        self.driver.find_element(*Register.last_name_inp_xpath).send_keys(last_name)

    def phone_enter(self, phone):
        self.driver.find_element(*Register.phone_inp_xpath).clear()
        self.driver.find_element(*Register.phone_inp_xpath).send_keys(phone)

    def email_enter(self, email):
        self.driver.find_element(*Register.email_inp_xpath).send_keys(email)

    def address_enter(self, address):
        self.driver.find_element(*Register.address_inp_xpath).send_keys(address)

    def city_enter(self, city):
        self.driver.find_element(*Register.city_inp_xpath).send_keys(city)

    def state_enter(self, post):
        self.driver.find_element(*Register.state_inp_Xpath).send_keys(post)

    def post_enter(self, post):
        self.driver.find_element(*Register.post_inp_xpath).send_keys(post)

    def select_country(self, country):
        ele = self.driver.find_element(*Register.country_inp_xpath)
        drop = Select(ele)
        drop.select_by_visible_text(country)

    def username_enter(self, username):
        self.driver.find_element(*Register.username_inp_xpath).send_keys(username)

    def password_enter(self, password):
        self.driver.find_element(*Register.password_inp_xpath).send_keys(password)

    def conform_password(self, password):
        self.driver.find_element(*Register.conform_pass_inp_xpath).send_keys(password)

    def submit_click(self):
        self.driver.find_element(By.XPATH, "//input[@name='submit']").click()

    def verify_register(self):
        bodycontain = self.driver.find_element(*Register.register_verify_inp_xpath).text
        assert 'Thank you for registering' in bodycontain
        self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\mercury\screenshots\register_pass.png')

