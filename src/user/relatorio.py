from src.midia import Serie


class Relatorio:
    def __init__(self, catalogo):
        self._catalogo = catalogo  # Lista de mídias

    def media_por_genero(self):
        generos = {}
        for midia in self._catalogo:
            # Acessa via Property
            if midia.genero not in generos:
                generos[midia.genero] = []
            if midia.nota_media > 0:
                generos[midia.genero].append(midia.nota_media)

        print("\n--- Média por Gênero ---")
        for genero, notas in generos.items():
            if notas:
                media = sum(notas) / len(notas)
                print(f"{genero}: {media:.2f}")
            else:
                print(f"{genero}: Sem avaliações")

    def tempo_total_assistido(self, usuario):
        total_minutos = 0
        titulos_assistidos = [h['titulo'] for h in usuario.historico]

        for midia in self._catalogo:
            if midia.titulo in titulos_assistidos:
                total_minutos += midia.duracao

        horas = total_minutos // 60
        minutos = total_minutos % 60
        print(f"\nTempo total assistido por {usuario.nome}: {horas}h {minutos}m")

    def top10(self):
        # Acessa via Property
        ranking = sorted(self._catalogo, key=lambda x: x.nota_media, reverse=True)
        print("\n--- TOP 10 Melhores Avaliados ---")
        for i, midia in enumerate(ranking[:10], 1):
            print(f"{i}. {midia.titulo} - Nota: {midia.nota_media:.1f}")

    def series_com_mais_episodios(self):
        series = [m for m in self._catalogo if isinstance(m, Serie)]
        ranking = sorted(series, key=lambda x: len(x), reverse=True)
        print("\n--- Séries com Mais Episódios ---")
        for s in ranking[:5]:
            print(f"{s.titulo}: {len(s)} episódios")
