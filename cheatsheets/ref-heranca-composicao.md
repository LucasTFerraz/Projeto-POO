# Referência rápida — Herança e composição

## `class Sub(Base)` e `super().__init__`

```python
class RoboComSensor(Robo):
    def __init__(self, nome, alcance_sensor=2, **kwargs):
        super().__init__(nome, **kwargs)   # cria nome/x/y/... como o Robo faria
        self.alcance_sensor = alcance_sensor
```
⚠️ Armadilha: esquecer de repassar `**kwargs` pra `super().__init__` — os atributos do
`Robo` voltam sempre pro valor padrão, mesmo passando `x=5` na criação.

---

## Sobrescrita: substituir vs. estender

```python
class RoboComSensor(Robo):
    def sensor_frente(self):        # SUBSTITUI — nunca chama a versão do Robo
        ...

class RoboVeloz(Robo):
    def avancar(self):              # ESTENDE — chama super() e faz mais em cima
        moveu1 = super().avancar()
        moveu2 = super().avancar()
        return moveu1 or moveu2
```
⚠️ Armadilha: reescrever a lógica inteira quando só precisava **acrescentar** algo —
`super().metodo()` reaproveita o que o pai já faz.

---

## O erro clássico: esquecer `super().__init__()`

```python
class RoboQuebrado(Robo):
    def __init__(self, nome, alcance_sensor=2):
        self.alcance_sensor = alcance_sensor   # esqueceu super().__init__(nome)

r = RoboQuebrado("Bug")
r.x     # AttributeError: 'RoboQuebrado' object has no attribute '_x'
```
⚠️ Armadilha: nada avisa na hora de **definir** a classe — o erro só aparece quando
alguém tenta **usar** um atributo que o `__init__` do pai deveria ter criado.

---

## `isinstance()` — checando a relação é-um

```python
isinstance(robo_sensor, Robo)            # True — RoboComSensor é um Robo
isinstance(robo_sensor, RoboComSensor)   # True
isinstance(robo_comum, RoboComSensor)    # False — Robo comum não é RoboComSensor
```
⚠️ Armadilha: é-um é de **mão única** — toda subclasse é a classe-mãe, o inverso não vale.

---

## Composição: `self.outro = OutraClasse(...)`

```python
class Robo:
    def __init__(self, nome, alcance_sensor=1):
        self.nome = nome
        self.sensor = Sensor(alcance_sensor)     # Robo TEM um Sensor

    def sensor_frente(self):
        return self.sensor.ler(self)             # delega pro objeto composto
```
⚠️ Armadilha: `self.sensor = Sensor` (sem os parênteses) não dá erro na hora — vira a
**classe**, não um objeto; o erro só aparece quando algo chama `self.sensor.ler(...)`.

---

## Composição troca em tempo de execução

```python
robo1.sensor = Sensor(alcance=5)   # troca a peça, mesmo objeto, sem criar Robo novo
```
⚠️ Armadilha: herança fixa o tipo do objeto desde `class Sub(Base):`, pra sempre — só
composição permite trocar a "peça" depois que o objeto já existe.

---

## Herança = é-um, composição = tem-um

Use **herança** quando a variação muda como o objeto **se comporta de verdade**
(`RoboVeloz` sobrescrevendo `avancar()`). Use **composição** quando a variação é uma
**peça ou capacidade** que poderia ser trocada, combinada ou configurada por parâmetro
(`Sensor`, `Radio`) — evita a "explosão de subclasses" (uma classe nova pra cada
combinação de peças).
