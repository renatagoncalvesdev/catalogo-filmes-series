from abc import ABC, abstractmethod


class Midia(ABC):
    def __init__(self, titulo: str, genero: str, ano: int, classificacao: str):
        self.titulo: str = titulo
        self.tipo: str = ''
        self.genero: str = genero
        self.ano: int = ano
        self.duracao: float = 0
        self.classificacao: str = classificacao
        self.elenco: [dict[str, str]] = [{}]
        self.status: str = 'Disponível'
        self.nota_media: float = 0
        self.notas: [float] = []

    @abstractmethod
    def detalhes(self):
        pass

    def avaliar(self, nota: float):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            self.nota_media = sum(self.notas) / len(self.notas)
            print(f"{self.titulo} avaliado com {nota}. Nova média: {self.nota_media:.1f}")
        else:
            print("Nota inválida.")

    def atualizar_status(self, novo_status: str):
        self.status = novo_status

    def __str__(self):
        return f"{self.titulo} ({self.ano}) - {self.genero} | Nota: {self.nota_media:.1f}"

    def __eq__(self, other):
        if isinstance(other, Midia):
            return self.titulo.lower() == other.titulo.lower() and self.ano == other.ano
        return False

    def __lt__(self, other):
        return self.titulo < other.titulo

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "genero": self.genero,
            "ano": self.ano,
            "classificacao": self.classificacao,
            "duracao": self.duracao,
            "elenco": self.elenco,
            "status": self.status,
            "notas": self.notas,
            "nota_media": self.nota_media,
            "tipo_classe": self.__class__.__name__
        }
