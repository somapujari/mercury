from pageobject.loginpage import LoginPage
from utility.logcreation import LogGen


class Test_Login:
    base_url = 'https://demo.guru99.com/test/newtours/'
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info('test_login started')
        self.driver = setup
        self.logger.info('openting url')
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lg = LoginPage(self.driver)
        self.logger.info('enter username')
        self.lg.enter_username('mercury')
        self.logger.info('enter password')
        self.lg.enter_password('mercury')
        self.logger.info('click on login ')
        self.lg.click_login()
        self.logger.info('verifying login')
        self.lg.verify_login()
        self.logger.info('test_login is completed')

