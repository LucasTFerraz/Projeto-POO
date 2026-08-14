# Exercício Básico — Aula 9

## Contexto

Em sala, `RoboVeloz(Robo)` estendeu `avancar()` chamando `super().avancar()` duas vezes,
para andar sempre 2 casas de uma vez. Este exercício pede uma variação direta: em vez de
andar mais rápido, o robô andará mais devagar.

## Problema

Escreva `RoboLento(Robo)`, que sobrescreve `avancar()` para só se mover de fato a **cada
duas chamadas** — a primeira chamada não move (só conta), a segunda move de verdade, a
terceira não move, e assim por diante. Use um atributo de instância (por exemplo,
`self.chamadas`) para contar.

## Exemplo

```python
r = RoboLento("Tartaruga")
r.avancar()   # não move
print(r.x)
r.avancar()   # move
print(r.x)
r.avancar()   # não move
print(r.x)
```

Saída esperada:
```
0
1
1
```

## Dica

No `__init__`, acrescente `self.chamadas = 0` (depois de chamar `super().__init__`).
Em `avancar()`, incremente `self.chamadas` primeiro; só chame `super().avancar()` quando
`self.chamadas` for par.
