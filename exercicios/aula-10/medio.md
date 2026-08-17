# Exercício Médio — Aula 10

## Contexto

Vocês viram polimorfismo (`mover()` respondendo diferente por herança e por duck
typing) e delegação (`Robo` compõe uma `estrategia` e repassa a chamada pra ela). Este
exercício pede as duas ferramentas **juntas**: uma estratégia que envolve outra
estratégia.

## Problema

Escreva `EstrategiaContadora`, uma estratégia que **envolve** outra estratégia
qualquer. No `__init__`, ela recebe uma `estrategia` (guarde em
`self.estrategia_interna`) e inicializa `self.chamadas = 0`. O método
`mover(self, robo)` deve: incrementar `self.chamadas` em 1, delegar o movimento de
fato para `self.estrategia_interna.mover(robo)`, e devolver o que essa chamada
devolver.

`EstrategiaContadora` não deve saber nada sobre o que a estratégia interna faz — ela
precisa funcionar tanto com `EstrategiaPadrao()` quanto com `EstrategiaEsquiva()` (ou
qualquer outra estratégia com `mover(self, robo)`), sem checar o tipo dela em nenhum
momento.

## Exemplo

```python
robo1 = Robo("Bender", estrategia=EstrategiaContadora(EstrategiaPadrao()))
robo1.mover()
robo1.mover()
robo1.mover()
print(robo1.x, robo1.estrategia.chamadas)

obstaculos = {(1, 0): True}
robo2 = Robo("Wall-E", obstaculos=obstaculos, estrategia=EstrategiaContadora(EstrategiaEsquiva()))
robo2.mover()
print(robo2.x, robo2.y, robo2.estrategia.chamadas)
```

Saída esperada:
```
3 3
0 1 1
```
