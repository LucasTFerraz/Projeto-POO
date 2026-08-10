# Exercício Avançado — Aula 5

## Contexto

Hoje o robô ganhou atributos livres: `robo1.x = 999` funciona sem protesto nenhum, mesmo sendo
um valor absurdo. Em testes de software, é comum escrever uma função auxiliar de asserção —
um "checador de invariantes" — que recebe um objeto depois de uma sequência de operações e
devolve tudo que está fora do esperado, sem travar o programa no meio do caminho. É esse tipo
de função que este exercício pede.

## Problema

Escreva `validar_estado_robo(robo, lado_grade=10)`, que recebe um objeto `Robo` (com atributos
`x`, `y`, `direcao`, `bateria`) e devolve uma **lista de strings**, uma para cada invariante
violado:
- `x` fora de `[0, lado_grade)` → `f"x fora da grade: {robo.x}"`
- `y` fora de `[0, lado_grade)` → `f"y fora da grade: {robo.y}"`
- `direcao` fora de `{"LESTE", "NORTE", "OESTE", "SUL"}` → `f"direcao invalida: {robo.direcao}"`
- `bateria` fora de `[0, 100]` → `f"bateria fora do intervalo: {robo.bateria}"`

Se nenhum invariante for violado, devolva a lista vazia.

## Exemplo

```python
robo = Robo(x=3, y=4, direcao="NORTE", bateria=50)
print(validar_estado_robo(robo))

robo.x = 999
robo.bateria = -10
print(validar_estado_robo(robo))
```

Saída esperada:
```
[]
['x fora da grade: 999', 'bateria fora do intervalo: -10']
```

## Extensão — conexão com testes de software

`validar_estado_robo` é, na prática, um *assertion helper*: uma função reutilizável que
centraliza as regras de "estado válido" de um objeto, em vez de espalhar `assert`s soltos por
cada teste. Pesquise: em frameworks de teste como `pytest`, como um assertion helper desse
tipo costuma ser usado dentro de um teste (`def test_algo(): ...`)? E por que devolver uma
**lista de erros** costuma ser preferível a lançar uma exceção na primeira violação encontrada?
