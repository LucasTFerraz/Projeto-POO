# Pré-aula 4 — Python idiomático

## O robô até aqui

O robô v6 já faz tudo que ele vai fazer nesta disciplina: lê um programa de um arquivo de texto,
executa os comandos tratando erros sem quebrar, e grava num log **onde** ele passou — posição,
comando e se bateu na parede em cada passo.

## O problema que vamos resolver

O robô funciona. Mas será que o código que escrevemos parece Python, ou parece Java/C traduzido
palavra por palavra para outra sintaxe? Hoje não escrevemos nenhuma versão nova do robô — usamos
o log que ele já gera para aprender a escrever o mesmo tipo de lógica de um jeito mais curto, mais
claro, e mais fácil de outro Python dev reconhecer de cara. Pergunta para guardar: dado o log de
9 passos do robô, quantas linhas de código vocês acham que precisam para descobrir a célula que
ele mais visitou? Guardem o palpite — a resposta de hoje vai surpreender.

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código nenhum, escreva de memória a função `parsear_seguro(linha)` da Aula 3: ela
recebe uma linha como `"AVANCAR 3"`, tenta separar em ação e valor, converte o valor para `int`,
e captura os dois tipos de erro que podem acontecer numa linha mal formatada (um deles é o de
"faltou uma parte da linha"; o outro é o de "essa parte não é um número"). Não precisa rodar —
só escrever no papel ou num arquivo, de memória, e comparar depois com o `solucao/aula03/`.

## Leitura opcional

- List/tuple/dict comprehensions e generator expressions — Tutorial oficial:
  https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- `*args`/`**kwargs` — Tutorial oficial (argumentos arbitrários):
  https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
- `map`/`filter` — documentação oficial: https://docs.python.org/3/library/functions.html#map
