# Exercício Médio — Aula 4

## Contexto

Hoje vimos `*args` (funções que recebem qualquer quantidade de argumentos posicionais) e `map`
(aplicar uma transformação a cada elemento de uma sequência). Este exercício pede para combinar
os dois numa função só.

## Problema

Escreva `distancias(*passos)`, que recebe qualquer quantidade de passos do robô (dicts com `x` e
`y`) como argumentos variádicos, e devolve uma lista com a distância Manhattan de cada passo até
a origem `(0, 0)` — ou seja, `abs(x) + abs(y)` — usando `map` com uma `lambda` (não uma
comprehension).

## Exemplo

```python
p1 = {"x": 3, "y": 0}
p2 = {"x": 3, "y": 2}
p3 = {"x": 6, "y": 4}

print(distancias(p1, p2, p3))
print(distancias(*[p1, p2, p3]))   # mesmo resultado, chamando com * na lista
```

Saída esperada:
```
[3, 5, 10]
[3, 5, 10]
```
