from src.midia import Midia


class Filme(Midia):
    def __init__(self, titulo, genero, ano, classificacao, duracao):
        super().__init__(titulo, genero, ano, classificacao)
        self._tipo = "Filme"
        self._duracao = duracao

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self._tipo = tipo

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao: float):
        self._duracao = duracao

    def detalhes(self):
        return (f"FILME: {self.titulo}\n"
                f"Gênero: {self.genero} | Ano: {self.ano}\n"
                f"Duração: {self._duracao} min | Classificação: {self.classificacao}\n"
                f"Status: {self.status} | Nota: {self.nota_media:.1f}")

    @classmethod
    def from_dict(cls, data):
        obj = cls(data['titulo'], data['genero'], data['ano'], data['classificacao'], data['duracao'])
        obj._elenco = data.get('elenco', [])
        obj._status = data.get('status', "Disponível")
        obj._notas = data.get('notas', [])
        obj._nota_media = data.get('nota_media', 0.0)
        return obj
