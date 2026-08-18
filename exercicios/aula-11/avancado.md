# Exercício Avançado — Aula 11

## Contexto

Um descriptor como `Coordenada` ou `PositivoEstrito` promete uma coisa: "para todo
valor fora da regra, `__set__` levanta um erro; para todo valor dentro da regra, não
levanta". Isso é um **invariante** — e invariantes são exatamente o que testes
automatizados existem para checar, sem depender de alguém lembrar de testar cada caso
à mão toda vez que a classe mudar.

## Problema

Escreva `checar_invariante(classe, nome_atributo, valores_invalidos, valores_validos,
**kwargs_construtor)`. A função deve:

1. Para cada valor em `valores_invalidos`: criar uma instância de `classe` (passando
   `**kwargs_construtor` mais `{nome_atributo: valor}`) e confirmar que a criação
   levanta `ValueError`. Se **não** levantar, é uma falha do invariante.
2. Para cada valor em `valores_validos`: criar a instância do mesmo jeito e confirmar
   que **não** levanta exceção nenhuma, e que `getattr(instancia, nome_atributo)`
   devolve exatamente o valor passado (sem `clamp` silencioso). Se levantar, ou se o
   valor guardado for diferente do esperado, também é uma falha.

A função deve devolver uma lista de strings, uma por falha encontrada (formato livre,
mas deve identificar o valor e o motivo). Lista vazia = invariante confirmado.

## Exemplo

```python
class Robo:
    x = Coordenada(0, 10)

    def __init__(self, nome, x=0):
        self.nome = nome
        self.x = x

falhas = checar_invariante(
    Robo, "x",
    valores_invalidos=[-1, 10, 99],
    valores_validos=[0, 5, 9],
    nome="TesteBot",
)
for f in falhas:
    print(f)
print(len(falhas))
```

Saída esperada (para uma `Coordenada` implementada corretamente):
```
0
```

## Extensão — conexão com testes de software

`checar_invariante` é uma versão manual e simplificada de **teste baseado em
propriedades** (*property-based testing*): em vez de escrever um caso de teste por
valor (`assert Robo(x=-1)` levanta erro, `assert Robo(x=10)` levanta erro, ...), você
declara a propriedade ("todo valor fora do intervalo levanta `ValueError`") e o teste
verifica vários valores contra ela de uma vez. Pesquise a biblioteca `hypothesis`
(documentação oficial: https://hypothesis.readthedocs.io/) — ela gera automaticamente
centenas de valores de teste (incluindo casos extremos que ninguém pensaria em
escrever à mão) para checar exatamente esse tipo de invariante. Por que isso é mais
forte do que uma lista fixa de `valores_invalidos`/`valores_validos` escrita à mão?
