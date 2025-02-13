from coleta_dados.coletor import ColetorDeDados
from logs.registra_logs import RegistraLogs

from dotenv import load_dotenv
import os

load_dotenv()

coletor = ColetorDeDados()
logs = RegistraLogs()

dados_coletados = coletor.coletar()
logs.ArquivoTXT(os.getenv("CAMINHO_LOG_FACILITA"), dados_coletados)
