from datetime import date, timedelta
import requests
import os
from dotenv import load_dotenv
import time

class FacilitaSP:
    def __init__(self):
        load_dotenv()
        return
    
    def TokenAutenticacao(self):
        
        token = 0
        url = f'{os.getenv("URL_REDESIM")}/token-autenticacao'
        body = {
            "autenticacao": {
                "userName": f'{os.getenv("USUARIO_REDESIM")}',
                "password": f'{os.getenv("SENHA_REDESIM")}',
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

        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            
        return response

    def Coleta(self):
        data = {
            "tipo": "FACILITA_SP",
            "status_code": None,
            "headers": None,
            "content": None,
            "cookies": None,
            "response_time": None,
            "url_final": None,
            "history": None
        }

        tempo_inicio = time.time()
        resp_lista_inscrições = self.ListaIncricoes()
        tempo_fim = time.time()

        data["status_code"] = resp_lista_inscrições.status_code
        data["headers"] = resp_lista_inscrições.headers
        data["content"] = resp_lista_inscrições.content
        data["cookies"] = resp_lista_inscrições.cookies
        data["response_time"] = tempo_fim - tempo_inicio
        data["url_final"] = resp_lista_inscrições.url
        data["history"] = resp_lista_inscrições.history

        return data