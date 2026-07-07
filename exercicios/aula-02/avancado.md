# Exercício Avançado — Aula 2

## Contexto

Em testes de software, comparar uma saída **real** contra uma saída **esperada** (um
"golden file") é a base de qualquer teste de regressão: se o programa mudar de
comportamento, o teste precisa apontar exatamente **onde** a divergência começou — não só
dizer "diferente".

## Problema

O robô grava sua trajetória como uma lista de tuplas `(x, y)`. Escreva uma função
`comparar_trajetorias(esperada, real)` que recebe duas listas de tuplas e retorna um dict
relatório:

- Percorra as duas listas posição a posição. Na primeira posição em que os dois valores
  diferirem, pare e retorne
  `{"identica": False, "primeira_divergencia": indice, "detalhe": "posição <indice>: esperado <valor_esperado>, obtido <valor_real>"}`.
- Se uma lista for mais curta que a outra e todas as posições em comum forem iguais, isso
  também é uma divergência: retorne
  `{"identica": False, "primeira_divergencia": <tamanho da lista comum>, "detalhe": "tamanhos diferentes: esperado N posições, obtido M posições"}`.
- Se as duas listas forem idênticas (mesmo tamanho, todas as posições iguais), retorne
  `{"identica": True, "primeira_divergencia": None, "detalhe": "trajetórias idênticas"}`.

A função não deve usar `print` — só `return`.

## Exemplo

```python
esperada = [(0, 0), (1, 0), (2, 0), (3, 0)]
real     = [(0, 0), (1, 0), (2, 1), (3, 0)]
comparar_trajetorias(esperada, real)
```

Saída esperada (valor retornado):
```python
{
    "identica": False,
    "primeira_divergencia": 2,
    "detalhe": "posição 2: esperado (2, 0), obtido (2, 1)",
}
```

Teste também com listas idênticas:
```python
comparar_trajetorias([(0, 0), (1, 0)], [(0, 0), (1, 0)])
# {"identica": True, "primeira_divergencia": None, "detalhe": "trajetórias idênticas"}
```

E com tamanhos diferentes (mesmo prefixo):
```python
comparar_trajetorias([(0, 0), (1, 0), (2, 0)], [(0, 0), (1, 0)])
# {"identica": False, "primeira_divergencia": 2, "detalhe": "tamanhos diferentes: esperado 3 posições, obtido 2 posições"}
```

**Conexão com testes de software:** isso é exatamente o que um framework de testes faz por
trás de um `assert trajetoria_real == trajetoria_esperada` quando você quer uma mensagem de
erro útil em vez de só "AssertionError": ele localiza o primeiro ponto de divergência para
que quem lê o relatório não precise comparar as duas listas na mão. O mesmo padrão aparece em
testes de regressão de qualquer sistema que produza uma sequência de estados (logs, frames de
simulação, respostas de API gravadas).
