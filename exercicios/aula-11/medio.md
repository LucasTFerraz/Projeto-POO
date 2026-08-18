# Exercício Médio — Aula 11

## Contexto

Vocês viram que todo atributo mora num `__dict__`, e que um descriptor decide o que
fazer com leitura/escrita nesse `__dict__`. `Percentual` guarda só o valor atual de
`Robo.bateria`. Este exercício pede um descriptor que guarda o valor atual **e**
lembra de todos os valores anteriores — combinando as duas ideias: o `__dict__` da
instância vira o lugar de duas chaves diferentes, não só uma.

## Problema

Escreva `Historico`, um descriptor com a mesma regra de `Percentual` (`clamp` entre 0
e 100, nunca levanta erro) que também guarda, em uma lista à parte, todo valor já
atribuído (incluindo o valor inicial do `__init__`). `__set_name__` deve derivar
**dois** nomes internos a partir do nome público: um para o valor atual (`"_" + name`,
igual a `Percentual`) e outro para a lista de histórico (`"_" + name + "_historico"`).
Acrescente um método `valores(self, instance)` que devolve a lista de histórico
daquela instância (uma cópia, não a lista original).

`Robo.bateria` deve usar `Historico` no lugar de `Percentual`.

## Exemplo

```python
robo1 = Robo("Wall-E", bateria=150)
robo1.bateria = 40
robo1.bateria = -10
print(robo1.bateria)
print(type(Robo.bateria).__name__)
print(Robo.bateria.valores(robo1))
```

Saída esperada:
```
0
Historico
[100, 40, 0]
```

(Repare: `150` já entra na lista como `100`, porque o `clamp` roda antes de guardar —
o histórico registra o valor **depois** de ajustado, não o que foi passado.)
