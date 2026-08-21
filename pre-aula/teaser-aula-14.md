# Pré-aula 14 — Design Patterns II: Observer e State

## O robô até aqui

`Robo` já troca de comportamento de navegação sem ninguém tocar na classe (Strategy),
guarda cada comando como objeto reexecutável (Command), e sabe se criar sozinho a
partir só de um nome (Factory). Mas ele ainda é passivo: alguém sempre precisa
**perguntar** — `robo.bateria_critica`, checar se bateu numa parede — nada acontece
por conta própria.

## O problema que vamos resolver

E se o robô pudesse **avisar sozinho** quando algo relevante acontece, sem ninguém
ficar checando em loop? E se ele tivesse **modos de operação** — explorando,
carregando — e o comportamento inteiro mudasse dependendo do modo atual, sem um `if`
gigante espalhado por todo método sensível a estado?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a assinatura de `criar_robo_configurado`
(Aula 13) e o que ela faz com `FABRICA_ESTRATEGIAS`. Compare com
`notas/notas-aula-13-solucao.ipynb`.

## Leitura opcional

- Observer Pattern — Refactoring.Guru: https://refactoring.guru/design-patterns/observer
- State Pattern — Refactoring.Guru: https://refactoring.guru/design-patterns/state
