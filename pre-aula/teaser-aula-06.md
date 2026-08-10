# Pré-aula 6 — Encapsulamento e properties

## O robô até aqui

O robô já é um objeto de verdade: `class Robo`, com `__init__`, atributos de instância e
todo o comportamento — `avancar`, `girar`, `sensor_frente` — como método. `self` já não é
mistério: é o mesmo `robo` que vocês passavam à mão antes, só que a linguagem passa ele
sozinho em toda chamada por ponto.

## O problema que vamos resolver

Hoje, nada impede `robo1.x = 999` ou `robo1.bateria = -50`. Amarramos dado e comportamento
num objeto só, mas o dado continua exposto, sem porteiro nenhum. Se um teste automatizado,
sem querer, colocasse o robô numa posição impossível, quem perceberia? Pergunta para
guardar: existe um jeito de proteger um atributo em Python sem trocar `robo.x` por
`robo.get_x()` em todo lugar do código?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a prova de que `self` é passado automaticamente:
duas formas de chamar o mesmo método de um objeto (por exemplo `relatorio()` da
`Bateria`) que dão exatamente o mesmo resultado — uma escrita como `objeto.metodo()`,
outra escrita como `Classe.metodo(objeto)`. Compare depois com
`notas/notas-aula-05-solucao.ipynb`.

## Leitura opcional

- Encapsulamento e a convenção de underscore — PEP 8: https://peps.python.org/pep-0008/#descriptive-naming-styles
- `@property` (fundamentos) — Tutorial oficial: https://docs.python.org/3/library/functions.html#property
