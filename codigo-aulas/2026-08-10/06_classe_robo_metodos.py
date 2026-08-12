class Robo:
    LADO_GRADE = 10
    DELTAS = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}
    GIRAR_ESQ = {"LESTE": "NORTE", "NORTE": "OESTE", "OESTE": "SUL", "SUL": "LESTE"}
    GIRAR_DIR = {"LESTE": "SUL", "SUL": "OESTE", "OESTE": "NORTE", "NORTE": "LESTE"}

    def __init__(self, nome, x=0, y=0, direcao="LESTE", obstaculos=None, bateria=100):
        self.nome = nome
        self.x = x
        self.y = y
        self.direcao = direcao
        self.trajetoria = [(x, y)]
        self.obstaculos = obstaculos if obstaculos is not None else {}
        self.bateria = bateria
        self.historico_comandos = []

    def sensor_frente(self):
        dx, dy = Robo.DELTAS[self.direcao]
        nx, ny = self.x + dx, self.y + dy
        return 0 <= nx < Robo.LADO_GRADE and 0 <= ny < Robo.LADO_GRADE and (nx, ny) not in self.obstaculos

    def avancar(self):
        if self.sensor_frente():
            dx, dy = Robo.DELTAS[self.direcao]
            self.x += dx
            self.y += dy
            self.trajetoria.append((self.x, self.y))
            return True
        return False

    def girar(self, lado):
        if lado == "ESQ":
            self.direcao = Robo.GIRAR_ESQ[self.direcao]
        elif lado == "DIR":
            self.direcao = Robo.GIRAR_DIR[self.direcao]

if __name__ == "__main__":
    robo1 = Robo("Wall-E")
    print(robo1.avancar())
    print(robo1.x, robo1.y)
    # Saída esperada: True \n 1 0

    robo1.girar("ESQ")
    print(robo1.direcao)
    # Saída esperada: NORTE
