# Exercício Avançado — Aula 3

## Contexto

Após o robô executar um programa, `gravar_log` registra a trajetória em `log.txt` no formato
`x,y` (uma posição por linha). Em testes de sistemas robóticos, analisar o log de uma execução
é tão importante quanto gerar o log — é assim que se detecta anomalias sem precisar rodar o
robô de novo. Este exercício é um **analisador de log estático**: examina o comportamento do
robô sem executá-lo.

## Problema

Implemente `resumo_log(caminho)`, que lê um arquivo de log e imprime um relatório com: posição
inicial, posição final, total de posições registradas e a posição mais visitada (contando com
um dict, padrão `d.get(k, 0) + 1`). Use `caminho="log_aula03.txt"` como valor padrão — o arquivo
de exemplo está em `dados/aula-03/log_aula03.txt` (ou use o `log.txt` que o seu próprio robô v6
gerou no notebook da Aula 3).

## Exemplo

Para o arquivo `log_aula03.txt` (conteúdo: `0,0` / `0,3` / `0,3` / `2,3` / `2,3` / `2,4`):

```python
resumo_log("log_aula03.txt")
```

Saída esperada:
```
=== Resumo do log ===
Início: (0, 0)
Fim:    (2, 4)
Total de posições: 6
Mais visitada: (0, 3) — 2 vez(es)
```

*(Há empate entre `(0, 3)` e `(2, 3)`, ambas com 2 visitas — qualquer uma das duas é aceitável
na sua saída, dependendo de como você percorre o dict.)*

---

## Extensão 1 — Detectar sequências repetidas

O robô às vezes fica preso num ciclo (executando o mesmo percurso em loop). Implemente
`detectar_ciclo(posicoes)` que retorna `True` se alguma posição aparece mais de uma vez na
trajetória.

```python
def detectar_ciclo(posicoes):
    # implemente aqui
    pass

print(detectar_ciclo([(0,0), (1,0), (2,0), (1,0)]))   # True (1,0 repetido)
print(detectar_ciclo([(0,0), (1,0), (2,0), (3,0)]))   # False
```

## Extensão 2 — Conexão com testes de software

Em sistemas embarcados reais (robôs ROS 2, drones, veículos autônomos), essa análise
pós-execução é chamada de *log replay* e é uma das principais ferramentas de depuração —
antes de reproduzir um bug ao vivo, o time examina o log da execução que falhou.

Pesquise: o que é `rosbag` no contexto do ROS 2? Como ele se relaciona com o que
`gravar_log` + `resumo_log` fazem neste exercício?
