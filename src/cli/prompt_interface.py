from src.utils.config import Configuracoes
from src.utils.dados import Dados
from src.user.usuario import Usuario
from src.user.relatorio import Relatorio
from src.filme import Filme
from src.midia import Serie


class PromptInterface:
    @staticmethod
    def menu_principal():
        print("\n=== CINE CATALOGO CLI ===")
        print("1. Listar Catálogo")
        print("2. Ver Detalhes de Mídia")
        print("3. Avaliar Mídia")
        print("4. Meus Usuários e Listas")
        print("5. Relatórios")
        print("6. Configurações")
        print("7. Salvar Dados")
        print("8. Adicionar Mídia")
        print("0. Sair")
        return input("Escolha: ")

    def main(self):
        config = Configuracoes()
        config.carregar()

        db = Dados()
        catalogo, usuarios = db.carregar()

        usuario_ativo = usuarios[0] if usuarios else Usuario("Convidado")
        relatorio = Relatorio(catalogo)

        while True:
            opcao = self.menu_principal()

            if opcao == '1':
                print(f"\n--- Catálogo ({len(catalogo)} itens) ---")
                catalogo.sort()
                for i, m in enumerate(catalogo):
                    # Acesso via propriedade
                    print(f"{i + 1}. {m}")

            elif opcao == '2':
                termo = input("Digite o nome da mídia: ").lower()
                encontrado = next((m for m in catalogo if m.titulo.lower() == termo), None)
                if encontrado:
                    print("\n" + encontrado.detalhes())
                else:
                    print("Mídia não encontrada.")

            elif opcao == '3':
                termo = input("Nome da mídia para avaliar: ").lower()
                encontrado = next((m for m in catalogo if m.titulo.lower() == termo), None)
                if encontrado:
                    try:
                        nota = float(input("Nota (0-10): "))
                        encontrado.avaliar(nota)
                    except ValueError:
                        print("Por favor, digite um número válido.")
                else:
                    print("Mídia não encontrada.")

            elif opcao == '4':
                print(f"\nUsuário Ativo: {usuario_ativo.nome}")
                print("a. Criar Nova Lista")
                print("b. Adicionar Mídia a uma Lista")
                print("c. Ver Minhas Listas")
                print("d. Registrar 'Assistido' no Histórico")
                sub = input("Escolha: ").lower()

                if sub == 'a':
                    nome = input("Nome da nova lista: ")
                    usuario_ativo.criar_lista(nome, config.limite_listas)
                elif sub == 'b':
                    lista_nome = input("Nome da lista destino: ")
                    midia_nome = input("Nome da mídia: ")
                    midia = next((m for m in catalogo if m.titulo.lower() == midia_nome.lower()), None)
                    if midia:
                        usuario_ativo.adicionar_a_lista(lista_nome, midia)
                    else:
                        print("Mídia não encontrada.")
                elif sub == 'c':
                    for lists in usuario_ativo.listas:
                        print(f"Lista [{lists.nome}]: {', '.join(lists.midias)}")
                elif sub == 'd':
                    midia_nome = input("Nome da mídia assistida: ")
                    midia = next((m for m in catalogo if m.titulo.lower() == midia_nome.lower()), None)
                    if midia:
                        usuario_ativo.registrar_assistido(midia)

            elif opcao == '5':
                print("a. Média por Gênero")
                print("b. Top 10 Avaliados")
                print("c. Séries mais longas")
                print("d. Meu Tempo Assistido")
                sub = input("Escolha: ").lower()

                if sub == 'a':
                    relatorio.media_por_genero()
                elif sub == 'b':
                    relatorio.top10()
                elif sub == 'c':
                    relatorio.series_com_mais_episodios()
                elif sub == 'd':
                    relatorio.tempo_total_assistido(usuario_ativo)

            elif opcao == '6':
                print(f"Nota mínima atual: {config.nota_minima_recomendado}")
                try:
                    nova = float(input("Definir nova nota mínima recomendada: "))
                    config.nota_minima_recomendado = nova
                    config.salvar()
                except ValueError:
                    print("Valor inválido.")

            elif opcao == '7':
                db.salvar(catalogo, usuarios)

            elif opcao == '8':
                print("\n--- Adicionar Nova Mídia ---")
                tipo = input("Tipo (1-Filme, 2-Série): ")
                titulo = input("Título: ")
                genero = input("Gênero: ")
                try:
                    ano = int(input("Ano: "))
                    classificacao = input("Classificação: ")

                    if tipo == '1':
                        duracao = int(input("Duração (min): "))
                        # Criação do objeto Filme usando os dados inseridos
                        novo = Filme(titulo, genero, ano, classificacao, duracao)
                        catalogo.append(novo)
                        print(f"Sucesso! Filme '{titulo}' adicionado ao catálogo.")

                    elif tipo == '2':
                        # Criação do objeto Série
                        novo = Serie(titulo, genero, ano, classificacao)
                        catalogo.append(novo)
                        print(f"Sucesso! Série '{titulo}' adicionada ao catálogo.")

                    else:
                        print("Tipo inválido. Escolha 1 ou 2.")
                except ValueError:
                    print("Erro: Ano e Duração devem ser números inteiros.")

            elif opcao == '0':
                db.salvar(catalogo, usuarios)
                print("Saindo... Até logo!")
                break

            else:
                print("Opção inválida.")
