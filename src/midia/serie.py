from .midia import Midia
from .temporada import Temporada


class Serie(Midia):
    def __init__(self, titulo, genero, ano, classificacao):
        super().__init__(titulo, genero, ano, classificacao)
        self._tipo = "Série"
        self._temporadas = []

    def adicionar_temporada(self, temporada):
        self._temporadas.append(temporada)
        self.calcular_duracao_total()

    def calcular_duracao_total(self):
        total = 0
        for temp in self._temporadas:
            for ep in temp.episodios:
                total += ep.duracao
        self.duracao = total

    def calcular_media(self):
        notas_eps = []
        for temp in self._temporadas:
            for ep in temp.episodios:
                if ep.nota is not None:
                    notas_eps.append(ep.nota)

        if notas_eps:
            self.nota_media = sum(notas_eps) / len(notas_eps)
        return self.nota_media

    def __len__(self):
        return sum(t.total_episodios() for t in self._temporadas)

    def detalhes(self):
        qtd_eps = len(self)
        return (f"SÉRIE: {self.titulo}\n"
                f"Gênero: {self.genero} | Ano: {self.ano}\n"
                f"Temporadas: {len(self._temporadas)} | Episódios Totais: {qtd_eps}\n"
                f"Duração Total: {self.duracao} min\n"
                f"Nota Média (Episódios): {self.nota_media:.1f}")

    def to_dict(self):
        data = super().to_dict()
        data['temporadas'] = [t.to_dict() for t in self._temporadas]
        return data

    @classmethod
    def from_dict(cls, data):
        obj = cls(data['titulo'], data['genero'], data['ano'], data['classificacao'])
        obj._elenco = data.get('elenco', [])
        obj._status = data.get('status', "Disponível")
        obj._notas = data.get('notas', [])
        obj._nota_media = data.get('nota_media', 0.0)
        obj._duracao = data.get('duracao', 0)

        if 'temporadas' in data:
            obj._temporadas = [Temporada.from_dict(t) for t in data['temporadas']]
        return obj
