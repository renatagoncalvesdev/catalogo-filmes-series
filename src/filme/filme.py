from src.midia import Midia, MidiaType, MidiaStatus


class Filme(Midia):
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
        super().__init__(titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota_media)

    def avaliar(self, nota: float):
        if 0 > nota > 10:
            raise Exception("A nota deve ser entre 0 e 10.")
        self.nota_media = nota

    def atualizar_status(self, status: MidiaStatus):
        self.status = status

    def __str__(self):
        print(f'{self.titulo}')
        print('\nSOBRE:\n')
        print(f'Gênero: {self.genero}')
        print(f'Ano de lançamento: {self.ano}')
        print(f'Duração: {self.duracao}')
        print(f'Classificação: {self.classificacao}')
        print(f'Status: {self.status.value}')
        print(f'Nota média: {self.nota_media}')
        print('\nElenco:\n')
        for actor, character in self.elenco.items():
            print(f'{actor}: {character}')

    def __eq__(self, other):
        if isinstance(other, Filme):
            return self.titulo == other.titulo

    def __lt__(self, other):
        if isinstance(other, Filme):
            return self.nota_media < other.nota_media
