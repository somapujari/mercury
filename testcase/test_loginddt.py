import pytest

from pageobject.loginpage import LoginPage


class Test_Login:
    base_url = 'https://demo.guru99.com/test/newtours/'

    @pytest.mark.parametrize('username, password', [
        ('mercury', 'mercury'),
        ('soma', 'soma123'),
        ('mercury', 'm')
    ]
    )
    def test_login(self, setup, username, password):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lg = LoginPage(self.driver)
        self.lg.enter_username(username)
        self.lg.enter_password(password)
        self.lg.click_login()
        self.lg.verify_login()
