# Exercício Médio — Aula 3

## Contexto

`carregar_programa` lê o arquivo de comandos usando um `for` e `try/except` para pular linhas
mal formadas. Este exercício combina os dois conceitos centrais da aula de um jeito diferente:
percorrer a lista de linhas **recursivamente**, sem `for` nem `while`.

## Problema

Escreva `carregar_comandos_recursivo(linhas, indice=0)`, que recebe uma lista de strings (já
lidas do arquivo, uma por linha) e devolve a lista de comandos válidos como tuplas
`(acao, valor)` — na mesma ordem em que aparecem, ignorando linhas mal formadas e parando ao
encontrar `"PARAR"` ou o fim da lista.

Requisitos:
- Nenhum `for`/`while` — só recursão (`indice` avança a cada chamada).
- Cada linha deve ser parseada com `try/except` (`ValueError`/`IndexError`), igual ao
  `parsear_seguro` — se der erro, a linha é ignorada, mas a recursão continua para a próxima.
- Caso-base 1: `indice` chegou ao fim da lista.
- Caso-base 2: a linha atual é `"PARAR"` (ou vazia).

## Exemplo

```python
linhas = ["AVANCAR 3", "GIRAR ESQ", "AVANCAR 2", "GIRAR -1", "PARAR", "AVANCAR 9"]
print(carregar_comandos_recursivo(linhas))
```

Saída esperada:
```
[('AVANCAR', 3), ('AVANCAR', 2), ('GIRAR', -1)]
```

Note que `"GIRAR ESQ"` foi descartada (o `int("ESQ")` falha) e `"AVANCAR 9"`, que vem depois
do `"PARAR"`, nunca chega a ser processada.
