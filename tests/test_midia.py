import unittest
from src.filme import Filme
from src.midia import Serie, Temporada, Episodio


class TestEpisodio(unittest.TestCase):
    def test_criacao_episodio(self):
        ep = Episodio(1, "Piloto", 45, "2022-01-01")
        self.assertEqual(ep.numero, 1)
        self.assertEqual(ep.status, "Não Assistido")

    def test_avaliar_episodio(self):
        ep = Episodio(1, "Piloto", 45, "2022-01-01")
        ep.avaliar(9.0)
        self.assertEqual(ep.nota, 9.0)
        self.assertEqual(ep.status, "Assistido")

    def test_avaliar_invalido(self):
        ep = Episodio(1, "Teste", 20, "2022")
        ep.avaliar(11)
        self.assertIsNone(ep.nota)


class TestFilme(unittest.TestCase):
    def setUp(self):
        self.filme = Filme("Matrix", "Sci-Fi", 1999, "14", 136)

    def test_atributos_filme(self):
        self.assertEqual(self.filme.titulo, "Matrix")
        self.assertEqual(self.filme.duracao, 136)

    def test_avaliacao_media(self):
        self.filme.avaliar(10)
        self.filme.avaliar(8)
        self.assertEqual(self.filme.nota_media, 9.0)


class TestSerie(unittest.TestCase):
    def setUp(self):
        self.serie = Serie("Dark", "Drama", 2017, "16")
        self.temp1 = Temporada(1)
        self.ep1 = Episodio(1, "Secrets", 60, "2017-12-01")
        self.ep2 = Episodio(2, "Lies", 55, "2017-12-01")
        self.temp1.adicionar_episodio(self.ep1)
        self.temp1.adicionar_episodio(self.ep2)
        self.serie.adicionar_temporada(self.temp1)

    def test_duracao_total(self):
        self.assertEqual(self.serie.duracao, 115)

    def test_calculo_media_episodios(self):
        self.ep1.avaliar(10)
        self.ep2.avaliar(8)
        media = self.serie.calcular_media()
        self.assertEqual(media, 9.0)

    def test_total_episodios(self):
        self.assertEqual(len(self.serie), 2)


if __name__ == '__main__':
    unittest.main()
