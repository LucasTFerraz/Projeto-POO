# Exercício Básico — Aula 15

## Contexto

Em sala, `EXCLUI["RoboVeloz"] = {"esquiva"}` — `RoboVeloz` já é rápido por dobrar
`avancar()`, e `EstrategiaEsquiva` para o robô pra girar antes de andar,
desperdiçando exatamente essa vantagem. `EstrategiaZigzag` também vira bruscamente a
cada `periodo` passos — o mesmo problema, de outro jeito.

## Problema

Acrescente `"zigzag"` ao conjunto de estratégias que `RoboVeloz` exclui, sem apagar
`"esquiva"` que já está lá.

## Exemplo

```python
print(EXCLUI["RoboVeloz"])
validar_configuracao("RoboVeloz", "zigzag")
```

Saída esperada:
```
{'esquiva', 'zigzag'}
ConfiguracaoInvalida: RoboVeloz exclui a estratégia 'zigzag'
```

## Dica

`EXCLUI["RoboVeloz"]` já é um `set` — use `.add("zigzag")` nele, em vez de
reatribuir a chave inteira (isso apagaria o `"esquiva"` que já estava lá).
