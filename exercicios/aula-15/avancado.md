# Exercício Avançado — Aula 15

## Contexto

Em vez de testar configurações uma a uma, à mão, este exercício testa **todas as
combinações possíveis** de uma vez — o mesmo espírito de `verificar_invariante_frota`
(Aula 13), aplicado ao próprio modelo de features de hoje.

## Problema

Escreva `matriz_configuracoes(tipos, estrategias)`: usando `itertools.product`,
gere todo par `(tipo_nome, estrategia_nome)` de `tipos` × `estrategias`, chame
`validar_configuracao` pra cada par (dentro de `try`/`except`), e devolva um
dicionário `{(tipo_nome, estrategia_nome): True_ou_False}` — `True` se a
combinação é válida, `False` se `ConfiguracaoInvalida` foi levantada.

## Exemplo

```python
tipos = sorted(Robo._registro)
estrategias = sorted(ESTRATEGIAS_VALIDAS)
matriz = matriz_configuracoes(tipos, estrategias)
invalidas = [par for par, ok in matriz.items() if not ok]
print(len(matriz), len(invalidas))
print(invalidas)
```

Saída esperada:
```
9 2
[('RoboBlindado', 'zigzag'), ('RoboExplorador', 'padrao')]
```

## Extensão — conexão com testes de software

`matriz_configuracoes` é uma versão pequena e caseira de **teste combinatório**
(*combinatorial testing*): em vez de escolher alguns casos de teste à mão e torcer
pra cobrir os problemas, gera-se e testa-se **todo** o espaço de combinações — aqui
só 3×3=9, mas a mesma ideia escala (com técnicas como *pairwise testing*, que testa
todo **par** de valores sem precisar do produto cartesiano completo, quando o
espaço fica grande demais). É o mesmo princípio por trás de
`pytest.mark.parametrize` (documentação oficial:
https://docs.pytest.org/en/stable/how-to/parametrize.html) — que a turma vai usar
de verdade na Aula 16, pra rodar o mesmo teste contra uma lista inteira de
combinações, sem escrever um teste por linha.
