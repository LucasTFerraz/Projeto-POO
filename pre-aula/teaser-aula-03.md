# Pré-aula 3 — Recursão, exceções e arquivos: o robô autônomo

## O robô até aqui

O robô v4 tem seu estado organizado num dicionário (`robo['x']`, `robo['obstaculos']`, ...) e
um conjunto de funções — `avancar`, `girar`, `sensor_frente`, `executar` — que recebem `robo`
como primeiro argumento e executam uma sequência de comandos que você escreve na mão.

## O problema que vamos resolver

Duas perguntas que o v4 ainda não sabe responder. Primeira: sem mover o robô, como saber
quantas células ele consegue alcançar a partir de onde está, sem bater em obstáculo? Segunda:
se o programa do robô vier de um arquivo de texto — escrito por outra pessoa, com chance de
erro de digitação — o que acontece quando uma linha vem mal formatada? O programa deveria
travar, ou existe um jeito do robô lidar com isso e continuar?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar o notebook da Aula 2, escreva **de memória** a função `avancar(robo, obstaculos)`
completa (as poucas linhas que você escreveu naquela aula — pode usar `sensor_frente` como
parte da resposta, sem reescrevê-la). O objetivo é ativar a memória, não acertar de primeira.

## Leitura opcional

- **Recursão — introdução visual:** https://realpython.com/python-recursion/ (leia até "Thinking Recursively")
- **Exceções — tutorial oficial:** https://docs.python.org/3/tutorial/errors.html (seções 8.3 e 8.4)
- **Arquivos — tutorial oficial:** https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
