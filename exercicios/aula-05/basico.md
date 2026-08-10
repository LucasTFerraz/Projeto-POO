# Exercício Básico — Aula 5

## Contexto

Em sala, a classe `Robo` ganhou o método `avancar(self)`, que move o robô um passo na direção
atual usando a tabela `DELTAS`:
```python
class Robo:
    DELTAS = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}

    def __init__(self, x=0, y=0, direcao="LESTE"):
        self.x = x
        self.y = y
        self.direcao = direcao

    def avancar(self):
        dx, dy = Robo.DELTAS[self.direcao]
        self.x += dx
        self.y += dy
```

## Problema

Adicione à classe `Robo` o método `anda_atras(self)`, que move o robô um passo na direção
**contrária** à atual, **sem** girar (a `direcao` do robô não muda).

## Exemplo

```python
robo = Robo(x=5, y=5, direcao="NORTE")
robo.anda_atras()
print(robo.x, robo.y, robo.direcao)
```

Saída esperada:
```
5 4 NORTE
```

## Dica

É a mesma conta de `avancar`, só que subtraindo `dx`/`dy` em vez de somar — o delta da
direção atual continua sendo a referência, só o sinal inverte.
