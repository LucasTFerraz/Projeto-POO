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

    def avancar_n(self, passos):
        for _ in range(passos):
            if not self.avancar():
                break

    def executar(self, comandos):
        tabela = {"AVANCAR": self.avancar_n, "GIRAR": self.girar}
        for cmd in comandos:
            partes = cmd.strip().upper().split()
            acao = partes[0]
            if acao == "PARAR":
                print(f"{self.nome} parou.")
                break
            if acao in tabela:
                valor = partes[1] if acao == "GIRAR" else int(partes[1])
                tabela[acao](valor)
            self.historico_comandos.append(cmd)


if __name__ == "__main__":
    robo_a = Robo("Alfa", x=0, y=0, direcao="LESTE")
    robo_b = Robo("Beta", x=9, y=9, direcao="OESTE")

    robo_a.executar(["AVANCAR 3", "PARAR"])
    robo_b.executar(["GIRAR ESQ", "AVANCAR 2", "PARAR"])

    print(robo_a.x, robo_a.y, robo_a.direcao)
    print(robo_b.x, robo_b.y, robo_b.direcao)
    # Saída esperada:
    # Alfa parou.
    # Beta parou.
    # 3 0 LESTE
    # 9 7 SUL

    # Contraste com atributo de classe — muda para todos, não só quem "mudou":
    Robo.LADO_GRADE = 20
    print(robo_a.LADO_GRADE, robo_b.LADO_GRADE)
    # Saída esperada: 20 20
