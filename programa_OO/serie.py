import programa
from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

sherlock = Serie("sherlock", 2010, 3)

sherlock.dar_like()

print(f"Nome: {sherlock.nome} - Ano: {sherlock.ano} "
      f"- Temporadas: {sherlock.temporadas} - Likes: {sherlock.likes}")