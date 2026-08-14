# Exercício Avançado — Aula 9

## Contexto

Composição permite trocar uma peça por outra com o mesmo "contrato" (o mesmo método
esperado) — vocês fizeram isso em sala com `robo1.sensor = Sensor(alcance=5)`. Em testes
automatizados, essa técnica tem nome: **dublê de teste** (*test double*). Em vez de
depender de um sensor de verdade (ou de rede, banco de dados, relógio do sistema...), o
teste substitui a peça real por uma versão fake e controlada — assim o resultado do
teste não depende de nada fora do seu controle.

## Problema

Escreva `SensorFalso`, uma classe com o mesmo contrato de `Sensor` (um método
`ler(robo)`), mas que **sempre** devolve um valor fixo, passado no construtor —
`SensorFalso(livre=True)` sempre devolve `True`; `SensorFalso(livre=False)` sempre
devolve `False`. Nada de calcular grade, obstáculo ou direção de verdade.

Depois, escreva `teste_avancar_bloqueado()`: crie um `Robo` comum, troque `robo.sensor`
por um `SensorFalso(livre=False)`, chame `robo.avancar()`, e imprima `"PASSOU"` se
`avancar()` devolveu `False` **e** a posição do robô não mudou; `"FALHOU"` caso
contrário.

## Exemplo

```python
teste_avancar_bloqueado()
```

Saída esperada:
```
PASSOU
```

## Extensão — conexão com testes de software

Pesquise sobre **test doubles**/**mocks** — por exemplo, `unittest.mock.Mock` ou
`MagicMock` da biblioteca padrão, ou `pytest-mock`. Compare com o que vocês acabaram de
fazer: `SensorFalso` não herda de `Sensor`, não implementa nenhuma interface formal — só
precisa ter um `ler(robo)` com a cara certa, porque Python usa duck typing. É exatamente
essa flexibilidade que permite trocar `robo.sensor` por `Mock()` num teste real, sem
precisar de herança nem de classes abstratas. Por que essa técnica é especialmente útil
para testar código que depende de algo lento, caro ou não-determinístico (rede, banco de
dados, hora atual)?
