# Exercício Médio — Aula 6

## Contexto

Vocês já viram atributo de classe (compartilhado, ex.: `LADO_GRADE`) e, hoje, `@property`
com setter validado. Este exercício combina os dois numa classe nova.

## Problema

Escreva a classe `Sensor`, com:
- um atributo de **classe** `TOTAL_SENSORES`, iniciado em `0`, incrementado a cada
  `Sensor(...)` criado;
- uma property `alcance`, cujo setter levanta `ValueError` se o valor não for
  estritamente positivo (`valor <= 0`).

## Exemplo

```python
s1 = Sensor(alcance=5)
s2 = Sensor(alcance=10)
print(Sensor.TOTAL_SENSORES)

try:
    s1.alcance = -3
except ValueError as erro:
    print(erro)
```

Saída esperada:
```
2
alcance=-3 deve ser positivo
```
