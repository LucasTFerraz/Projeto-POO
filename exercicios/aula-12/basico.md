# Exercício Básico — Aula 12

## Contexto

Em sala, `__getattr__` calculou `robo.leitura_<direção>` sob demanda — `True` quando
a próxima casa naquela direção está livre. Este exercício pede o oposto.

## Problema

Escreva `__getattr__` para que `robo.obstaculo_<direção>` devolva `True` quando a
próxima casa naquela direção está **bloqueada** (fora da grade **ou** tem obstáculo),
e `False` quando está livre — o inverso exato de `leitura_<direção>`. Guarde o
resultado num cache, do mesmo jeito que em sala.

## Exemplo

```python
robo1 = Robo(x=5, y=9, obstaculos={(6, 5): True})
print(robo1.obstaculo_norte)   # y=9 -> y+1=10, fora da grade
print(robo1.obstaculo_sul)     # y=9 -> y-1=8, livre
```

Saída esperada:
```
True
False
```

## Dica

Reaproveite a estrutura de `leitura_<direção>` quase inteira — só troca a condição
final: em vez de `livre = (0 <= nx < LADO_GRADE and ...)`, calcule `bloqueado = not
(0 <= nx < LADO_GRADE and ...) or (nx, ny) in self.obstaculos`.
