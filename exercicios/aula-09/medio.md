# Exercício Médio — Aula 9

## Contexto

Vocês viram herança (`RoboComSensor(Robo)`, sobrescrevendo `sensor_frente()`) e
composição (`Sensor` como objeto que `Robo` **tem**) resolvendo o mesmo tipo de
problema de formas diferentes. Este exercício pede as duas ferramentas **juntas**, no
mesmo robô.

## Problema

Escreva `Alarme`, uma classe nova (sem relação com `Robo`), com um método
`disparar()` que imprime `"⚠️ Alarme disparado!"`.

Escreva `RoboEscolta(Robo)` — por **herança**, estende `Robo`. No `__init__`, além de
chamar `super().__init__(nome, **kwargs)`, **compõe** um `Alarme` em `self.alarme`.
Sobrescreva `sensor_frente()`: chame a versão do pai (`super().sensor_frente()`); se o
resultado for `False` (caminho bloqueado), chame `self.alarme.disparar()` antes de
devolver `False`. Se o caminho estiver livre, devolva `True` normalmente, sem disparar
nada.

## Exemplo

```python
obstaculos = {(1, 0): True}
re = RoboEscolta("Sentinela", obstaculos=obstaculos)
print(re.sensor_frente())   # bloqueado, dispara o alarme antes

re2 = RoboEscolta("Sentinela2")
print(re2.sensor_frente())  # livre, sem alarme
```

Saída esperada:
```
⚠️ Alarme disparado!
False
True
```
