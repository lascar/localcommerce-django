import pdb
from django.test import tag
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.utils import translation
from django.conf import settings

class RootTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    @tag('selenium')
    def test_root(self):
        with translation.override('es'):
            self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn('comercio local' , self.selenium.title)
        element = self.selenium.find_element_by_css_selector('.card-header')
        self.assertIn(('listado de los productos'.upper()), element.text)
        # pdb.set_trace()
