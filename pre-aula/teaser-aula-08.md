# Pré-aula 8 — Dataclasses e enums

## O robô até aqui

`Posicao` e `Comando` já imprimem bem, comparam por valor e são construídos com
`__init__`, `__repr__` e `__eq__` — mas cada um desses três métodos foi escrito à
mão, campo por campo. `Robo.direcao` é uma `@property` que só aceita quatro strings
específicas, validadas por um `if`.

## O problema que vamos resolver

Toda classe nova de vocês — `Posicao` ontem, `Comando` antes disso — repete a mesma
receita: `__init__` copia parâmetro para atributo, `__repr__` monta um f-string,
`__eq__` compara campo a campo com `isinstance` na frente. Sempre o mesmo padrão,
sempre reescrito à mão. Existe um jeito de o Python escrever isso sozinho, só a
partir dos nomes e tipos dos campos?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a assinatura do `__eq__` defensivo de
`Posicao` (Aula 3): o que ele faz **antes** de comparar `x` e `y`? Depois, escreva de
memória por que `print([robo1])` usa `__repr__` mesmo se `Robo` tiver `__str__`
definido. Compare com `notas/notas-aula-07-solucao.ipynb`.

## Leitura opcional

- `dataclasses` (visão geral) — documentação oficial: https://docs.python.org/3/library/dataclasses.html
- `frozen`, `field`, `default_factory` — Real Python, Data Classes: https://realpython.com/python-data-classes/
- `enum` (visão geral) — documentação oficial: https://docs.python.org/3/library/enum.html
