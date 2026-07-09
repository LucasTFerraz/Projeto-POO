# Exercício Avançado — Aula 4

## Contexto

Um log de execução (do robô, ou de qualquer sistema de testes automatizados) esconde padrões que
não aparecem olhando linha por linha: quantas falhas seguidas aconteceram, se o processo ficou
"preso" repetindo o mesmo estado, etc. Detectar esses padrões automaticamente — em vez de um
humano lendo o log inteiro — é exatamente o trabalho de um verificador de log/health-check em
testes de software.

## Problema

Escreva `maior_sequencia_bloqueios(log)`, que recebe o log do robô (lista de dicts com `x`, `y`,
`status`) e devolve o **maior número de passos consecutivos** com `status == "PAREDE"` — ou seja,
quantas vezes seguidas, sem nenhum `"OK"` no meio, o robô bateu na parede.

Depois, escreva `robo_esta_preso(log, limite)`, que devolve `True` se em algum momento o robô
visitou a **mesma coordenada `(x, y)`** por `limite` vezes ou mais **sem visitar nenhuma
coordenada nova entre essas repetições** — um sinal de que o robô está girando no lugar sem
progredir (o tipo de coisa que, num sistema de testes real, dispararia um alerta de "processo
travado").

## Exemplo

```python
log = [
    {"x": 0, "y": 0, "status": "OK"},
    {"x": 1, "y": 0, "status": "PAREDE"},
    {"x": 1, "y": 0, "status": "PAREDE"},
    {"x": 1, "y": 0, "status": "PAREDE"},
    {"x": 2, "y": 0, "status": "OK"},
]

print(maior_sequencia_bloqueios(log))     # 3 (as três linhas PAREDE seguidas)
print(robo_esta_preso(log, limite=3))     # True (mesma posição (1,0) 3 vezes seguidas)
print(robo_esta_preso(log, limite=4))     # False (só se repetiu 3 vezes, não 4)
```

Saída esperada:
```
3
True
False
```

## Extensão — conexão com testes de software

Pesquise: em ferramentas de observabilidade (Datadog, Grafana, ELK) e em suites de teste (CI/CD),
que tipo de "regra" costuma disparar um alerta automático a partir de um log de execução? Seu
`robo_esta_preso` é uma versão simplificada de uma dessas regras — qual delas, especificamente?
