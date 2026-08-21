# Exercício Médio — Aula 13

## Contexto

Em sala, `criar_robo_configurado` (Factory) montou uma frota a partir de uma lista de
configuração, e `parse_comando`/`Comando` (Command) executaram uma sequência de ações
num robô. Este exercício combina os dois: a mesma sequência de comandos, aplicada a
cada robô de uma frota inteira.

## Problema

Escreva `criar_frota_com_comandos(configs, comandos)`: usa `criar_robo_configurado`
para montar um robô por item de `configs` (cada item é um dicionário de kwargs),
executa a mesma lista `comandos` (strings, no formato de `parse_comando`) em **cada**
robô da frota, e devolve uma lista de tuplas `(nome, x, y, direcao)` — uma por robô,
na ordem em que apareceram em `configs`.

## Exemplo

```python
configs = [
    {"tipo_nome": "RoboVeloz", "nome": "a"},
    {"tipo_nome": "RoboExplorador", "nome": "b"},
]
resultado = criar_frota_com_comandos(configs, ["GIRAR ESQ", "AVANCAR 2"])
for linha in resultado:
    print(linha)
```

Saída esperada:
```
('a', 0, 4, <Direcao.NORTE: (0, 1)>)
('b', 0, 2, <Direcao.NORTE: (0, 1)>)
```

Repare que `"a"` (`RoboVeloz`) anda o **dobro** de `"b"` com o mesmo comando
`"AVANCAR 2"` — `RoboVeloz.avancar()` já é sobrescrito desde a Aula 8 pra mover duas
vezes por chamada; `criar_frota_com_comandos` não precisa saber disso, só delega pro
`Comando.executar()` de cada robô.
