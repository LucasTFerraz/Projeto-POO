# Exercício Básico — Aula 1

## Contexto

O robô está na posição `(x=6, y=0)` numa grade 10 × 10. Ele só se move para leste (eixo x).

## Problema

O robô vai tentar andar `passos = 5` passos para leste. Escreva um programa que:

1. Calcula o destino: `novo_x = x + passos`.
2. Se o destino couber na grade (`0 <= novo_x < 10`), atualiza `x` e imprime a nova posição no formato `Robô em (novo_x, 0)` (use f-string).
3. Se bater na parede leste (`novo_x >= 10`), imprime `Parede leste! Fiquei em (6, 0)`.

Use variáveis fixas no código (sem `input()`).

## Exemplo

Valores iniciais: `x = 6`, `passos = 5`

Saída esperada:
```
Parede leste! Fiquei em (6, 0)
```

Teste também com `passos = 3` — saída esperada:
```
Robô em (9, 0)
```

## Dica

Calcule `novo_x` antes de entrar no `if`. Só atualize `x = novo_x` dentro do ramo em que ele cabe na grade — nunca antes de decidir.
