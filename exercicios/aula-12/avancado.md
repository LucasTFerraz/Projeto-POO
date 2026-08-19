# Exercício Avançado — Aula 12

## Contexto

Em sala, `__init_subclass__` fez toda subclasse de `Robo` se registrar sozinha num
catálogo, sem lista mantida à mão. É exatamente o mecanismo que frameworks de teste
usam por baixo dos panos: quando vocês escrevem uma classe de teste em `pytest` (ou
em `unittest`), ninguém registra essa classe em lugar nenhum — o framework **descobre**
sozinho, na hora de rodar, todas as classes e métodos de teste que existem. Este
exercício pede para vocês construírem essa peça — em miniatura.

## Problema

Escreva `CasoDeTeste`, uma classe-mãe que usa `__init_subclass__` para registrar
automaticamente toda subclasse (guarde as classes numa lista de classe, ex.:
`CasoDeTeste._registro`). Escreva também `rodar_todos_os_testes()`, uma função que:

1. Para cada classe registrada, cria uma instância.
2. Para cada método da instância cujo nome comece com `teste_`, chama o método sem
   argumentos.
3. Se o método rodar sem levantar `AssertionError`, registra o resultado como
   `(nome_da_classe, nome_do_metodo, "PASSOU")`.
4. Se levantar `AssertionError`, registra como
   `(nome_da_classe, nome_do_metodo, f"FALHOU: {erro}")`.

A função deve devolver a lista de resultados, na ordem em que os métodos foram
descobertos. **Nenhuma lista de classes ou métodos deve ser escrita à mão** — tudo
descoberto automaticamente a partir de `__init_subclass__` e `dir()`/`getattr()`.

## Exemplo

```python
class TesteRobo(CasoDeTeste):
    def teste_grade_padrao(self):
        assert LADO_GRADE == 10

    def teste_posicao_inicial(self):
        r = Robo()
        assert (r.x, r.y) == (0, 0)

for resultado in rodar_todos_os_testes():
    print(resultado)
```

Saída esperada:
```
('TesteRobo', 'teste_grade_padrao', 'PASSOU')
('TesteRobo', 'teste_posicao_inicial', 'PASSOU')
```

## Extensão — conexão com testes de software

Vocês acabaram de construir, em ~20 linhas, o núcleo de descoberta automática de
testes que sustenta `pytest`: uma classe-mãe que qualquer arquivo de teste pode
herdar, um hook que registra cada nova classe de teste sozinha, e uma convenção de
nome (`teste_*`, ou `test_*` no `pytest` de verdade) que decide o que é executável.
A diferença entre o que vocês escreveram e o `pytest` real é sofisticação — coleta de
testes em múltiplos arquivos, fixtures, relatório colorido — não o mecanismo central.
Pesquise a documentação do `pytest` sobre "test discovery"
(https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery):
quais convenções de nome de arquivo/classe/função o `pytest` usa para decidir o que
é teste, e o que aconteceria se vocês nomeassem um método `verifica_grade` em vez de
`teste_grade`?
