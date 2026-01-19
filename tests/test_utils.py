import unittest
import os
from src.utils import Configuracoes, Dados
from src.user import Relatorio
from src.filme import Filme


class TestConfiguracoes(unittest.TestCase):
    def test_valores_padrao(self):
        config = Configuracoes()
        self.assertEqual(config.nota_minima_recomendado, 7.0)

    def test_setter_validacao(self):
        config = Configuracoes()
        config.nota_minima_recomendado = 15  # Deve falhar (ignorar)
        self.assertEqual(config.nota_minima_recomendado, 7.0)

        config.nota_minima_recomendado = 8.5  # Deve funcionar
        self.assertEqual(config.nota_minima_recomendado, 8.5)


class TestRelatorio(unittest.TestCase):
    def test_media_por_genero(self):
        f1 = Filme("F1", "Ação", 2000, "12", 90)
        f1.avaliar(8.0)
        f2 = Filme("F2", "Ação", 2002, "12", 90)
        f2.avaliar(6.0)
        f3 = Filme("F3", "Drama", 2005, "12", 120)
        f3.avaliar(10.0)

        catalogo = [f1, f2, f3]
        rel = Relatorio(catalogo)

        try:
            rel.media_por_genero()
        except Exception as e:
            self.fail(f"media_por_genero falhou com erro: {e}")


class TestDados(unittest.TestCase):
    def setUp(self):
        self.arquivo_teste = "test_catalogo.json"
        self.dados = Dados(self.arquivo_teste)

    def tearDown(self):
        if os.path.exists(self.arquivo_teste):
            os.remove(self.arquivo_teste)

    def test_salvar_carregar(self):
        filme = Filme("Teste", "T", 2020, "L", 100)
        usuarios = []

        self.dados.salvar([filme], usuarios)
        self.assertTrue(os.path.exists(self.arquivo_teste))

        midias_carregadas, _ = self.dados.carregar()
        self.assertEqual(len(midias_carregadas), 1)
        self.assertEqual(midias_carregadas[0].titulo, "Teste")


if __name__ == '__main__':
    unittest.main()
