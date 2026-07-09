# Exercício Básico — Aula 4

## Contexto

Em sala, filtramos o log do robô para pegar só os passos com `status == "OK"`, usando list
comprehension com filtro:
```python
passos_ok = [p for p in log if p["status"] == "OK"]
```

## Problema

Escreva `passos_bloqueados(log)` que faz a mesma coisa, mas para o lado oposto: devolve a lista
de passos (os dicts inteiros, não só o comando) cujo `status` foi `"PAREDE"` — os momentos em que
o robô tentou avançar e bateu.

## Exemplo

```python
log = [
    {"x": 3, "y": 0, "comando": "AVANCAR 3", "status": "OK"},
    {"x": 3, "y": 2, "comando": "AVANCAR 5", "status": "PAREDE"},
    {"x": 6, "y": 2, "comando": "AVANCAR 4", "status": "PAREDE"},
]
print(len(passos_bloqueados(log)))
```

Saída esperada:
```
2
```

## Dica

É exatamente a mesma estrutura de `passos_ok` que fizemos em sala — só troca a string comparada
no `if` de `"OK"` para `"PAREDE"`. Não precisa inverter o filtro com `not`.
