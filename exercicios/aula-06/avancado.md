# Exercício Avançado — Aula 6

## Contexto

Hoje, o setter de `x` **recusa** um valor inválido levantando `ValueError` na hora. Em
frameworks de teste (ex.: `pytest-check`, ou o padrão manual de "soft assertions"), às
vezes é melhor **não** parar no primeiro problema — coletar todas as violações de uma
rodada e reportar todas de uma vez no final, em vez de interromper no primeiro erro.

## Problema

Escreva a classe `Robo`, com:
- um atributo `violacoes` (lista, uma por robô, sem repetir o bug do argumento default
  mutável);
- uma property `x` cujo setter, ao receber um valor fora de `[0, 9]`, **não levanta
  exceção** — em vez disso, acrescenta uma string descrevendo o problema a
  `self.violacoes` (formato `f"x={valor} sai da grade (0 a 9)"`) e mantém o valor
  anterior de `x` sem alterar.

Depois, escreva `relatorio_violacoes(robo)`, que devolve quantas violações o robô
acumulou.

## Exemplo

```python
robo = Robo()
robo.x = 999
robo.x = 5
robo.x = -1
print(robo.x, relatorio_violacoes(robo))
print(robo.violacoes)
```

Saída esperada:
```
5 2
['x=999 sai da grade (0 a 9)', 'x=-1 sai da grade (0 a 9)']
```

## Extensão — conexão com testes de software

Pesquise o padrão "soft assertions" (ex.: `pytest-check`, `assertpy`, ou o
`SoftAssert` do Selenium/Java). Por que uma suíte de teste de UI (que clica em vários
elementos numa página) costuma preferir esse padrão a um `assert` tradicional que
para no primeiro erro?
