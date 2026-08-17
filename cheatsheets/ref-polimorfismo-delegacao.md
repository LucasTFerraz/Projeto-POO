# Referência rápida — Polimorfismo e delegação

## Duck typing — mesmo método, sem herança nenhuma

```python
class RoboSimulado:                 # NÃO herda de Robo
    def mover(self):
        print("passo virtual")
        return True

robos = [Robo("Wall-E"), RoboSimulado("Sim-1")]
for r in robos:
    r.mover()                       # funciona pros dois — só usa o método
```
⚠️ Armadilha: duck typing não confere tipo nenhum — se o método faltar, o erro só
aparece em tempo de execução (`AttributeError`), não antes.

---

## `mover()` polimórfico por herança (despacho dinâmico)

```python
class Robo:
    def mover(self):
        return self.avancar()       # escrito UMA VEZ só, no Robo

class RoboVeloz(Robo):
    def avancar(self):              # nunca sobrescreve mover(), só avancar()
        return super().avancar() or super().avancar()

RoboVeloz("Flash").mover()          # anda 2 casas — self.avancar() resolve pro tipo real
```
⚠️ Armadilha: achar que "mesmo método, mesmo resultado" — `mover()` nunca muda, mas o
resultado varia porque ele delega para `avancar()`, que **é** sobrescrito.

---

## `isinstance` vs. duck typing — quando não usar

```python
# Ruim: reescreve na mão o que o polimorfismo já faz
if isinstance(objeto, RoboVeloz):
    objeto.mover()
elif isinstance(objeto, Robo):
    objeto.mover()
else:
    print("não sei mover")          # rejeita RoboSimulado mesmo ele tendo mover()

# Bom: confia no método
objeto.mover()
```
⚠️ Armadilha: cadeia de `isinstance`/`elif` chamando o **mesmo** método em cada ramo é
sinal de que o polimorfismo já resolve sozinho. `isinstance` continua legítimo dentro
de métodos como `__eq__`, checando se a comparação faz sentido.

---

## Delegação — um método que só repassa a chamada

```python
class EstrategiaPadrao:
    def mover(self, robo):          # recebe o robô como argumento
        return robo.avancar()       # repassa a chamada — não decide nada sozinho
```
⚠️ Armadilha: confundir com herança — `EstrategiaPadrao` não é um `Robo`, não herda
dele; ela só recebe um `robo` e chama métodos nele.

---

## `Robo` compõe `estrategia` e `mover()` delega

```python
class Robo:
    def __init__(self, nome, estrategia=None, **kwargs):
        ...
        self.estrategia = estrategia if estrategia is not None else EstrategiaPadrao()

    def mover(self):
        return self.estrategia.mover(self)   # delega a decisão pra peça composta
```
⚠️ Armadilha: `self.estrategia = EstrategiaPadrao` (sem os parênteses) não dá erro na
hora de criar o robô — vira a **classe**, não um objeto; o erro só aparece quando
`mover()` chama `self.estrategia.mover(self)`.

---

## Trocar a estratégia em tempo de execução

```python
robo1.estrategia = EstrategiaEsquiva()   # mesmo Robo, sem subclasse nova
robo1.mover()                            # agora desvia de obstáculo em vez de parar
```
⚠️ Armadilha: herança fixa o tipo do objeto desde `class Sub(Base):`, pra sempre —
composição/delegação são só um atributo, trocável a qualquer momento (igual
`robo1.sensor = Sensor(5)`).
