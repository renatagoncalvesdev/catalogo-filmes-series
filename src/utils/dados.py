from src.midia import Serie, Temporada, Episodio
from src.filme import Filme
from src.user import Usuario
import json
import os


class Dados:
    def __init__(self, caminho_arquivo="catalogo.json"):
        self._caminho_arquivo = caminho_arquivo

    @staticmethod
    def seed_inicial():
        filme1 = Filme("O Poderoso Chefão", "Crime", 1972, "18", 175)
        filme1.avaliar(9.8)

        serie1 = Serie("Breaking Bad", "Drama", 2008, "16")
        temp1 = Temporada(1)
        temp1.adicionar_episodio(Episodio(1, "Pilot", 58, "2008-01-20"))
        temp1.adicionar_episodio(Episodio(2, "Cat's in the Bag", 48, "2008-01-27"))
        serie1.adicionar_temporada(temp1)
        serie1.calcular_duracao_total()
        serie1.avaliar(9.5)

        return [filme1, serie1], [Usuario("Admin")]

    def salvar(self, midias, usuarios):
        data = {
            "midias": [m.to_dict() for m in midias],
            "usuarios": [u.to_dict() for u in usuarios]
        }
        try:
            with open(self._caminho_arquivo, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("Dados salvos no disco.")
        except IOError as error:
            print(f"Erro crítico ao salvar: {error}")

    def carregar(self):
        if not os.path.exists(self._caminho_arquivo):
            print("Arquivo não encontrado. Criando base inicial...")
            return self.seed_inicial()

        try:
            with open(self._caminho_arquivo, encoding='utf-8') as f:
                raw_data = json.load(f)

            midias = []
            for item in raw_data.get('midias', []):
                if item.get('tipo_classe') == 'Filme':
                    midias.append(Filme.from_dict(item))
                elif item.get('tipo_classe') == 'Serie':
                    midias.append(Serie.from_dict(item))

            usuarios = [Usuario.from_dict(u) for u in raw_data.get('usuarios', [])]

            return midias, usuarios
        except (json.JSONDecodeError, KeyError) as error:
            print(f"Arquivo corrompido ou formato antigo ({error}). Recriando seed...")
            return self.seed_inicial()
