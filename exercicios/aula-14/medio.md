# Exercício Médio — Aula 14

## Contexto

Em sala, `MonitorBateria` (um `Observador`) trocou `robo.modo` sozinho, reagindo à
notificação de bateria crítica — sem ninguém chamar `tick()` ou checar nada
manualmente. Este exercício combina Observer e State: além de trocar o modo, o
observador também guarda um **histórico** de cada transição que provocou.

## Problema

Escreva `HistoricoDeModos(Observador)`:

1. `__init__`: cria `self.transicoes = []`.
2. `atualizar(self, evento, **dados)`: se `evento` for `"bateria_critica"`, troca
   `dados["robo"].modo` para uma nova `ModoCarregando()` (igual `MonitorBateria` fez em
   sala) **e** adiciona a `self.transicoes` uma tupla `(nivel, nome_do_novo_modo)`,
   onde `nivel` vem de `dados["nivel"]` e `nome_do_novo_modo` é
   `type(dados["robo"].modo).__name__`.

## Exemplo

```python
robo2 = Robo("Bender", x=0, y=0)
robo2.modo = ModoExplorando()
historico = HistoricoDeModos()
robo2.adicionar_observador(historico)
robo2.gastar_bateria(85)
print(historico.transicoes)
```

Saída esperada:
```
[(15, 'ModoCarregando')]
```
