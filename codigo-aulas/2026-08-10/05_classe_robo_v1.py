class Robo:
    LADO_GRADE = 10

    def __init__(self, nome, x=0, y=0, direcao="LESTE", obstaculos=None, bateria=100):
        self.nome = nome
        self.x = x
        self.y = y
        self.direcao = direcao
        self.trajetoria = [(x, y)]
        self.obstaculos = obstaculos if obstaculos is not None else {}
        self.bateria = bateria
        self.historico_comandos = []

if __name__ == "__main__":
    wall_e = Robo("Wall-E", x=0, y=0)
    r2d2 = Robo("R2D2", x=5, y=5)

    wall_e.historico_comandos.append("AVANCAR 1")
    print("Wall-E:", wall_e.nome, wall_e.x, wall_e.y, wall_e.historico_comandos)
    print("R2D2:  ", r2d2.nome, r2d2.x, r2d2.y, r2d2.historico_comandos)

# Saída esperada:
# Wall-E: Wall-E 0 0 ['AVANCAR 1']
# R2D2:   R2D2 5 5 []
