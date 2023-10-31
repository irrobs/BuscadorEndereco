from kivymd.app import MDApp
from kivy.core.window import Window
import requests


class Buscador(MDApp):
    Window.size = (300, 600)

    def buscarEndereco(self):
        try:
            entrada_dados = int(self.root.ids.entrada_dados.text)
            saida_dados_cep = self.root.ids.saida_dados_cep
            saida_dados_logradouro = self.root.ids.saida_dados_logradouro
            saida_dados_bairro = self.root.ids.saida_dados_bairro
            saida_dados_cidade = self.root.ids.saida_dados_cidade
            saida_dados_estado = self.root.ids.saida_dados_estado

            if len(str(entrada_dados)) != 8:
                raise ValueError

            url = f"https://cep.awesomeapi.com.br/json/{entrada_dados}"
            response = requests.get(url)
            data = response.json()

            if "code" in data:
                raise ValueError

            saida_dados_cep.text = f"CEP: {data['cep']}"
            saida_dados_logradouro.text = f"Logradouro: {data['address']}"
            saida_dados_bairro.text = f"Bairro: {data['district']}"
            saida_dados_cidade.text = f"Cidade: {data['city']}"
            saida_dados_estado.text = f"Estado: {data['state']}"
                
                
                
        except ValueError:
            print("Deve conter 8 caracteres e apenas números.")


Buscador().run()
