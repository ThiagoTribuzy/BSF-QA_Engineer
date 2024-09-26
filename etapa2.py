import time
import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# import speech_recognition as sr
# import requests
# import mimetypes

class Etapa2(unittest.TestCase):
    
    driver: Firefox | None = None
    
    def setUp(self) -> None:
        self.driver = Firefox()
        url = 'https://buscacepinter.correios.com.br/app/endereco/index.php'
        self.driver.get(url)
                
    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()
    
    def test_correios_cep(self):  
        inputCEP =  WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, 'endereco')))
        inputCEP.send_keys('69005-040')
        
        self.driver.execute_script("alert('Preencha o captcha.');")
        time.sleep(10)

        # O site dos correios adicionou um captcha para poder realizar a pesquisa, fiz a tentativa de Bypass utilizando OCR e Speech Recognition,
        # mas não obtive sucesso, pois ao tentar realizar o download da imagem ou o arquivo .wav, o sistema de captcha da "Securimage" repassa um 
        # arquivo diferente do captcha visivel na tela do webdriver. Para contornar de forma rápida, foi escolhido realizar este passo de forma manual.
        # Abaixo está a tentativa do código.
        
        # audioResults = self.driver.find_elements(By.XPATH,'//*[@id="captcha_image_audio_controls"]/a')
        # r = sr.Recognizer()
        # print(audioResults[0].get_attribute('href'))
        # response = requests.get(audioResults[0].get_attribute('href'))
        # content = response.content
        # content_type = response.headers['Content-Type']
        # ext = mimetypes.guess_extension(content_type)

        # with open('captcha_audio'+ext, 'wb') as file:
        #     file.write(content)
        #     file.close()
    
        # wav = sr.AudioFile('captcha_audio.wav')
        # with wav as source:
        #     audio = r.listen(source)
        #     try:
        #         s = r.recognize_google(audio,language='pt-BR')
        #         print("Text: "+s)
        #     except Exception as err:
        #         print("Exception: "+str(err))
        
        logradouroNome = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
        bairroDistrito = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
        localidadeUF = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
        cep = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')
        
        print("\n-----Busca por CEP-----\nLogradouro/Nome: "+logradouroNome.text+"\nBairro/Distrito: "+bairroDistrito.text+"\nLocalidade/UF: "+localidadeUF.text+"\nCEP: "+cep.text)
                    
    def test_correios_logradouro(self):  
        inputCEP =  WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, 'endereco')))
        inputCEP.send_keys('Lojas Bemol')
        
        self.driver.execute_script("alert('Preencha o captcha.');")
        time.sleep(50)
        
        logradouroNome = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
        bairroDistrito = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
        localidadeUF = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
        cep = self.driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')
        
        print("\n-----Busca por Nome-----\nLogradouro/Nome: "+logradouroNome.text+"\nBairro/Distrito: "+bairroDistrito.text+"\nLocalidade/UF: "+localidadeUF.text+"\nCEP: "+cep.text)
                    
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(Etapa2("test_correios_cep"))
    test_suite.addTest(Etapa2("test_correios_logradouro"))
    return test_suite

if __name__ == '__main__':
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)