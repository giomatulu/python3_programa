import programa
from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f" {self._nome} ({self.ano}) — {self.temporadas} temporadas — {self._likes} Likes")

sherlock = Serie("sherlock", 2010, 3)

sherlock.dar_like()
