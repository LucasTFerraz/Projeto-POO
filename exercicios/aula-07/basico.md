# Exercício Básico — Aula 7

## Contexto

Em sala, `Posicao` ganhou `__repr__` (representação para programador) e `Comando`
ganhou `__repr__`/`__str__` como exercício. Este exercício pede a mesma técnica, num
objeto novo do domínio do robô: um `Sensor`.

## Problema

Escreva a classe `Sensor`, com atributos `nome` e `alcance`, e:
- `__repr__`, no formato `Sensor('frente', 5)` (use `!r` no nome, para bater com a
  convenção "dá para copiar e colar de volta");
- `__str__`, no formato `"frente (alcance 5)"` — a versão legível.

## Exemplo

```python
s = Sensor("frente", 5)
print(repr(s))
print(s)
print([s])
```

Saída esperada:
```
Sensor('frente', 5)
frente (alcance 5)
[Sensor('frente', 5)]
```

## Dica

A última linha (`print([s])`) é a pegadinha: dentro de uma lista, o Python usa
`__repr__`, não `__str__` — mesmo que os dois estejam definidos. Confira o cheat
sheet, seção "dois níveis de representação".
