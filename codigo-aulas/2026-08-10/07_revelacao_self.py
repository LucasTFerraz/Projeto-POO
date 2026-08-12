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

# --- A prova: chamando pelos dois caminhos ---
robo2 = Robo("R2D2")
robo2.avancar()
print(robo2.x, robo2.y)
# Saída esperada: 1 0

robo3 = Robo("BB-8")
Robo.avancar(robo3)          # chamando pela classe, passando o objeto à mão
print(robo3.x, robo3.y)
# Saída esperada: 1 0 — idêntico ao robo2: robo2.avancar() e Robo.avancar(robo3) são a mesma
# chamada; o Python reescreve objeto.metodo(...) para Classe.metodo(objeto, ...) por trás dos
# panos.


# --- A prova de que "self" é só convenção, não palavra reservada ---
class RoboTeste:
    def andou(robo):             # nomeei de "robo", não "self" — funciona igual
        print(f"{robo} andou")


r = RoboTeste()
r.andou()
# Saída esperada (endereço varia): <__main__.RoboTeste object at 0x...> andou


# --- Modo de falha: método comum sem self ---
class RoboQuebrado2:
    def avancar():          # sem o self de novo, agora num método comum
        print("andei")


r2 = RoboQuebrado2()
try:
    r2.avancar()
except TypeError as erro:
    print(f"TypeError: {erro}")
# Saída esperada:
# TypeError: RoboQuebrado2.avancar() takes 0 positional arguments but 1 was given
