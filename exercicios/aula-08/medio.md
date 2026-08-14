# Exercício Médio — Aula 8

## Contexto

Vocês já viram `Enum` (`Direcao`, com vetor de movimento como valor) e `@dataclass`
(`Posicao`, `Comando`, `Leitura`). Este exercício combina os dois: um `Enum` usado
como **campo** de uma dataclass.

## Problema

Escreva `TipoObstaculo` como `Enum`, com três membros: `PAREDE`, `BURACO`, `ROBO`.

Escreva `ObstaculoDetectado` como dataclass `frozen=True`, com:
- `posicao: tuple`;
- `tipo: TipoObstaculo`.

O `__eq__` gerado deve considerar dois `ObstaculoDetectado` iguais só se a posição
**e** o tipo baterem (reaproveite o `__eq__` gerado — não escreva um na mão).

## Exemplo

```python
o1 = ObstaculoDetectado((3, 3), TipoObstaculo.PAREDE)
o2 = ObstaculoDetectado((3, 3), TipoObstaculo.PAREDE)
o3 = ObstaculoDetectado((3, 3), TipoObstaculo.BURACO)

print(o1)
print(o1 == o2)
print(o1 == o3)
```

Saída esperada:
```
ObstaculoDetectado(posicao=(3, 3), tipo=<TipoObstaculo.PAREDE: 1>)
True
False
```
