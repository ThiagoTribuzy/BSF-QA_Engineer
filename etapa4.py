import unittest
import requests

class TestEtapaQuatro(unittest.TestCase):
    def test_create_user(self):  
        url = 'https://serverest.dev/usuarios'
        myObj = {
                    "nome": "Thiago",
                    "email": "thiago.bemol@bemol.com",
                    "password": "Bem@l123",
                    "administrador": "true"
                }
        resp = requests.post(url, json = myObj)
        print("\n1 - Criação de um usuário: "+"\nStatus: "+str(resp.status_code)+"\nResponse: "+resp.text)
        self.assertEqual(201, resp.status_code, "Expected status code 201, got "+str(resp.status_code)) 
    
    def test_check_user(self):
        url = 'https://serverest.dev/login'
        myObj = {
                    "email": "thiago.bemol@bemol.com",
                    "password": "Bem@l123"
                }
        resp = requests.post(url, json = myObj)
        print("\n2 - Verificar se o usuário foi criado: "+"\nStatus: "+str(resp.status_code)+"\nResponse: "+resp.text)
        self.assertEqual(200, resp.status_code, "Expected status code 200, got "+str(resp.status_code)) 
    
    def test_create_product(self):  
        url = 'https://serverest.dev/login'
        myObj = {
                    "email": "thiago.bemol@bemol.com",
                    "password": "Bem@l123"
                }
        auth = requests.post(url, json = myObj).json()["authorization"]
        
        url = 'https://serverest.dev/produtos'
        headers = {
            'authorization': auth
        }
        myObj = {
                    "nome": "Forno_Elétrico_Fischer_B",
                    "preco": 799,
                    "descricao": "Forno Elétrico Fischer Gourmet Grill Bancada 44 Litros 127V Inox 9741/7985",
                    "quantidade": 488
                }
        resp = requests.post(url, json = myObj, headers = headers)
        print("\n3 - Criação de um produto: "+"\nStatus: "+str(resp.status_code)+"\nResponse: "+resp.text)
        self.assertEqual(201, resp.status_code, "Expected status code 201, got "+str(resp.status_code)) 

    def test_check_product(self):  
        url = 'https://serverest.dev/produtos?nome=Forno_Elétrico_Fischer'
        resp = requests.get(url)
        print("\n4 - Verificar se o produto foi criado: "+"\nStatus: "+str(resp.status_code)+"\nResponse: "+resp.text)
        self.assertEqual(200, resp.status_code, "Expected status code 200, got "+str(resp.status_code)) 
        
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestEtapaQuatro("test_create_user"))
    test_suite.addTest(TestEtapaQuatro("test_check_user"))
    test_suite.addTest(TestEtapaQuatro("test_create_product"))
    test_suite.addTest(TestEtapaQuatro("test_check_product"))
    return test_suite

if __name__ == '__main__':
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)