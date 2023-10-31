from kivymd.app import MDApp
from kivy.core.window import Window
import requests


class Buscador(MDApp):
    Window.size = (300, 600)

    def buscarEndereco(self):
        try:
            entrada_dados = int(self.root.ids.entrada_dados.text)
            saida_dados = self.root.ids.saida_dados

            if len(str(entrada_dados)) != 8:
                raise ValueError

            url = f"https://cep.awesomeapi.com.br/json/{entrada_dados}"
            response = requests.get(url)
            data = response.json()

            if "code" in data:
                raise ValueError

            for key in data:
                {
                    print(key, ":", data[key])
                }

            saida_dados.text = (
                f"CEP: {data['cep']}\nLogradouro: {data['address']}\n"
                f"Bairro: {data['district']}\nCidade: {data['city']}\n"
                f"Estado: {data['state']}")
        except ValueError:
            print("Deve conter 8 caracteres e apenas números.")


Buscador().run()
