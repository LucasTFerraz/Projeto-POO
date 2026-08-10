# Exercício Médio — Aula 5

## Contexto

Hoje vimos que um atributo pode morar na classe (compartilhado por todos os objetos) ou na
instância (uma cópia por objeto), e que métodos podem combinar os dois. Este exercício pede
para juntar as duas ideias numa classe só.

## Problema

Adicione à classe `Robo` um atributo de **classe** chamado `POPULACAO`, iniciado em `0`, que
conta quantos robôs já foram criados (incremente ele dentro do `__init__`, toda vez que um novo
robô nasce). Depois, escreva o método de instância `colegas(self)`, que devolve quantos
**outros** robôs existem além dele mesmo (`POPULACAO - 1`).

## Exemplo

```python
r1 = Robo(nome="Alfa")
r2 = Robo(nome="Beta")
r3 = Robo(nome="Gama")

print(r1.colegas())
print(Robo.POPULACAO)
```

Saída esperada:
```
2
3
```
