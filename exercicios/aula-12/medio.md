# Exercício Médio — Aula 12

## Contexto

Em sala, `__setattr__` guardou um log de toda mudança de estado, e `__getattr__`
calculou um atributo sob demanda a partir de outra informação já guardada. Este
exercício combina as duas ideias: um atributo derivado, calculado a partir do próprio
histórico de auditoria — sem nunca ser guardado diretamente em lugar nenhum.

## Problema

Escreva `RoboMedidor`, uma classe com `x`/`y` (sem validação de grade — não é o foco
aqui) que:

1. Via `__setattr__`, registra em `self._log_mudancas` toda vez que `x` ou `y` mudam
   de valor (incluindo a atribuição inicial no `__init__`), como par
   `(nome_attr, valor)`.
2. Via `__getattr__`, expõe um atributo `distancia_percorrida`: o número de vezes que
   `x` ou `y` mudaram **depois** da criação do robô (ou seja, o total de entradas no
   log, menos as duas entradas iniciais de `x` e `y`). Não guarde esse número em
   nenhum atributo — recalcule a partir do log toda vez que alguém perguntar.

## Exemplo

```python
medidor = RoboMedidor(x=0, y=0)
medidor.x = 1
medidor.y = 1
medidor.x = 2
print(medidor.distancia_percorrida)
```

Saída esperada:
```
3
```
