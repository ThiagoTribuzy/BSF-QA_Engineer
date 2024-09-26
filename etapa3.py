import time
import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class TestEtapaTres(unittest.TestCase):
    
    driver = Firefox()
        
    def setUp(self) -> None:
        url = 'https://www.trivago.com.br/pt-BR'
        self.driver.get(url)
        
    def searchNclick(self,xpath,search_name):
        count = 1
        while(True):
                path = xpath+str(count)+']'
                list = self.driver.find_element(By.XPATH, path)
                if(search_name in list.text):
                    list.click()
                    break
                else:
                    count+=1
                
    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()
    
    def test_trivago(self):  
        trivago_search = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-auto-complete"]')))
        trivago_search.send_keys('Manaus')
        
        time.sleep(1)
        self.searchNclick('//*[@id="suggestion-list"]/ul/li[','Manaus')
        time.sleep(1)
        
        self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/section[1]/div[2]/div[4]/div/button').click()
        
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '[name="sorting_selector"]').click()
        time.sleep(1)
        self.searchNclick('//*[@id="__next"]/div/main/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/section/div/ul/li[','Avaliação e sugestões')
        self.driver.find_element(By.CSS_SELECTOR, '[data-testid="filters-popover-apply-button"]').click()
        time.sleep(5)
        
        trivago_options = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="accommodation-list"]')
        trivago_options_list:list[WebElement] = trivago_options.find_elements(By.CSS_SELECTOR, '[data-testid="accommodation-list-element"]')
        
        for option in trivago_options_list:
            value_check = option.find_element(By.CSS_SELECTOR, '[data-testid="expected-price"]')
            
            if value_check is not None:
                name_section = option.find_element(By.CSS_SELECTOR,'[data-testid="item-name"]')
                rating_section = option.find_element(By.CSS_SELECTOR,'[data-testid="rating-section"]')
                
                name = name_section.find_element(By.CSS_SELECTOR,'[itemprop="name"]')
                rating = rating_section.find_element(By.TAG_NAME,'strong')
                value = value_check.find_element(By.TAG_NAME, 'b')
                
                print("Nome: "+name.text+"\nNota: "+rating.text+"\nValor: "+value.text)
                break
            
            continue    
        
if __name__ == '__main__':
    unittest.main()