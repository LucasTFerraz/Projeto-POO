# Exercício Avançado — Aula 8

## Contexto

Um teste automatizado que compara "estado observado" com "estado esperado" costuma
comparar campo por campo, na mão — frágil, e a mensagem de erro raramente ajuda a
achar a diferença. `@dataclass` gera `__eq__` e `__repr__` de graça: comparar dois
estados vira uma linha, e o `__repr__` já aparece pronto pra debugar quando o teste
falha.

## Problema

Escreva `EstadoRobo` como dataclass `frozen=True`, com os campos `x: int`,
`y: int`, `direcao` (uma string, para simplificar) e `bateria: int`.

Escreva `verificar_estado(atual, esperado)`, que devolve `True` se `atual ==
esperado` (reaproveitando o `__eq__` gerado, sem comparar campo por campo). Se
forem diferentes, a função deve devolver `False` e **imprimir** quais campos
específicos divergem, no formato `"campo: valor_atual != valor_esperado"` — um por
linha, só os que realmente diferem.

## Exemplo

```python
atual = EstadoRobo(x=3, y=2, direcao="NORTE", bateria=80)
esperado = EstadoRobo(x=3, y=2, direcao="NORTE", bateria=100)

print(verificar_estado(atual, esperado))
```

Saída esperada:
```
bateria: 80 != 100
False
```

## Extensão — conexão com testes de software

Pesquise como `unittest.TestCase.assertEqual` e o `assert` do `pytest` tratam a
comparação de dois objetos com `__eq__`/`__repr__` gerados (por `@dataclass` ou por
bibliotecas como `attrs`/`pydantic`): por que a mensagem de erro desses frameworks,
ao comparar dois objetos assim, já mostra os dois `__repr__` lado a lado, sem você
escrever nada a mais? Que economia isso representa para quem escreve testes de
regressão de estado (comparar "estado antes" com "estado depois" de uma operação)?
