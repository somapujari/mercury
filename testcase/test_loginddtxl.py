from pageobject.loginpage import LoginPage
from utility.readxl import Readxl


class Test_Login:
    base_url = 'https://demo.guru99.com/test/newtours/'
    path = r'C:\Users\Dell\PycharmProjects\mercury\testdata\soma.xlsx'
    sheet_name = 'Sheet1'

    def test_login(self, setup):
        assertion_error = []
        rows = Readxl.get_row_count(self.path, self.sheet_name)
        for r in range(1, rows+1):
            self.driver = setup
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(10)
            self.lg = LoginPage(self.driver)
            username = Readxl.read_data(self.path, self.sheet_name, row=r, column=1)
            self.lg.enter_username(username)
            password = Readxl.read_data(self.path, self.sheet_name, row=r, column=2)
            self.lg.enter_password(password)
            self.lg.click_login()
            try:
                self.lg.verify_login()
                assertion_error.append('pass')
                Readxl.write_data(self.path, self.sheet_name, r, column=4, value='pass')
            except Exception as e:
                print(e)
                print(f'{username , password}, assert failed')
                assertion_error.append('fail')
                Readxl.write_data(self.path, self.sheet_name, r, column=4, value='fail')
            # self.driver.close()
            actual = Readxl.read_data(self.path, self.sheet_name, row=r, column=4)
            expected = Readxl.read_data(self.path, self.sheet_name, row=r, column=3)
            if actual == expected:
                assert True
            else:
                self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\mercury\screenshots\login_fail.png')
                assert False
