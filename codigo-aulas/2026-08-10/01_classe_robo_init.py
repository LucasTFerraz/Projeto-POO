robo_dict = {"x": 0, "y": 0, "direcao": "LESTE", "trajetoria": [(0, 0)]}
print(robo_dict)
print(type(robo_dict))
# Saída esperada:
# {'x': 0, 'y': 0, 'direcao': 'LESTE', 'trajetoria': [(0, 0)]}
# <class 'dict'>

class Robo:
    def __init__(self, x=0, y=0, direcao="LESTE"):
        self.x = x
        self.y = y
        self.direcao = direcao
        self.trajetoria = [(x, y)]

robo1 = Robo()
print(robo1)
print(type(robo1))
# Saída esperada (o endereço de memória varia a cada execução):
# <__main__.Robo object at 0x...>
# <class '__main__.Robo'>

print(robo1.x, robo1.y, robo1.direcao)
# Saída esperada: 0 0 LESTE

# Comparação lado a lado — colchete + chave (dict) vs. ponto + nome (objeto):
print(robo_dict["x"])   # dict
print(robo1.x)           # objeto