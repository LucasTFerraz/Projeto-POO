print("--- versão com o bug (obstaculos={} como default) ---")

class RoboComBug:
    def __init__(self, x=0, y=0, direcao="LESTE", obstaculos={}):
        self.x = x
        self.y = y
        self.direcao = direcao
        self.trajetoria = [(x, y)]
        self.obstaculos = obstaculos

robo1 = RoboComBug()
robo2 = RoboComBug()
robo1.obstaculos[(2, 2)] = True
print(robo2.obstaculos)                                   # {(2, 2): True} — vazou!
print(id(robo1.obstaculos) == id(robo2.obstaculos))        # True — mesmo objeto na memória

print()
print("--- versão corrigida (sentinela None) ---")

class Robo:
    LADO_GRADE = 10

    def __init__(self, x=0, y=0, direcao="LESTE", obstaculos=None):
        self.x = x
        self.y = y
        self.direcao = direcao
        self.trajetoria = [(x, y)]
        self.obstaculos = obstaculos if obstaculos is not None else {}


robo1 = Robo()
robo2 = Robo(5, 5)
robo1.obstaculos[(2, 2)] = True
print(robo2.obstaculos)                                    # {} — agora independente

print(robo1.LADO_GRADE, robo2.LADO_GRADE)                  # 10 10 — atributo de classe
print(robo1.x, robo2.x)                                     # 0 5 — atributo de instância
