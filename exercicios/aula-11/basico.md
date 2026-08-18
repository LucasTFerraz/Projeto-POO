# Exercício Básico — Aula 11

## Contexto

Em sala, `NaoNegativo` recusou `Sensor.alcance` menor que zero. `Robo.velocidade`
tem uma regra parecida, mas um pouco mais estrita: zero também não faz sentido — um
robô com `velocidade = 0` não anda.

## Problema

Escreva `PositivoEstrito`, um descriptor que recusa valores **menores ou iguais a
zero** (não só negativos), levantando
`ValueError(f"{nome} precisa ser maior que zero, recebi {valor}")`. Use-o em
`Robo.velocidade`.

## Exemplo

```python
class Robo:
    velocidade = PositivoEstrito()

    def __init__(self, velocidade=1):
        self.velocidade = velocidade

robo1 = Robo(2)
print(robo1.velocidade)
robo1.velocidade = 0
```

Saída esperada:
```
2
ValueError: velocidade precisa ser maior que zero, recebi 0
```

## Dica

Copie a estrutura de `NaoNegativo` (mesmos quatro métodos: `__set_name__`,
`__get__`, `__set__`); só troca a condição de `valor < 0` para `valor <= 0`.
