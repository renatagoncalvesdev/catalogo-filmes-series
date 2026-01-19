import unittest
from src.user import Usuario
from src.filme import Filme


class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.user = Usuario("Tester")
        self.filme = Filme("Inception", "Sci-Fi", 2010, "14", 148)

    def test_criar_lista(self):
        self.user.criar_lista("Favoritos", config_limite=5)
        self.assertEqual(len(self.user.listas), 1)
        self.assertEqual(self.user.listas[0].nome, "Favoritos")

    def test_limite_listas(self):
        self.user.criar_lista("Lista 1", config_limite=1)
        self.user.criar_lista("Lista 2", config_limite=1)
        self.assertEqual(len(self.user.listas), 1)

    def test_adicionar_midia_lista(self):
        self.user.criar_lista("Ver Depois", 5)
        self.user.adicionar_a_lista("Ver Depois", self.filme)
        self.assertIn("Inception", self.user.listas[0].midias)

    def test_historico(self):
        self.user.registrar_assistido(self.filme)
        self.assertEqual(len(self.user.historico), 1)
        self.assertEqual(self.user.historico[0]['titulo'], "Inception")
        self.assertEqual(self.filme.status, "Assistido")


if __name__ == '__main__':
    unittest.main()
