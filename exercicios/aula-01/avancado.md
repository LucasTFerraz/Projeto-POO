# Exercício Avançado — Aula 1

## Contexto

Em testes de software, validar entradas é tão importante quanto escrever o código que as
processa. O robô v2 lê comandos como `"AVANCAR 3"` ou `"GIRAR ESQ"` — mas um arquivo de comandos
gerado por outro sistema pode vir com linhas mal formatadas.

## Problema

Você recebeu a seguinte lista de comandos brutos, como se tivessem vindo de um arquivo:

```python
comandos = ["AVANCAR 3", "girar esq", "AVANCAR", "PULAR 2", "  avancar   5  ", "GIRAR DIR"]
```

Escreva um programa que percorra `comandos` com um `for` e, para cada linha:
1. Normalize com `.strip().upper().split()`.
2. Considere **válido** um comando cuja ação (primeira palavra) seja `"AVANCAR"` (com um
   segundo item numérico) ou `"GIRAR"` (com segundo item `"ESQ"` ou `"DIR"`).
3. Considere **inválido** qualquer outro caso (ação desconhecida, ou `AVANCAR` sem valor
   numérico).

Ao final, imprima um relatório no formato:
```
Comandos válidos: 4
Comandos inválidos: 2
  'AVANCAR' — sem valor numérico
  'PULAR 2' — ação desconhecida
```

## Exemplo

Entrada: a lista `comandos` acima.
Saída esperada: conforme o formato acima (a ordem das linhas de erro deve seguir a ordem em que
os comandos inválidos aparecem na lista original).

**Conexão com testes de software:** este é o padrão de um *validador de log de execução* —
ferramenta comum em sistemas de robótica e automação para detectar comandos corrompidos ou
malformados antes (ou depois) de uma execução. O mesmo padrão aparece em qualquer framework de
teste que precise comparar uma entrada real contra um formato esperado, linha por linha.

> **Dica de implementação:** para checar se uma string representa um número inteiro, use
> `.isdigit()` (funciona para números positivos sem sinal, que é o caso aqui).
