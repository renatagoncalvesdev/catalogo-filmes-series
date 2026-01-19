from .episodio import Episodio


class Temporada:
    def __init__(self, numero):
        self._numero = numero
        self._episodios = []

    @property
    def numero(self): return self._numero
    @property
    def episodios(self): return self._episodios

    def adicionar_episodio(self, episodio):
        self._episodios.append(episodio)

    def total_episodios(self):
        return len(self._episodios)

    def to_dict(self):
        return {
            "numero": self._numero,
            "episodios": [ep.to_dict() for ep in self._episodios]
        }

    @classmethod
    def from_dict(cls, data):
        temp = cls(data['numero'])
        temp._episodios = [Episodio.from_dict(ep) for ep in data['episodios']]
        return temp
