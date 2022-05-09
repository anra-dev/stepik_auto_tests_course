import unittest
import warnings

from selenium import webdriver


class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # Убираем сообщения о deprecation notices. 
        # По хорошему нужно использовать класс By, но для согласованности
        # с курсом просто игнорируем эти сообщения
        warnings.filterwarnings("ignore", category=DeprecationWarning) 
    
    def tearDown(self):
        self.browser.quit()

    def find_welcome_text(self, link):
        """
        Заполняет поля регистрации. 
        Возвращает текст об успешной регистрации или None
        """
        self.browser.get(link)

        element_first = self.browser.find_element_by_css_selector(
            'input.first:required')
        element_first.send_keys("Мой first-ответ")

        element_second = self.browser.find_element_by_css_selector(
            'input.second:required')
        element_second.send_keys("Мой second-ответ")

        element_third = self.browser.find_element_by_css_selector(
            'input.third:required')
        element_third.send_keys("Мой third-ответ")

        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        
        return welcome_text_elt.text

    def test_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(
            first=self.find_welcome_text(link),
            second="Congratulations! You have successfully registered!", 
            msg="Registration is failed",
            )
    
    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(
            first=self.find_welcome_text(link),
            second="Congratulations! You have successfully registered!", 
            msg="Registration is failed",
            )


if __name__ == "__main__":
    unittest.main()
