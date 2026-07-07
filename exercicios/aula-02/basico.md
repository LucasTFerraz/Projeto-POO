# Exercício Básico — Aula 2

## Contexto

O robô está em `(x=5, y=5)`, virado para `"NORTE"`, numa grade 10×10. Há um obstáculo
marcado no dict `obstaculos = {(5, 7): True}`.

## Problema

Escreva um programa que faça o robô tentar andar `passos = 5` passos para `NORTE`, **um passo
de cada vez** (`for _ in range(passos)`):

1. A cada passo, calcule o destino `(nx, ny)` usando o delta da direção atual (`NORTE` →
   `dx, dy = 0, 1`).
2. Se o destino couber na grade (`0 <= nx < 10` e `0 <= ny < 10`) e **não** estiver em
   `obstaculos`, atualize a posição e imprima `Robô em (nx, ny)`.
3. Se o destino for inválido ou tiver obstáculo, imprima `Bloqueado em (x, y)` (a posição
   **atual**, antes do passo que falhou) e pare o loop com `break`.

Use variáveis fixas no código (sem `input()`).

## Exemplo

Valores iniciais: `x, y = 5, 5`, `obstaculos = {(5, 7): True}`, `passos = 5`

Saída esperada:
```
Robô em (5, 6)
Bloqueado em (5, 6)
```

Teste também com `obstaculos = {(5, 9): True}` (mesma posição e direção inicial) — saída
esperada:
```
Robô em (5, 6)
Robô em (5, 7)
Robô em (5, 8)
Bloqueado em (5, 8)
```

## Dica

Calcule `nx, ny` **antes** de decidir. A condição de checagem tem duas partes ligadas por
`and`: a posição precisa estar dentro da grade **e** não estar em `obstaculos`. Só atualize
`x, y = nx, ny` dentro do ramo em que as duas partes são verdadeiras.
