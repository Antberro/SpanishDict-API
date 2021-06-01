from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options



class SpanishDictClient(object):

    def __init__(self):
        ''''
        Creates instance of SpanishDictClient in order to interface with SpanishDict.com
        '''

        self.URL = 'https://www.spanishdict.com/translate/'
        self.MAX_CHARS = 500

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)




    def translate(self, text: str) -> str:
        '''
        Translate the given text from English to Spanish or Spanish to English.

        Args:
            text (str): text to translate, max of 500 chars

        Returns:
            message (str): translated text
        '''

        assert (len(text) <= self.MAX_CHARS), 'expected text to have a max of 500 characters'

        # send GET request to page source
        self.driver.get(self.URL + text)

        # extract translation
        element1 = self.driver.find_elements_by_class_name('content--2F-n_tCo')[0]
        element2 = element1.find_element_by_tag_name('span')
        out_text = element2.find_element_by_tag_name('span').text

        return out_text
