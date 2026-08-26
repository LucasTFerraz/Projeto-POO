# Exercício Básico — Aula 16

## Contexto

Em sala, cada preset de grade (`grade_vazia`, `grade_moldura`, `grade_labirinto`) é
uma função sem argumento que devolve um dicionário `{(x, y): True, ...}` novo a
cada chamada.

## Problema

Escreva `grade_diagonal()`: obstáculo em toda casa `(i, i)` para `i` de 0 a 9 (a
diagonal principal de uma grade 10×10). Acrescente ao `FABRICA_GRADES` com a chave
`"diagonal"` e recalcule `GRADES_VALIDAS`.

## Exemplo

```python
FABRICA_GRADES["diagonal"] = grade_diagonal
GRADES_VALIDAS = set(FABRICA_GRADES)

print(len(grade_diagonal()))
print((5, 5) in grade_diagonal())
```

Saída esperada:
```
10
True
```

## Dica

Um dict comprehension de uma linha: `{(i, i): True for i in range(10)}`.
