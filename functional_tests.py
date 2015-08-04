from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        #to check out it's homepage
        self.browser.get('http://localhost:8000')

        #notice the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #invite to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
               inputbox.get_attribute('placeholder'),
               'Enter a to-do item'
                )


        # I typed "Buy peacock feathers" into the text box
        inputbox.send_keys('Buy peacock feathers')

        # When i hit enter the page updates and now the page list
        # "1: Buy peacock feathers" as an item in to-do list table
        inputbox.send_keys(keys.ENTER)

        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
               )
        # There is still a textbox inviting me to add a to-do
        self.fail('Finish the test !')

if __name__== '__main__':
    unittest.main()
