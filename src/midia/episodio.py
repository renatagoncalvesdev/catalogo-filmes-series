class Episodio:
    def __init__(self, numero, titulo, duracao, data_lancamento):
        self._numero = numero
        self._titulo = titulo
        self._duracao = duracao
        self._data_lancamento = data_lancamento
        self._status = "Não Assistido"
        self._nota = None

    # Getters
    @property
    def numero(self): return self._numero
    @property
    def titulo(self): return self._titulo
    @property
    def duracao(self): return self._duracao
    @property
    def nota(self): return self._nota
    @property
    def status(self): return self._status

    def avaliar(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
            self._status = "Assistido"
        else:
            print("Nota deve ser entre 0 e 10.")

    def to_dict(self):
        return {
            "numero": self._numero,
            "titulo": self._titulo,
            "duracao": self._duracao,
            "data_lancamento": self._data_lancamento,
            "status": self._status,
            "nota": self._nota
        }

    @classmethod
    def from_dict(cls, data):
        ep = cls(data['numero'], data['titulo'], data['duracao'], data['data_lancamento'])
        ep._status = data['status']
        ep._nota = data['nota']
        return ep
