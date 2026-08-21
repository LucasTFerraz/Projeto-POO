# Exercício Básico — Aula 13

## Contexto

Em sala, `ComandoAvancar` moveu o robô na direção atual. Este exercício pede o oposto:
um comando que recua, sem deixar o robô "virado" ao final.

## Problema

Escreva `ComandoRecuar(passos)`: move o robô `passos` casas na direção **oposta** à
atual, mas devolve o robô com a **mesma direção** de antes ao final (o robô não fica
de costas — ele só anda pra trás e volta a "olhar" pra onde olhava).

## Exemplo

```python
robo1 = Robo("Wall-E", x=5, y=5)   # direção LESTE
ComandoRecuar(2).executar(robo1)
print(robo1.x, robo1.y, robo1.direcao)
```

Saída esperada:
```
3 5 Direcao.LESTE
```

## Dica

Guarde `robo.direcao` numa variável antes de mexer nela, use `Direcao.oposta()` (Aula
9) pra virar, chame `robo.avancar_n(passos)`, e devolva `robo.direcao` pro valor
original guardado no começo.
