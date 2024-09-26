import time
import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class Etapa3(unittest.TestCase):
    
    driver = Firefox()
        
    def setUp(self) -> None:
        url = 'https://www.trivago.com.br/pt-BR'
        self.driver.get(url)
        
    def searchNclick(self,xpath,searchname):
        count = 1
        while(True):
                path = xpath+str(count)+']'
                list = self.driver.find_element(By.XPATH, path)
                if(searchname in list.text):
                    list.click()
                    break
                else:
                    count+=1
                
    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()
    
    def test_trivago(self):  
        trivagoSearch = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-auto-complete"]')))
        trivagoSearch.send_keys('Manaus')
        
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
        
        trivagoOptions = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="accommodation-list"]')
        trivagoOptionsList:list[WebElement] = trivagoOptions.find_elements(By.CSS_SELECTOR, '[data-testid="accommodation-list-element"]')
        
        for option in trivagoOptionsList:
            valueCheck = option.find_element(By.CSS_SELECTOR, '[data-testid="expected-price"]')
            
            if valueCheck is not None:
                nameSection = option.find_element(By.CSS_SELECTOR,'[data-testid="item-name"]')
                ratingSection = option.find_element(By.CSS_SELECTOR,'[data-testid="rating-section"]')
                
                name = nameSection.find_element(By.CSS_SELECTOR,'[itemprop="name"]')
                rating = ratingSection.find_element(By.TAG_NAME,'strong')
                value = valueCheck.find_element(By.TAG_NAME, 'b')
                
                print("Nome: "+name.text+"\nNota: "+rating.text+"\nValor: "+value.text)
                break
            
            continue    
        
if __name__ == '__main__':
    unittest.main()