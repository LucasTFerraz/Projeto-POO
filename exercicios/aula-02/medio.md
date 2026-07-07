# Exercício Médio — Aula 2

## Contexto

O robô tem sensores que conseguem checar **qualquer** direção, não só a que ele está
encarando no momento — sem se mover. A tabela de deltas de movimento é:

```python
DELTAS = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}
LADO_GRADE = 10
```

## Problema

Escreva uma função `checar_sensores(x, y, obstaculos, direcoes)` que recebe a posição atual
do robô, um dict de obstáculos (`{(x, y): True, ...}`) e uma **lista** de direções a checar
(ex.: `["NORTE", "LESTE", "SUL", "OESTE"]`). Para cada direção da lista, calcule a célula
vizinha usando `DELTAS` e decida se ela está livre: dentro da grade **e** sem obstáculo.

A função deve **retornar** um dict no formato `{direcao: True/False}`, um par por direção
checada — sem mover o robô e sem usar `print` dentro da função.

## Exemplo

```python
x, y = 3, 1
obstaculos = {(3, 2): True, (4, 1): True}
checar_sensores(x, y, obstaculos, ["NORTE", "LESTE", "SUL", "OESTE"])
```

Saída esperada (valor retornado pela função):
```python
{"NORTE": False, "LESTE": False, "SUL": True, "OESTE": True}
```

Teste também com `obstaculos = {}` (grade sem obstáculos), mesma posição `(3, 1)` e as
mesmas quatro direções — saída esperada:
```python
{"NORTE": True, "LESTE": True, "SUL": True, "OESTE": True}
```
