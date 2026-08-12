# Exercício Básico — Aula 6

## Contexto

Em sala, `x`/`y` ganharam `@property` com setter que recusa (`ValueError`) valores fora
da grade:
```python
@property
def x(self):
    return self._x

@x.setter
def x(self, valor):
    if not (0 <= valor < Robo.LADO_GRADE):
        raise ValueError(f"x={valor} sai da grade")
    self._x = valor
```

## Problema

Adicione à classe `Robo` uma property `nome`, com setter que recusa (`ValueError`) nome
vazio ou só com espaços.

## Exemplo

```python
robo = Robo(nome="Wall-E")
try:
    robo.nome = "   "
except ValueError as erro:
    print(erro)
robo.nome = "R2D2"
print(robo.nome)
```

Saída esperada:
```
nome não pode ser vazio
R2D2
```

## Dica

Mesma estrutura do setter de `x` — só troca a condição de "fora da grade" para
`len(valor.strip()) == 0`.
