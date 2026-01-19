class ListaPersonalizada:
    def __init__(self, nome):
        self._nome = nome
        self._midias = []

    @property
    def nome(self): return self._nome
    @property
    def midias(self): return self._midias

    def adicionar_midia(self, midia):
        if not any(m == midia.titulo for m in self._midias):
            self._midias.append(midia.titulo)
            print(f"'{midia.titulo}' adicionado à lista '{self._nome}'.")
        else:
            print("Mídia já está na lista.")

    def remover_midia(self, nome_midia):
        if nome_midia in self._midias:
            self._midias.remove(nome_midia)
            print("Removido com sucesso.")
        else:
            print("Mídia não encontrada na lista.")

    def to_dict(self):
        return {
            "nome": self._nome,
            "midias": self._midias
        }

    @classmethod
    def from_dict(cls, data):
        lista = cls(data['nome'])
        lista._midias = data['midias']
        return lista
