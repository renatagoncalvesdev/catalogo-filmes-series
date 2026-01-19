# Catálogo de Filmes e Séries

Desenvolver sistema para gerenciar um catálogo pessoal de filmes e séries, com avaliações, status de visualização, temporadas/episódios, histórico e relatórios de consumo de mídia

---
**Equipe**

FELIPE PEREIRA DE SOUZA SILVA

GABRIEL PEREIRA DA SILVA

RENATA DO NASCIMENTO GONÇALVES

**Descrição de responsabilidades de cada membro**

**Entrega 1 — 12/12/2025**

Listar as principais classes do sistema → Renata

Descrever relacionamentos entre as classes → Gabriel

Definir atributos e métodos das classes → Felipe

**Entrega 2 — 19/12/2025**

Implementar classes Midia e Filme → Renata

Implementar classe Serie (com temporadas) → Gabriel

Implementar Episodio + lógica de avaliação → Felipe

**Entrega Final — 17/01/2026**

Criar README e documentação → Renata

Implementar testes + persistência JSON → Gabriel

Integrar módulos + relatórios → Felipe

Criar CLI (ou API mínima) → Felipe

Implementar histórico, listas e favoritos → Gabriel

Implementar configurações e seed inicial → Renata

As demandas foram organizadas no Jira para melhor organização e utilização de metodologia ágil na administração do projeto.
<img width="1360" height="673" alt="JIRA" src="https://github.com/user-attachments/assets/52ec171f-8175-4018-b47b-74108fb572f4" />


___
**Lista das principais classes do sistema**

**Midia**

Atributos: titulo, tipo, genero, ano, duracao, classificacao, elenco, status, nota_media

Metodos: avaliar(), atualizar_status(), __str__(), __eq__(), __lt__()


**Filme**

Atributos: (herda de Midia)

Metodos: detalhes()


**Serie**

Atributos: temporadas

Metodos: adicionar_temporada(), calcular_media(), atualizar_status(), __len__()


**Temporada**

Atributos: numero, episodios

Metodos: adicionar_episodio(), total_episodios()


**Episodio**

Atributos: numero, titulo, duracao, data_lancamento, status, nota

Metodos: avaliar()


**Usuario**

Atributos: nome, listas, historico

Metodos: criar_lista(), adicionar_a_lista(), registrar_assistido()


**ListaPersonalizada**

Atributos: nome, midias

Metodos: adicionar_midia(), remover_midia()


**Relatorio**

Atributos: —
Metodos: media_por_genero(), tempo_total_assistido(), top10(), series_com_mais_episodios()


**Configuracoes**

Atributos: nota_minima_recomendado, limite_listas, multiplicador_duracao

Metodos: carregar(), salvar()


**Dados**

Atributos: caminho_arquivo (str)

Metodos: salvar(), carregar(), seed_inicial()

### Como rodar:

Estando na pasta raiz:

> No terminal: python -m src.main
