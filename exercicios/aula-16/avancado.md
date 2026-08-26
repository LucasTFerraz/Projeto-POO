# Exercício Avançado — Aula 16

## Contexto

Na Aula 15, `matriz_configuracoes` testou à mão **todas** as combinações de tipo ×
estratégia. Este exercício fecha o curso testando **todas** as combinações de
tipo × estratégia × grade com `pytest` de verdade — e não só "isso é válido ou
não", mas o **contrato inteiro**: uma configuração válida sempre produz um robô
com exatamente o tipo e a estratégia pedidos; uma inválida sempre levanta
`ConfiguracaoInvalida`, nunca outra coisa.

## Problema

Num arquivo `test_contrato.py`, escreva `test_contrato_criar_ou_recusar`,
parametrizado com todo `(tipo_nome, estrategia_nome, grade_nome)` de
`Robo._registro` × `{"padrao", "esquiva", "zigzag"}` × `GRADES_VALIDAS` (use
`itertools.product`). Para cada combinação:

1. Se a configuração é válida (chame `validar_configuracao` dentro de um
   `try`/`except` pra descobrir, sem levantar o teste inteiro): crie o robô e
   confirme que `type(robo).__name__ == tipo_nome` e que a estratégia criada é
   exatamente a classe certa em `FABRICA_ESTRATEGIAS[estrategia_nome]`.
2. Se é inválida: confirme com `pytest.raises(ConfiguracaoInvalida)` que
   `criar_robo_configurado` recusa.

## Exemplo

```python
CASOS = list(itertools.product(sorted(Robo._registro),
                                sorted({"padrao", "esquiva", "zigzag"}),
                                sorted(GRADES_VALIDAS)))

@pytest.mark.parametrize("tipo_nome,estrategia_nome,grade_nome", CASOS)
def test_contrato_criar_ou_recusar(tipo_nome, estrategia_nome, grade_nome):
    ...
```

Rodando `pytest test_contrato.py -v`, saída esperada (3 tipos × 3 estratégias × 3
grades):
```
27 passed
```

## Extensão — conexão com testes de software

Vinte e sete testes de uma função só, sem escrever nenhum caso à mão — isso é
**teste combinatório** de verdade, fechando o ciclo que começou na Aula 15 com
`matriz_configuracoes`. A diferença não é só sintática: com `pytest`, cada
combinação vira um teste individualmente reportável (`pytest -v -k RoboBlindado`
filtra só os casos daquele tipo), e o `pytest.raises` documenta, no próprio
código do teste, **qual** exceção é esperada — não só "deu erro". Se o modelo de
features crescer (uma quarta dimensão, mais tipos), essa mesma suíte continua
funcionando sem nenhuma linha nova — o `itertools.product` sobre
`Robo._registro`/`GRADES_VALIDAS` já capta qualquer variante nova
automaticamente, a mesma lição de `TIPOS_VALIDOS = set(Robo._registro)` desde a
Aula 15.
