# Pré-aula 15 — Variabilidade e Linha de Produtos de Software

## O robô até aqui

`Robo` já tem uma família inteira de variantes — três tipos (`RoboVeloz`,
`RoboExplorador`, `RoboBlindado`), três estratégias de navegação, observadores que
se plugam ou não, dois modos de operação. Tudo isso combinado dá dezenas de robôs
diferentes, todos vindos do mesmo código.

## O problema que vamos resolver

Nem toda combinação faz sentido. Um robô blindado, pesado, fazendo zigue-zague
brusco é uma péssima ideia de engenharia — mas nada no código de hoje impede
alguém de criar exatamente essa combinação. E se existisse uma peça que
**garantisse**, antes de qualquer robô nascer, que só combinações válidas saem da
fábrica?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória o que `MonitorBateria.atualizar` faz 
e por que ele troca `robo.modo` sozinho, sem ninguém chamar `tick()`.
Compare com `notas/notas-aula-14-solucao.ipynb`.

## Leitura opcional

- Software Product Line — Wikipedia: https://en.wikipedia.org/wiki/Software_product_line
- Feature model — Wikipedia: https://en.wikipedia.org/wiki/Feature_model
