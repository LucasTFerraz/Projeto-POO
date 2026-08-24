# Exercício Básico — Aula 14

## Contexto

Em sala, `ModoCarregando` recusou `mover()` e, à parte, foi recarregando a bateria a
cada `tick()`. Este exercício pede a versão mais simples possível de um modo: um que
só recusa `mover()`, sem fazer mais nada — nem recarregar, nem levantar exceção.

## Problema

Escreva `ModoPausado(ModoOperacao)`: sobrescreve `mover(self, robo)` para imprimir
`"{nome} está pausado, aguardando comando manual."` e devolver `False`, sem tocar em
nenhum outro atributo do robô.

## Exemplo

```python
robo1 = Robo("Wall-E", x=5, y=5)
robo1.modo = ModoPausado()
resultado = robo1.mover()
print(resultado)
```

Saída esperada:
```
Wall-E está pausado, aguardando comando manual.
False
```

## Dica

É a versão mais enxuta possível de `ModoOperacao` — só sobrescreva `mover()`, seguindo
a mesma estrutura de `ModoCarregando.mover()` vista em sala, mas sem o método
`carregar()`.
