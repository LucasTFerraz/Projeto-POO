# Pré-aula 12 — Metaprogramação

## O robô até aqui

`Robo` já tem `x`/`y` (grade) e `bateria` (percentual) validados por descriptors
reutilizáveis, `direcao` como `@property`, `Sensor`/`Radio` como peças compostas, e a
família `RoboVeloz`/`RoboExplorador` por herança. Todo atributo mora num `__dict__`,
e todo mundo já sabe onde intervir para validar leitura e escrita.

## O problema que vamos resolver

Até agora, todo atributo do robô existe desde o `__init__` — mesmo os que ninguém usa
na maior parte do tempo. E se um atributo só devesse aparecer quando alguém
**pergunta** por ele, calculado na hora, em vez de sempre? E se, toda vez que a turma
criar um tipo novo de robô, ele aparecesse sozinho num catálogo — sem ninguém lembrar
de atualizar lista nenhuma?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória os quatro métodos da classe `Coordenada`
(Aula 11): `__init__`, `__set_name__`, `__get__`, `__set__`. Compare com
`notas/notas-aula-11-solucao.ipynb`.

## Leitura opcional

- Módulos (tutorial completo) — documentação oficial: https://docs.python.org/3/tutorial/modules.html
- Customização de acesso a atributo (`__getattr__`, `__setattr__`) — referência oficial do modelo de dados: https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access
- `__init_subclass__` — referência oficial do modelo de dados: https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__
