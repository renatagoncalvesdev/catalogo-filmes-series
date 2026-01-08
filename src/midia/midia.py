from abc import ABC, abstractmethod
from .type import MidiaType
from .status import MidiaStatus


class Midia(ABC):
    def __init__(self, titulo: str, tipo: MidiaType, genero: str, ano: int, duracao: float, classificacao: str,
                 elenco: dict[str, str], status: MidiaStatus, nota_media: float):
        self.titulo: str = titulo
        self.tipo: MidiaType = tipo
        self.genero: str = genero
        self.ano: int = ano
        self.duracao: float = duracao
        self.classificacao: str = classificacao
        self.elenco: dict[str, str] = elenco
        self.status: MidiaStatus = status
        self.nota_media: float = nota_media

    @abstractmethod
    def avaliar(self, nota: float):
        pass

    @abstractmethod
    def atualizar_status(self, status: MidiaStatus):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass
