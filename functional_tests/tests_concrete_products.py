import pdb
from django.test import tag
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from django.utils import translation
from users.models import CustomUser
from products.models import Product
from concrete_products.models import ConcreteProduct

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
        self.user = CustomUser.objects.create_user('test@example.com', 'password')
        self.product1 = Product.objects.create(name='product1',
                                               varieties=['variety1'])


    @tag('selenium')
    def test_user_makes_concrete_product(self):
        with translation.override('es'):
            self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.client.login(email='test@example.com', password='password')
        # self.client.force_login(self.user)
        element = self.selenium.find_element_by_link_text("Productos concretos").click()
        element = self.selenium.find_element_by_id('Crear un nuevo producto concreto').click()
        inputbox = self.selenium.find_element_by_id('')
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
