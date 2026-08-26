# Referência rápida — pytest

## Convenção de descoberta: `test_*.py`, função `test_*`

```python
# test_configuracao.py
def test_explorador_com_zigzag_e_valido():
    robo = criar_robo_configurado("RoboExplorador", "Scout", estrategia_nome="zigzag")
    assert robo.nome == "Scout"
```
Rodar: `pytest -v` (encontra todo `test_*.py` sozinho, recursivamente).
⚠️ Armadilha: função sem o prefixo `test_` **não é coletada** — some da suíte, sem
nenhum erro avisando. `pytest` reportar menos testes do que deveria é o sinal.

---

## `assert` puro, e o que a mensagem de erro mostra

```python
assert scout.categoria == "ofensivo"
```
Saída quando falha (rodando via `pytest`, não `python arquivo.py`):
```
E       AssertionError: assert 'reconhecimento' == 'ofensivo'
E         - ofensivo
E         + reconhecimento
```
⚠️ Armadilha: essa reescrita rica do `assert` (*assertion rewriting*) só acontece
quando `pytest` importa o arquivo — `python arquivo.py` direto mostra só
`AssertionError`, sem diff nenhum.

---

## `pytest.raises`: testando que uma exceção *deveria* acontecer

```python
import pytest

def test_blindado_com_zigzag_levanta_erro():
    with pytest.raises(ConfiguracaoInvalida):
        criar_robo_configurado("RoboBlindado", "Tank", estrategia_nome="zigzag")
```
⚠️ Armadilha: chamar a função sem `pytest.raises` e deixar a exceção subir também
falha o teste — mas por um motivo diferente ("erro inesperado"), não "confirmei que
o erro certo aconteceu". Se um caso **deveria** falhar, isso precisa estar
explícito.

---

## Fixtures: setup reaproveitado, isolado por teste

```python
@pytest.fixture
def scout():
    return criar_robo_configurado("RoboExplorador", "Scout", estrategia_nome="zigzag")

def test_scout_tem_estrategia_zigzag(scout):     # nome do parâmetro == nome da fixture
    assert type(scout.estrategia).__name__ == "EstrategiaZigzag"
```
⚠️ Armadilha: `pytest` chama a fixture **de novo, do zero**, pra cada teste que a
usa — não é o mesmo objeto reaproveitado entre testes. Um teste nunca pode depender
de estado deixado por outro; `pytest` não garante ordem de execução.

---

## `@pytest.mark.parametrize`: uma função, N testes

```python
@pytest.mark.parametrize("tipo_nome,estrategia_nome,valido", [
    ("RoboBlindado", "zigzag", False),
    ("RoboExplorador", "zigzag", True),
])
def test_contrato_de_configuracao(tipo_nome, estrategia_nome, valido):
    if valido:
        criar_robo_configurado(tipo_nome, "Teste", estrategia_nome=estrategia_nome)
    else:
        with pytest.raises(ConfiguracaoInvalida):
            criar_robo_configurado(tipo_nome, "Teste", estrategia_nome=estrategia_nome)
```
Cada linha da lista vira um teste com nome próprio:
`test_contrato_de_configuracao[RoboBlindado-zigzag-False]`.
⚠️ Armadilha: se um dos casos falhar, os outros continuam rodando e reportando —
`parametrize` não para no primeiro erro, ao contrário de um laço manual com
`return`/`break`.
