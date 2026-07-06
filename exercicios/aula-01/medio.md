# Exercício Médio — Aula 1

## Contexto

O robô começa em `(x=2, y=0)` numa grade 10 × 10 e só anda para leste. Ele vai receber uma
**lista** de quantidades de passos, uma tentativa de movimento atrás da outra.

## Problema

Escreva um programa que:

1. Percorra a lista `tentativas = [3, 10, 2, 1]` com um `for`.
2. Para cada valor de `tentativas`, calcule `novo_x = x + valor` e decida com `if`/`elif`/`else`
   se o robô anda (atualiza `x` e imprime `Robô em (x, 0)`) ou bate na parede leste (imprime
   `Parede leste! Fiquei em (x, 0)`, sem atualizar `x`).
3. Repita para os quatro valores da lista, na ordem, acumulando a posição de uma tentativa para
   a próxima.
4. Ao final do `for`, imprima a posição final no formato `Posição final: (x, 0)`.

## Exemplo

Valores iniciais: `x = 2`, `tentativas = [3, 10, 2, 1]`

Saída esperada:
```
Robô em (5, 0)
Parede leste! Fiquei em (5, 0)
Robô em (7, 0)
Robô em (8, 0)
Posição final: (8, 0)
```

Teste também com `tentativas = [4, 4, 4]` (começando de novo em `x = 2`) — saída esperada:
```
Robô em (6, 0)
Parede leste! Fiquei em (6, 0)
Parede leste! Fiquei em (6, 0)
Posição final: (6, 0)
```
