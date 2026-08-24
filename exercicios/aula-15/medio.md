# Exercício Médio — Aula 15

## Contexto

Em sala, `validar_configuracao` checou uma configuração por vez. Este exercício
combina isso com iteração sobre uma coleção: checar uma **frota inteira** de
configurações de uma vez, separando as válidas das inválidas — sem parar no
primeiro erro.

## Problema

Escreva `validar_frota(configs)`: `configs` é uma lista de dicionários, cada um com
as chaves `"tipo_nome"` e `"estrategia_nome"`. Para cada um, chame
`validar_configuracao` dentro de um `try`/`except ConfiguracaoInvalida`. Devolva
uma tupla `(validas, invalidas)` — duas listas com os dicionários originais,
na ordem em que apareceram em `configs`.

## Exemplo

```python
configs = [
    {"tipo_nome": "RoboExplorador", "estrategia_nome": "zigzag"},
    {"tipo_nome": "RoboBlindado", "estrategia_nome": "zigzag"},
    {"tipo_nome": "RoboVeloz", "estrategia_nome": "padrao"},
    {"tipo_nome": "RoboExplorador", "estrategia_nome": "padrao"},
]
validas, invalidas = validar_frota(configs)
print(len(validas), len(invalidas))
print(invalidas)
```

Saída esperada:
```
2 2
[{'tipo_nome': 'RoboBlindado', 'estrategia_nome': 'zigzag'}, {'tipo_nome': 'RoboExplorador', 'estrategia_nome': 'padrao'}]
```

Repare que as duas configurações inválidas quebram por razões diferentes — uma por
`excludes`, outra por `requires` — e `validar_frota` não precisa saber qual é qual,
só que `ConfiguracaoInvalida` foi levantada.
