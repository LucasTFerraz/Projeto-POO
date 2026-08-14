# Exercício Básico — Aula 8

## Contexto

Em sala, `Posicao` e `Comando` viraram `@dataclass` — poucas linhas, `__init__`/
`__repr__`/`__eq__` de graça. Este exercício pede a mesma técnica, num objeto novo
do domínio do robô: um `Motor`.

## Problema

Escreva a classe `Motor`, como dataclass, com:
- `potencia: int`;
- `ligado: bool = False` (desligado por padrão).

Sem `frozen` — `Motor` pode ligar/desligar depois de criado.

## Exemplo

```python
m1 = Motor(150)
m2 = Motor(150)
print(m1)
print(m1 == m2)

m1.ligado = True
print(m1)
```

Saída esperada:
```
Motor(potencia=150, ligado=False)
True
Motor(potencia=150, ligado=True)
```

## Dica

Não esqueça a anotação de tipo em cada campo (`: int`, `: bool`) — sem ela, o
`@dataclass` não reconhece o atributo como campo do `__init__`/`__repr__`.
