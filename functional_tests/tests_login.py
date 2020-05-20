import pdb
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from django.utils import translation
from django.conf import settings
from users.models import CustomUser

class LoginTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        CustomUser.objects.create_user('test@example.com', 'password')

    def test_user_login_with_email(self):
        with translation.override('es'):
            self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn('comercio local' , self.selenium.title)
        element = self.selenium.find_element_by_link_text("Autentificarse")
        element.click()
        inputbox = self.selenium.find_element_by_id('id_username')
        inputbox.send_keys("test@example.com")
        inputbox = self.selenium.find_element_by_id('id_password')
        inputbox.send_keys("password")
        button = self.selenium.find_element_by_tag_name('button')
        button.click()
        element = self.selenium.find_element_by_id('greeting')
        self.assertIn('Hola test@example.com' , element.text)
        element = self.selenium.find_element_by_link_text("Salir")
        element.click()
        element = self.selenium.find_element_by_id('greeting')
        self.assertIn('No esta autentificado' , element.text)
        # pdb.set_trace()
