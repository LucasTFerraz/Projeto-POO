# Referência rápida — Descriptors

## `__dict__` — onde o atributo mora de verdade

```python
robo1 = Robo("Wall-E")
print(robo1.__dict__)        # {'nome': 'Wall-E', 'x': 0, ...} — instância
print(Robo.__dict__["LADO_GRADE"])   # 10 — atributo de CLASSE, nunca na instância
```
⚠️ Armadilha: `self.atributo = valor` não é mágica — é inserir uma chave em
`self.__dict__`. Um atributo de classe só aparece no `__dict__` da instância se
alguém escrever nela explicitamente.

---

## Descriptor básico — `__get__`/`__set__`

```python
class NaoNegativo:
    def __set_name__(self, owner, name):
        self.nome = "_" + name              # descobre o próprio nome sozinho

    def __get__(self, instance, owner):
        if instance is None:                # acesso pela CLASSE (Robo.alcance)
            return self
        return instance.__dict__[self.nome]

    def __set__(self, instance, valor):
        if valor < 0:
            raise ValueError(f"{self.nome[1:]} não pode ser negativo, recebi {valor}")
        instance.__dict__[self.nome] = valor


class Sensor:
    alcance = NaoNegativo()                 # mora UMA VEZ na classe

    def __init__(self, alcance=1):
        self.alcance = alcance              # já passa pelo __set__
```
⚠️ Armadilha: dentro de `__get__`/`__set__`, mexer sempre em
`instance.__dict__[self.nome]` — nunca em `instance.atributo` ou
`setattr(instance, self.nome, valor)`. Isso chama o próprio `__set__` de novo,
e de novo, até `RecursionError: maximum recursion depth exceeded`.

---

## `__set_name__` elimina a repetição do nome

```python
alcance = NaoNegativo("alcance")   # sem __set_name__: nome repetido, risco de typo
alcance = NaoNegativo()            # com __set_name__: nome só aparece uma vez
```
⚠️ Armadilha: sem `__set_name__`, um typo como `NaoNegativo("alcancee")` não quebra
a classe na hora — só aparece depois, quando ninguém acha `"alcancee"` no `__dict__`.

---

## `Coordenada`: a mesma regra, parametrizada

```python
class Coordenada:
    def __init__(self, minimo, maximo):
        self.minimo, self.maximo = minimo, maximo

    def __set_name__(self, owner, name):
        self.nome_publico = name
        self.nome = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.nome]

    def __set__(self, instance, valor):
        if not (self.minimo <= valor < self.maximo):
            raise ValueError(f"{self.nome_publico}={valor} sai da grade "
                              f"({self.minimo} a {self.maximo - 1})")
        instance.__dict__[self.nome] = valor


class Robo:
    LADO_GRADE = 10
    x = Coordenada(0, LADO_GRADE)           # nove linhas de @property viram uma
    y = Coordenada(0, LADO_GRADE)
```
⚠️ Armadilha: `Robo.x` (sem nenhum robô criado) devolve o **objeto `Coordenada`**,
não um número — só `robo1.x` passa `instance` de verdade para `__get__`.

---

## `property` também é um descriptor

```python
print(type(Robo.direcao))                        # <class 'property'>
print(hasattr(Robo.direcao, "__get__"))           # True
```
⚠️ Armadilha: achar que `@property` e descriptor são coisas diferentes —
`@property` já implementa `__get__`/`__set__` por baixo dos panos, só que preso a
**um** atributo de **uma** classe. Um descriptor escrito à mão, como `Coordenada`,
serve para vários atributos e várias classes.

---

## Mesmo protocolo, regra diferente (`raise` vs. `clamp`)

```python
class Percentual:
    def __set_name__(self, owner, name):
        self.nome = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.nome]

    def __set__(self, instance, valor):
        instance.__dict__[self.nome] = max(0, min(100, valor))   # nunca levanta erro


class Robo:
    bateria = Percentual()
```
⚠️ Armadilha: `Coordenada` recusa valor fora do intervalo (`raise`); `Percentual`
aceita e ajusta (`clamp`). `__get__`/`__set__` são só o contrato de interceptação —
o que cada descriptor faz com ele é decisão própria.
