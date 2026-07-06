# Pré-aula 2 — Coleções e funções: o robô estruturado

## O robô até aqui

O robô v2 lê uma lista de comandos como `"AVANCAR 3"` e `"GIRAR ESQ"` e executa um a um,
checando a parede antes de cada avanço. Ele decide, se movimenta e para sozinho quando o
programa acaba.

## O problema que vamos resolver

Só que olhando o código de perto: a checagem "cabe na grade?" aparece **quatro vezes** — uma
para cada direção (leste, oeste, norte, sul) — e o comando `GIRAR` é uma cascata de 8 `if`/`elif`
para cobrir as quatro direções nos dois sentidos. Se alguém quiser adicionar uma quinta direção,
vai precisar tocar em 8 lugares diferentes. Como organizar os dados do robô e essa lógica de
decisão para que adicionar algo novo custe **uma linha**, não oito?

## Aquecimento (5 min — faça antes de entrar na sala)

Escreva **de memória** a linha (ou duas) que transforma o texto `"AVANCAR 3"` em ação e valor
separados, prontos para usar — sem consultar o código da Aula 1.

Dica de formato: o resultado deve deixar você com uma string `"AVANCAR"` e um inteiro `3`,
prontos para comparar e somar.

Sem consultar o código. O objetivo é ativar a memória, não avaliar.

## Leitura opcional

- **Dicionários:** https://www.w3schools.com/python/python_dictionaries.asp
- **Listas aninhadas (matrizes 2D):** https://realpython.com/python-lists-tuples/
- **Funções — definição, parâmetros, retorno:** https://www.w3schools.com/python/python_functions.asp
