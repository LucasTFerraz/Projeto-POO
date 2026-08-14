# Pré-aula 10 — Polimorfismo e delegação

## O robô até aqui

A família de robôs já existe: `RoboVeloz` e `RoboExplorador` (herança, sobrescrevendo
`avancar()`), e `Sensor`/`Radio` como peças que qualquer `Robo` **tem** (composição).
Cada jeito diferente de andar, até agora, significou criar uma classe nova.

## O problema que vamos resolver

Toda vez que um robô precisa andar de um jeito diferente, a solução até aqui foi a
mesma: escrever `class RoboAlgumaCoisa(Robo)` e sobrescrever `avancar()`. E se um
`Robo` comum — sem virar outro tipo, sem subclasse nenhuma — pudesse trocar de jeito
de andar no meio da execução, como quem troca uma peça? Hoje vocês veem duas ideias
que tornam isso possível: um mesmo comando respondendo de formas diferentes sem
checar "quem é você", e uma peça que decide, por fora, como o robô se move.

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a declaração de `RoboVeloz(Robo)`
sobrescrevendo `avancar()` (Aula 9) — o corpo do método, chamando `super().avancar()`
duas vezes. Depois, escreva de memória a linha, dentro de `Robo.__init__`, que compõe
um `Sensor` como peça do robô (`self.sensor = ...`). Compare com
`notas/notas-aula-09-solucao.ipynb`.

## Leitura opcional

- Duck typing (definição oficial) — glossário da documentação oficial: https://docs.python.org/3/glossary.html#term-duck-typing
- Classes e herança (revisão) — Tutorial oficial: https://docs.python.org/3/tutorial/classes.html
- Composição e delegação — Real Python: https://realpython.com/inheritance-composition-python/
