# Exercício Básico — Aula 3

## Contexto

O robô v5 usa flood fill (`celulas_alcancaveis`) para contar todas as células que consegue
alcançar a partir de onde está, sem limite de distância.

## Problema

Escreva `celulas_no_raio(robo, raio)` — uma variação de `celulas_alcancaveis` que só conta
células cuja distância até a posição do robô (em passos, `|dx| + |dy|`) seja **menor ou igual**
a `raio`. Reaproveite o padrão de `flood_fill` (os três casos-base + a soma dos vizinhos) e
acrescente um quarto caso-base: distância maior que `raio`.

```python
LADO_GRADE = 5

def flood_fill_raio(robo, visitadas, x, y, raio):
    # TODO: reaproveite os três casos-base de flood_fill (fora da grade,
    # obstáculo, já visitada) e acrescente um quarto: se a distância de (x, y)
    # até (robo['x'], robo['y']) for maior que `raio`, retorne 0.
    pass

def celulas_no_raio(robo, raio):
    visitadas = set()
    return flood_fill_raio(robo, visitadas, robo['x'], robo['y'], raio)
```

## Exemplo

Entrada: robô em `(0, 0)`, grade 5×5 sem obstáculos.

```python
robo = {'x': 0, 'y': 0, 'obstaculos': {}}
print(celulas_no_raio(robo, 1))   # esperado: 3
print(celulas_no_raio(robo, 2))   # esperado: 6
```

Saída esperada:
```
3
6
```

## Dica

A distância entre `(x, y)` e a posição do robô é `abs(x - robo['x']) + abs(y - robo['y'])`.
Calcule-a logo no início da função, antes dos outros casos-base — se já passou do raio, nem
vale a pena checar o resto.
