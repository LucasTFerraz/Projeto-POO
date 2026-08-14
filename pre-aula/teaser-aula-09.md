# Pré-aula 9 — Herança e composição

## O robô até aqui

`Posicao`, `Comando` e `Leitura` já são `@dataclass` — menos código, mesma promessa. A
direção do robô é um `Enum` (`Direcao`), com o vetor de movimento como valor e métodos
próprios de giro. Mas ainda existe só **um** tipo de robô: `Robo`, sozinho.

## O problema que vamos resolver

E se vocês precisassem de um robô que enxerga mais longe que o normal, ou de um robô mais
rápido — sem reescrever `Robo` inteiro do zero, e sem duplicar `nome`, `x`, `y` e todo o
resto que já funciona? Python tem, desde sempre, duas ferramentas clássicas de orientação a
objetos para variar um tipo sem repetir código. Hoje vocês usam as duas, no mesmo problema,
para sentir a diferença entre elas na prática.

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a declaração de `Direcao` como `Enum` (Aula 4):
os quatro membros e seus valores (vetores `(dx, dy)`). Depois, escreva de memória a
assinatura do método `virar_esquerda(self)` — não precisa acertar a lógica interna, só a
ideia de que ele devolve outro membro do próprio `Enum`. Compare com
`notas/notas-aula-08-solucao.ipynb`.

## Leitura opcional

- Herança (visão geral) — Tutorial oficial: https://docs.python.org/3/tutorial/classes.html#inheritance
- `super()` — documentação oficial: https://docs.python.org/3/library/functions.html#super
- Composição vs. herança — Real Python: https://realpython.com/inheritance-composition-python/
