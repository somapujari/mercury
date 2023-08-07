import time

from pageobject.register import Register
from utility.readconfig import Readconfig


class Test_register:
    base_url = Readconfig.get_url()

    def test_register(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.re = Register(self.driver)
        self.re.click_register_link()
        self.re.first_name_enter('soma')
        self.re.last_name_enter('pujari')
        self.re.phone_enter('8888953661')
        self.re.email_enter('ss@gmail.com')
        self.re.address_enter('mumbai')
        self.re.city_enter('mumbai')
        self.re.state_enter('maharashtra')
        self.re.post_enter('pune')
        self.re.select_country('INDIA')
        self.re.username_enter('soma')
        self.re.password_enter('soma123')
        self.re.conform_password('soma123')
        self.re.submit_click()
        self.re.verify_register()
        time.sleep(5)
