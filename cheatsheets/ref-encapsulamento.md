# Referência rápida — Encapsulamento e properties

## Convenção `_atributo` — comunica, não protege

```python
class Bateria:
    def __init__(self, nivel=100):
        self._nivel = nivel      # "não acesse direto" — mas nada impede

b = Bateria()
b._nivel = -999                  # funciona, mesmo assim
```
⚠️ Armadilha: `_atributo` é só convenção — o Python não bloqueia nada. Quem protege é
getter/setter (à moda antiga) ou `@property`.

---

## `_atributo` vs. `__atributo` (name mangling)

```python
class Carro:
    def __init__(self, potencia):
        self.__motor = Motor(potencia)   # Python renomeia para _Carro__motor

carro.__motor            # AttributeError — esse nome não existe de fora
carro._Carro__motor      # funciona (feio, de propósito)
```
⚠️ Armadilha: `__` resolve colisão de nome em herança — sem herança, use só `_`. A
maioria do código Python usa um underscore, mesmo para dado bem interno.

---

## `@property`: getter que se lê como atributo

```python
class Robo:
    def __init__(self, x=0):
        self.x = x                # já passa pelo setter, com validação

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if not (0 <= valor < Robo.LADO_GRADE):
            raise ValueError(f"x={valor} sai da grade")
        self._x = valor
```
⚠️ Armadilha: se `__init__` escrever `self._x = x` (direto, com underscore) em vez de
`self.x = x`, a validação **não roda** na criação do objeto.

---

## Duas estratégias de validação: recusar vs. prender (clamp)

```python
@x.setter
def x(self, valor):
    if not (0 <= valor < Robo.LADO_GRADE):
        raise ValueError(...)          # recusa — bug deve ser visível na hora
    self._x = valor

@bateria.setter
def bateria(self, valor):
    self._bateria = max(0, min(100, valor))   # prende — estado normal, não é bug
```
⚠️ Armadilha: escolher a estratégia errada — recusar bateria baixa (ela deveria poder
chegar a 0 sem quebrar nada) ou prender coordenada inválida (mascara um bug real).

---

## Property somente leitura

```python
@property
def posicao(self):
    return (self._x, self._y)      # sem @posicao.setter — não aceita escrita

robo1.posicao = (5, 5)             # AttributeError: no setter
```
⚠️ Armadilha: use property somente leitura para valor **derivado** de outros atributos
(não faz sentido atribuir direto) — mudança deve passar por um método (`avancar`, etc.).
