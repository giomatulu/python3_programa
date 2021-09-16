import programa
from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f" {self._nome} ({self.ano}) — Duração: {self.duracao} min — {self._likes} Likes")

v_de_vinganca = Filme("v de vingança", 2005, 133)
v_de_vinganca.dar_like()

harry_potter_4 = Filme("harry potter e o cálice de fogo", 2005, 157)
harry_potter_4.dar_like()


