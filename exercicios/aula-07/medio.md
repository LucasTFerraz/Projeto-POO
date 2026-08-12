# Exercício Médio — Aula 7

## Contexto

Vocês já viram `__iter__` percorrendo a `trajetoria` de um `Robo`, e `__eq__`
comparando duas `Posicao` por valor. Este exercício combina os dois numa classe
nova, que representa a rota completa de um robô.

## Problema

Escreva a classe `Rota`, que guarda uma lista de `Posicao` (reaproveite a `Posicao`
com `__eq__` defensivo já escrita em sala) em `self.pontos`, com:
- `__iter__`, para que `for p in rota` percorra `self.pontos`;
- `__eq__` (defensivo, com `isinstance` + `NotImplemented`), que compara duas rotas
  posição a posição — duas rotas são iguais se tiverem o mesmo número de pontos e
  cada `Posicao` correspondente for igual (reaproveitando o `__eq__` de `Posicao`,
  sem comparar `x`/`y` na mão).

## Exemplo

```python
r1 = Rota([Posicao(0, 0), Posicao(1, 0), Posicao(1, 1)])
r2 = Rota([Posicao(0, 0), Posicao(1, 0), Posicao(1, 1)])
r3 = Rota([Posicao(0, 0), Posicao(2, 2)])

for p in r1:
    print(p)

print(r1 == r2)
print(r1 == r3)
print(r1 == "não é uma rota")
```

Saída esperada:
```
Posicao(0, 0)
Posicao(1, 0)
Posicao(1, 1)
True
False
False
```
