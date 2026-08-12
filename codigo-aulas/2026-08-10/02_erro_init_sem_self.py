class RoboQuebrado:
    def __init__(x=0, y=0, direcao="LESTE"):     # faltou o self!
        pass

try:
    r = RoboQuebrado(2, 3, "NORTE")
except TypeError as erro:
    print(f"TypeError: {erro}")

# Saída esperada:
# TypeError: RoboQuebrado.__init__() takes from 0 to 3 positional arguments but 4 were given
#
# Por quê: RoboQuebrado(2, 3, "NORTE") sempre manda o objeto recém-criado como primeiro
# argumento de __init__, além dos três valores explícitos — quatro no total, para um método
# que (sem self) só tem posições para três. É a mesma "coisa que o Python manda de graça"
# que vira self no Bloco 2.
