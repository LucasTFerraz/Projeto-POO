# Exercício Médio — Aula 16

## Contexto

Em sala, uma fixture montou **um** robô configurado, reaproveitado entre testes.
Este exercício combina fixture com a ideia de frota (Aula 12/16): uma fixture que
monta **vários** robôs de uma vez, e um teste que confere uma propriedade sobre o
grupo inteiro.

## Problema

Escreva, num arquivo `test_frota.py`:

1. Uma fixture `frota_sem_colisao` que monta uma lista com pelo menos dois robôs
   configurados (via `criar_robo_configurado`), em posições `(x, y)` diferentes.
2. Um teste `test_frota_sem_colisao_inicial(frota_sem_colisao)` que confirma que
   nenhum par de robôs da fixture começa na **mesma** posição — ou seja, o número
   de posições únicas é igual ao número de robôs.

## Exemplo

```python
@pytest.fixture
def frota_sem_colisao():
    a = criar_robo_configurado("RoboExplorador", "a", estrategia_nome="zigzag", x=0, y=0)
    b = criar_robo_configurado("RoboVeloz", "b", x=5, y=5)
    return [a, b]


def test_frota_sem_colisao_inicial(frota_sem_colisao):
    posicoes = [(r.x, r.y) for r in frota_sem_colisao]
    assert len(posicoes) == len(set(posicoes))
```

Rodando `pytest test_frota.py -v`, saída esperada:
```
test_frota.py::test_frota_sem_colisao_inicial PASSED
```
