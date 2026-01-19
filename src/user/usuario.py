from .lista_personalizada import ListaPersonalizada
from datetime import datetime


class Usuario:
    def __init__(self, nome):
        self._nome = nome
        self._listas = []
        self._historico = []

    @property
    def nome(self): return self._nome
    @property
    def listas(self): return self._listas
    @property
    def historico(self): return self._historico

    def criar_lista(self, nome_lista, config_limite):
        if len(self._listas) >= config_limite:
            print("Limite de listas atingido.")
            return
        nova_lista = ListaPersonalizada(nome_lista)
        self._listas.append(nova_lista)
        print(f"Lista '{nome_lista}' criada.")

    def adicionar_a_lista(self, nome_lista, midia_obj):
        for lista in self._listas:
            if lista.nome == nome_lista:
                lista.adicionar_midia(midia_obj)
                return
        print("Lista não encontrada.")

    def registrar_assistido(self, midia_obj):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._historico.append({"titulo": midia_obj.titulo, "data": agora})
        midia_obj.atualizar_status("Assistido")
        print(f"'{midia_obj.titulo}' registrado no histórico.")

    def to_dict(self):
        return {
            "nome": self._nome,
            "listas": [lists.to_dict() for lists in self._listas],
            "historico": self._historico
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data['nome'])
        user._historico = data.get('historico', [])
        user._listas = [ListaPersonalizada.from_dict(lists) for lists in data.get('listas', [])]
        return user
