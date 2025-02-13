import time

class RegistraLogs:
    def __init__(self):
        return
    
    def ArquivoTXT(self, caminho, registro):
        with open(caminho, 'a', encoding='utf-8') as arquivo:
            arquivo.write(
                f'\n=================\n \
                LOG - {registro["tipo"]}\n \
                Horario_Registro: {time.strftime("%Y-%m-%d %H:%M:%S")}\n \
                Status_Code: {registro["status_code"]}\n \
                Headers: {registro["headers"]} \n \
                Conteudo: {registro["content"].decode("utf-8")} \n \
                Tempo_Resposta: {registro["response_time"]} \n \
                URL: {registro["url_final"]} \n')
        return