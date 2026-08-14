# Referência rápida — Dataclasses e enums

## `@dataclass`: `__init__`/`__repr__`/`__eq__` gerados

```python
@dataclass
class Posicao:
    x: int
    y: int          # anotação de tipo é obrigatória — sem ela, não é campo

p1 = Posicao(3, 4)  # __init__ gerado
print(p1)            # __repr__ gerado: Posicao(x=3, y=4)
print(p1 == Posicao(3, 4))  # __eq__ gerado: True
```
⚠️ Armadilha: `y = 0` (sem `: tipo`) vira atributo de **classe** comum, fora do
`__init__`/`__repr__` — some da comparação sem aviso nenhum.

---

## `frozen=True`: trava reatribuição

```python
@dataclass(frozen=True)
class Comando:
    acao: str
    valor: int | str

c = Comando("AVANCAR", 3)
c.valor = 5           # FrozenInstanceError: cannot assign to field 'valor'
```
⚠️ Armadilha: `frozen=True` é imutabilidade **rasa** — se um campo é uma lista,
`frozen` trava só o rótulo, não o conteúdo. `objeto.lista_campo.append(x)` funciona,
calado, mesmo com `frozen=True`.

---

## `field(default_factory=...)`: evita valor default compartilhado

```python
@dataclass(frozen=True)
class Leitura:
    posicao: tuple
    obstaculos_proximos: list = field(default_factory=list)  # certo

    # obstaculos_proximos: list = []   # ERRO — nem chega a rodar (ValueError)
```
⚠️ Armadilha: mesma raiz do argumento default mutável (`def __init__(self,
obstaculos=None)`) — `default_factory` cria uma coleção **nova** para cada
instância; um valor solto (`[]`, `{}`) seria compartilhado por todas.

---

## `Enum`: um conjunto fechado de valores válidos

```python
class Direcao(Enum):
    LESTE = (1, 0)      # o valor pode carregar dado útil, não só um número
    NORTE = (0, 1)
    OESTE = (-1, 0)
    SUL = (0, -1)

Direcao.LESTE.value      # (1, 0)
Direcao.LESTE.name       # 'LESTE'
Direcao.LESTE == "LESTE" # False — Enum comum não é igual a nada fora dele
Direcao((1, 0))           # Direcao.LESTE — busca reversa, do valor pro membro
```
⚠️ Armadilha: comparar `direcao == "LESTE"` depois de migrar para `Enum` nunca mais
bate — é rígido de propósito, mas quebra código antigo que ainda usa string.

---

## Enum com método: comportamento embutido no valor

```python
class Direcao(Enum):
    LESTE = (1, 0)
    NORTE = (0, 1)
    OESTE = (-1, 0)
    SUL = (0, -1)

    def virar_esquerda(self):
        ordem = [Direcao.LESTE, Direcao.NORTE, Direcao.OESTE, Direcao.SUL]
        return ordem[(ordem.index(self) + 1) % 4]

robo1.direcao = robo1.direcao.virar_esquerda()   # substitui GIRAR_ESQ[direcao]
dx, dy = robo1.direcao.value                      # substitui DELTAS[direcao]
```
⚠️ Armadilha: referenciar `Direcao.LESTE` dentro de um **método** de `Direcao`
funciona (roda só quando chamado, com a classe já pronta); usar `Direcao.LESTE` no
**valor** de outro membro, durante a própria declaração da classe, não funciona.
