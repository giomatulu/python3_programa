import programa
from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

v_de_vinganca = Filme("v de vingança", 2005, 133)

v_de_vinganca.dar_like()

print(f"Nome: {v_de_vinganca.nome} - Ano: {v_de_vinganca.ano} - "
      f"Duração: {v_de_vinganca.duracao} - Likes: {v_de_vinganca.likes}")

