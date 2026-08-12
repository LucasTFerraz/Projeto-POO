# Exercício Avançado — Aula 7

## Contexto

Testar um robô autônomo costuma envolver checar duas coisas contra uma trajetória
registrada: "ele nunca bateu num obstáculo?" e "ele terminou onde devia?". As duas
perguntas dependem de comparar posições — exatamente o que `Posicao.__eq__` e
`Grade.__getitem__`/`__contains__` (vistos em sala) fazem.

## Problema

Escreva a função `valida_trajetoria(pontos, grade)`, que recebe uma lista de
`Posicao` (a trajetória registrada de um robô) e uma `Grade` (com `__contains__`
sobre `self.obstaculos`), e devolve a **primeira** `Posicao` da lista que colide com
um obstáculo da grade — comparando com `(p.x, p.y) in grade` — ou `None` se a
trajetória inteira for livre de colisões.

Depois, escreva `trajetorias_equivalentes(pontos_a, pontos_b)`, que devolve `True`
se as duas listas de `Posicao` tiverem o mesmo comprimento e cada par de posições
correspondentes for igual (reaproveitando `Posicao.__eq__`, sem comparar `x`/`y` na
mão) — o "oráculo" que decide se uma trajetória observada bate com a esperada.

## Exemplo

```python
grade = Grade(5, {(2, 2): True})
trajetoria = [Posicao(0, 0), Posicao(1, 0), Posicao(2, 0), Posicao(2, 2)]

print(valida_trajetoria(trajetoria, grade))
print(valida_trajetoria([Posicao(0, 0), Posicao(1, 0)], grade))

esperada = [Posicao(0, 0), Posicao(1, 0)]
observada = [Posicao(0, 0), Posicao(1, 0)]
print(trajetorias_equivalentes(esperada, observada))
```

Saída esperada:
```
Posicao(2, 2)
None
True
```

## Extensão — conexão com testes de software

`trajetorias_equivalentes` é, na prática, um **oráculo de teste**: uma função que
decide se um resultado observado bate com o esperado, sem exigir que o teste compare
atributo por atributo. Pesquise como frameworks de teste (ex.: `pytest`, `unittest`)
usam `__eq__` de objetos customizados dentro de `assert resultado == esperado` — e
por que isso é preferível a escrever um `assert` gigante comparando cada campo na
mão.
