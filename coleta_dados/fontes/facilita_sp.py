from datetime import date, timedelta
import requests
import os
from dotenv import load_dotenv

class FacilitaSP:
    def __init__(self):
        load_dotenv()
        return
    
    def TokenAutenticacao(self):
        
        token = 0
        url = f"{os.getenv("URL_REDESIM")}/token-autenticacao"
        body = {
            "autenticacao": {
                "userName": f"{os.getenv("USUARIO_REDESIM")}",
                "password": f"{os.getenv("SENHA_REDESIM")}",
                "refreshToken": "string",
                "grantType": "webadmin-credential"
            }
        }

        try:
            response = requests.post(url, json = body)
            response.raise_for_status()

            token = response.json()["tokenAcesso"]

        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")

        return token
    
    def ListaIncricoes(self):
        dataFinal = date.today()
        dataInicial = dataFinal - timedelta(days=1)

        url = f'{os.getenv("URL_REDESIM")}/listar-inscricoes-municipais'
        token = self.TokenAutenticacao()

        body = {
            "intervalo": {
                "dataInicial": f"{dataInicial}",
                "dataFinal": f"{dataFinal}"
            }
        }
        headers = {
            "Authorization": f"Bearer {token}"
        }
        try:
            response = requests.post(url, json = body, headers = headers)
            response.raise_for_status()

            print(response.json())

        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            
        return
