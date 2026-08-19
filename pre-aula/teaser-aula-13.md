# Pré-aula 13 — Design Patterns I

## O robô até aqui

`Robo` já calcula leituras de sensor sob demanda, audita toda mudança de estado, e toda
subclasse — `RoboVeloz`, `RoboExplorador`, `RoboBlindado` — se registra sozinha num
catálogo assim que é definida, sem lista mantida à mão.

## O problema que vamos resolver

Hoje, trocar a forma como o robô se move ou monta a fila de comandos ainda exige mexer
dentro da classe `Robo`. E se desse pra trocar **o comportamento inteiro** de navegação
só trocando um objeto guardado, sem tocar em `Robo` nenhuma vez? E se cada comando —
"AVANCAR 3", "GIRAR ESQ" — deixasse de ser texto reinterpretado toda vez e virasse algo
que dá pra guardar, comparar e **reexecutar** depois, em outro robô, sem reparsear nada?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a assinatura de `__init_subclass__` que
`Robo` usa (Aula 12) e o que `Robo._registro` guarda. Compare com
`notas/notas-aula-12-solucao.ipynb`.

## Leitura opcional

- Strategy Pattern — Refactoring.Guru: https://refactoring.guru/design-patterns/strategy
- Command Pattern — Refactoring.Guru: https://refactoring.guru/design-patterns/command
- Factory Method / Simple Factory — Refactoring.Guru: https://refactoring.guru/design-patterns/factory-method
