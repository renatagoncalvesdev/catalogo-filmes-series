from src.filme import Filme
from src.midia import MidiaType, MidiaStatus


class PromptInterface:
    def __init__(self):
        self.__filmes: [Filme] = []

    def show_main_menu(self):
        while True:
            print('1) Registrar filme')
            print('2) Visualiar filme por título')
            print('3) Visualizar todos os filmes')
            option = input('4) Sair\n')
            option = int(option)
            if option == 1:
                self.__registrar_filme()
            elif option == 2:
                self.__visualizar_filme_por_titulo()
            elif option == 3:
                self.__visualizar_filmes()
            elif option == 4:
                break

    def __registrar_filme(self):
        titulo = input('Título do filme: ')
        genero = input('Gênero do filme: ')
        ano = int(input('Ano de lançamento do filme: '))
        duracao = float(input('Duração do filme (em minutos): '))
        classificacao = input('Classificação do filme: ')
        elenco = {'': ''}
        nota_media = float(input('Nota média do filme: '))
        filme = Filme(titulo, MidiaType.FILME, genero, ano, duracao, classificacao, elenco, MidiaStatus.DISPONIVEL,
                      nota_media)
        self.__filmes.append(filme)

    def __visualizar_filme_por_titulo(self):
        if len(self.__filmes) == 0:
            print('Nenhum filme registrado.')
            return
        titulo = input('Informe o título do filme: ')
        for filme in self.__filmes:
            if filme.titulo.lower() == titulo.lower():
                print(filme.__str__())

    def __visualizar_filmes(self):
        if len(self.__filmes) == 0:
            print('Nenhum filme registrado.')
            return
        for filme in self.__filmes:
            print(filme.__str__())
