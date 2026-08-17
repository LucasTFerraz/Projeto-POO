# Exercício Básico — Aula 10

## Contexto

Em sala, `quantos_avancaram(lista)` chamou `.mover()` em cada objeto e contou quantos
devolveram `True` — sem `isinstance` nenhum. Este exercício pede o inverso: contar
quantos **não** avançaram.

## Problema

Escreva `quantos_pararam(lista)`, que chama `.mover()` em cada objeto de `lista` e
devolve quantos objetos devolveram `False`. Não use `isinstance` em lugar nenhum —
funcione para qualquer objeto que tenha `.mover()`, seja `Robo`/subclasse, seja
duck-typed.

## Exemplo

```python
class RoboBloqueado:
    def mover(self):
        return False

lista = [Robo("A"), RoboBloqueado(), RoboBloqueado()]
print(quantos_pararam(lista))
```

Saída esperada:
```
2
```

## Dica

Mesma estrutura de `quantos_avancaram`, só troca a condição: em vez de
`if objeto.mover():`, use `if not objeto.mover():`.
