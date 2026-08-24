# Exercício Avançado — Aula 14

## Contexto

Na Aula 13, `verificar_invariante_frota` testou uma propriedade contra uma frota
inteira depois de executar uma sequência de comandos. Hoje, o cenário é orientado a
**eventos**: em vez de mover o robô de verdade até ele cruzar um limiar, o teste
**injeta a notificação diretamente** — a mesma técnica usada por *test doubles*/spies
(ver `unittest.mock` na leitura desta aula) — e confere se cada robô reagiu do jeito
esperado.

## Problema

Escreva `verificar_reacao_frota(robos, evento, dados_evento, invariante)`:

1. Para cada robô em `robos`, chama `robo.notificar(evento, **dados_evento)`.
2. Depois de notificar, chama `invariante(robo)` — uma função que devolve `True`
   (reagiu como esperado) ou `False` (não reagiu).
3. Devolve uma lista com o `nome` de todo robô cuja `invariante` devolveu `False`.
   Lista vazia = todos reagiram corretamente.

## Exemplo

```python
def esta_carregando(robo):
    return isinstance(robo.modo, ModoCarregando)

robos = [Robo("a", modo=ModoExplorando()), Robo("b", modo=ModoExplorando())]
for r in robos:
    r.adicionar_observador(MonitorBateria())

falhas = verificar_reacao_frota(
    robos, "bateria_critica", {"nivel": 15}, esta_carregando
)
print(falhas)
```

Saída esperada:
```
[]
```

## Extensão — conexão com testes de software

`verificar_reacao_frota` nunca precisa reproduzir as condições reais que levariam a
`gastar_bateria` a cruzar o limiar de 20% — ela **injeta** o evento direto, do jeito
que um teste com `unittest.mock`/spy faria para isolar o comportamento sob teste do
resto do sistema. Pesquise `unittest.mock.Mock` e `call_args` (documentação oficial:
https://docs.python.org/3/library/unittest.mock.html) — é a versão "de verdade" dessa
mesma ideia: um objeto que registra como foi chamado, sem precisar do sistema inteiro
rodando para provocar a chamada.
