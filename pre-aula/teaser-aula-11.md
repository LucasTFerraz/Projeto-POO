# Pré-aula 11 — Descriptors

## O robô até aqui

`Robo` já tem `x`, `y`, `bateria` e `direcao` como `@property` validada, `mover()`
delegando para `self.estrategia` (Padrão ou Esquiva), `Sensor`/`Radio` como peças
compostas, e a família `RoboVeloz`/`RoboExplorador` por herança.

## O problema que vamos resolver

`x` e `y` têm cada um seu próprio `@property`/`@x.setter` desde a Aula 6 — e a
validação dos dois (`0 <= valor < LADO_GRADE`) é **idêntica**, uma cópia da outra com
o nome trocado. Se amanhã a regra da grade mudar, alguém precisa lembrar de mudar nos
dois lugares — esquecer um deles não dá erro nenhum, só um bug silencioso. E se
existisse um jeito de escrever essa validação **uma vez só** e usá-la em quantos
atributos quiser, em quantas classes quiser?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória o método `mover(self, robo)` de
`EstrategiaEsquiva` (Aula 10) — o `while` que gira antes de desistir, seguido do
`avancar()`. Compare com `notas/notas-aula-10-solucao.ipynb`.

## Leitura opcional

- Descriptor HowTo Guide (visão geral, com exemplos) — documentação oficial: https://docs.python.org/3/howto/descriptor.html
- Protocolo de descriptors (`__get__`, `__set__`, `__set_name__`) — referência oficial do modelo de dados: https://docs.python.org/3/reference/datamodel.html#implementing-descriptors
- Descriptors na prática, com exemplos comentados — Real Python: https://realpython.com/python-descriptors/
