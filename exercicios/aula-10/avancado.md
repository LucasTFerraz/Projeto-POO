# Exercício Avançado — Aula 10

## Contexto

Hoje vimos que duck typing não checa contrato nenhum em tempo de definição: uma
"estratégia" pode esquecer o parâmetro `robo`, ou pode ser passada como classe em vez
de instância (`self.estrategia = EstrategiaPadrao`, sem os parênteses) — e o erro só
aparece quando alguém chama `mover()` de verdade, em produção. Em testes de software,
checar isso **antes** de usar um objeto plugável de verdade é uma prática comum:
validação de contrato (às vezes chamada de *smoke test* de plugin).

`hasattr(objeto, "nome_atributo")` devolve `True` se o objeto tem esse atributo/método;
`callable(x)` devolve `True` se `x` pode ser chamado como função (útil para distinguir
uma instância de uma classe não-instanciada).

## Problema

Escreva `valida_estrategia(estrategia)`, que devolve `True` só se `estrategia`
sobreviver a duas checagens: (1) tem um atributo `mover` que é `callable`; (2) chamar
`estrategia.mover(robo_falso)` — usando um `Robo` comum qualquer como robô de teste —
não levanta `TypeError` nem `AttributeError`. Capture as duas exceções e devolva
`False` se alguma ocorrer; devolva `True` caso a chamada complete normalmente
(não importa o valor de retorno).

Depois, escreva `relatorio_estrategias(lista_de_candidatos)`, que recebe uma lista de
objetos candidatos a estratégia e imprime, para cada um, `"OK"` ou `"QUEBRADA"`
conforme `valida_estrategia`.

## Exemplo

```python
class EstrategiaSemRobo:
    def mover(self):              # esqueceu o parâmetro robo
        return True

candidatos = [
    EstrategiaPadrao(),
    EstrategiaEsquiva(),
    EstrategiaPadrao,             # esqueceu de instanciar (classe, não objeto)
    EstrategiaSemRobo(),
    "não sou uma estratégia",
]

relatorio_estrategias(candidatos)
```

Saída esperada:
```
OK
OK
QUEBRADA
QUEBRADA
QUEBRADA
```

## Extensão — conexão com testes de software

`valida_estrategia` é um *smoke test* de plugin: antes de aceitar um objeto
duck-typed num sistema de produção (aqui, antes de aceitar uma nova `estrategia` no
robô), o teste confirma que ele tem a cara certa **e** que sobrevive a uma chamada
mínima, sem esperar até o robô real bater num obstáculo às 3h da manhã para descobrir
o bug. Pesquise sobre `typing.Protocol` (documentação oficial:
https://docs.python.org/3/library/typing.html#typing.Protocol) — uma forma de
declarar esse mesmo contrato duck-typed de um jeito que ferramentas como `mypy`
conseguem checar **antes** de rodar o código, sem exigir herança de nenhuma classe
comum. Por que isso é diferente de simplesmente criar uma classe abstrata
(`ABC`) da qual toda estratégia teria que herdar?
