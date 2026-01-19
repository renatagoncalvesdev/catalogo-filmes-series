import json
import os


class Configuracoes:
    def __init__(self):
        self._nota_minima_recomendado = 7.0
        self._limite_listas = 5
        self._multiplicador_duracao = 1.0
        self._arquivo_config = "config.json"

    @property
    def nota_minima_recomendado(self):
        return self._nota_minima_recomendado

    @nota_minima_recomendado.setter
    def nota_minima_recomendado(self, valor):
        if 0 <= valor <= 10:
            self._nota_minima_recomendado = valor
        else:
            print("A nota mínima deve estar entre 0 e 10.")

    @property
    def limite_listas(self):
        return self._limite_listas

    def salvar(self):
        data = {
            "nota_minima": self._nota_minima_recomendado,
            "limite_listas": self._limite_listas,
            "multiplicador": self._multiplicador_duracao
        }
        try:
            with open(self._arquivo_config, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            print("Configurações salvas com sucesso.")
        except IOError as error:
            print(f"Erro ao salvar configurações: {error}")

    def carregar(self):
        if not os.path.exists(self._arquivo_config):
            return
        try:
            with open(self._arquivo_config, encoding='utf-8') as file:
                data = json.load(file)
                self._nota_minima_recomendado = data.get("nota_minima", 7.0)
                self._limite_listas = data.get("limite_listas", 5)
                self._multiplicador_duracao = data.get("multiplicador", 1.0)
        except json.JSONDecodeError:
            print("Erro ao ler arquivo de configurações.")
