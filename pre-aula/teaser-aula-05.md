# Pré-aula 5 — Classes e objetos

## O robô até aqui

O robô v6 já faz tudo que ele vai fazer como script solto: decide para onde ir, navega numa
grade com obstáculos, lê seu programa de um arquivo e grava onde passou. Cada pedaço desse
comportamento (`avancar`, `girar`, `sensor_frente`, `executar`) é uma função separada, e toda
elas recebem o robô — um dicionário com `x`, `y`, `direcao` — como primeiro argumento.

## O problema que vamos resolver

Toda função do robô recebe `robo` como primeiro parâmetro, sempre. E se, num programa maior,
dois robôs existissem ao mesmo tempo e alguém confundisse qual `robo` passar para qual função?
O Python tem, desde o início da linguagem, um jeito de amarrar dado e comportamento numa coisa
só, para que essa confusão nem seja possível de escrever. Hoje vocês veem qual é — e por que
Python escreve isso de um jeito que chama atenção de quem já programou em Java, C++ ou C#.

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória duas formas de obter, a partir do `log` da Aula 4, a
lista dos comandos que começam com `"AVANCAR"`: uma usando list comprehension com filtro, outra
usando `filter` com uma `lambda`. Não precisa rodar — só escrever, e comparar depois com
`notas/notas-aula-04-solucao.ipynb`.

## Leitura opcional

- Classes e objetos (fundamentos) — Tutorial oficial: https://docs.python.org/3/tutorial/classes.html
- Por que `self` é explícito em Python — Real Python: https://realpython.com/python-self-variable/
