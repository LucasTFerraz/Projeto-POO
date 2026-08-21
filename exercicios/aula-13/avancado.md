# Exercício Avançado — Aula 13

## Contexto

Na Aula 12, `checar_invariante` testou que um descriptor sempre respeitava uma regra
(valores inválidos recusados, válidos aceitos). Este exercício traz a mesma ideia para
hoje: em vez de checar um único robô à mão depois de rodar uma sequência de comandos,
uma função verifica automaticamente que uma **propriedade** continua valendo para
**toda** uma frota, depois de executar os mesmos comandos em cada robô.

## Problema

Escreva `verificar_invariante_frota(configs, comandos, invariante)`:

1. Monta uma frota com `criar_robo_configurado`, um robô por item de `configs`.
2. Executa a mesma lista `comandos` (strings) em cada robô da frota.
3. Para cada robô, depois de executar os comandos, chama `invariante(robo)` — uma
   função que devolve `True` (propriedade respeitada) ou `False` (violada).
4. Devolve uma lista com o `nome` de todo robô cuja `invariante` devolveu `False`.
   Lista vazia = todos passaram.

## Exemplo

```python
def dentro_da_grade(robo):
    return 0 <= robo.x < Robo.LADO_GRADE and 0 <= robo.y < Robo.LADO_GRADE

configs = [
    {"tipo_nome": "RoboVeloz", "nome": "a"},
    {"tipo_nome": "RoboExplorador", "nome": "b"},
]
falhas = verificar_invariante_frota(
    configs, ["AVANCAR 3", "GIRAR ESQ", "AVANCAR 2"], dentro_da_grade
)
print(falhas)
```

Saída esperada:
```
[]
```

## Extensão — conexão com testes de software

`verificar_invariante_frota` é o mesmo princípio de teste baseado em propriedades da
Aula 12 (`hypothesis`), aplicado a um cenário de **integração**: em vez de testar uma
classe isolada, testa um comportamento (a sequência de comandos) contra **todas** as
variações de robô que a fábrica sabe criar — de uma vez, sem escrever um teste por
classe. Se amanhã a turma adicionar `RoboSubmarino` ao catálogo, essa mesma função já
testa o invariante nele também, sem precisar de nenhuma linha nova. Pesquise o que
frameworks de teste chamam de *parametrized tests* (`pytest.mark.parametrize`,
documentação oficial: https://docs.pytest.org/en/stable/how-to/parametrize.html) — é
a versão "de verdade", com relatório e integração de CI, da mesma ideia que vocês
acabaram de escrever à mão.
