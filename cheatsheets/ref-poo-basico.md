# Referência rápida — POO básico (classes e objetos)

## `class` e `__init__`

```python
class Robo:
    def __init__(self, x=0, y=0, direcao="LESTE"):
        self.x = x
        self.y = y
        self.direcao = direcao

robo1 = Robo()          # __init__ roda automaticamente
```
⚠️ Armadilha: esquecer o `self` no `__init__` (ou em qualquer método) dá `TypeError:
takes N positional arguments but N+1 was given` — o objeto sempre entra como argumento extra.

---

## Acessar atributos: `.` em vez de `[""]`

```python
robo_dict = {"x": 0}     # dict — acesso por colchete
print(robo_dict["x"])

print(robo1.x)           # objeto — acesso por ponto
```
⚠️ Armadilha: `dict` nunca sabe que representa um robô — é `class` que cria um tipo de
verdade, com `type(robo1)` mostrando `<class '__main__.Robo'>`.

---

## `self` é o objeto, passado automaticamente

```python
robo1.avancar()          # o Python reescreve para:
Robo.avancar(robo1)      # ... exatamente isto, por trás dos panos
```
⚠️ Armadilha: `self` não é palavra reservada — é convenção. O que importa é a **posição**
(primeiro parâmetro), não o nome.

---

## Atributo de classe vs. atributo de instância

```python
class Robo:
    LADO_GRADE = 10      # atributo de classe — uma cópia só, compartilhada

    def __init__(self, x=0, y=0):
        self.x = x        # atributo de instância — uma cópia por robô
        self.y = y
```
⚠️ Armadilha: `Robo.LADO_GRADE = 20` muda para **todos** os robôs de uma vez; `robo1.x = 20`
muda só `robo1`.

---

## Métodos: comportamento dentro do objeto

```python
class Robo:
    DELTAS = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}

    def avancar(self):
        dx, dy = Robo.DELTAS[self.direcao]
        self.x += dx
        self.y += dy
```
⚠️ Armadilha: dentro de um método, sempre `self.atributo` — usar o nome do atributo sozinho
(`x` em vez de `self.x`) dá `NameError`.

---

## Argumento default mutável — nunca use lista/dict

```python
def __init__(self, obstaculos=None):           # certo: sentinela None
    self.obstaculos = obstaculos if obstaculos is not None else {}

def __init__(self, obstaculos={}):              # errado: todo robô compartilha o MESMO dict
    self.obstaculos = obstaculos
```
⚠️ Armadilha: o valor default é criado **uma vez só**, na definição da função — não a cada
chamada. Prove com `id(robo1.obstaculos) == id(robo2.obstaculos)`.
