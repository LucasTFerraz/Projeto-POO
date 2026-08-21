# Referência rápida — Design Patterns

## Strategy — comportamento intercambiável

```python
class EstrategiaPadrao:
    def mover(self, robo):
        return robo.avancar()

class Robo:
    def mover(self):
        return self.estrategia.mover(self)   # troca comportamento = troca objeto
```
Duck typing: nenhuma interface obrigatória — qualquer objeto com `mover(robo)` serve.
⚠️ Armadilha: o erro de uma estratégia incompleta (sem `mover`) só aparece quando
alguém **chama** `mover()`, não na hora de criar o robô — é o preço da flexibilidade.

---

## Command — uma ação vira objeto

```python
from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self, robo):
        ...

class ComandoAvancar(Comando):
    def __init__(self, passos):
        self.passos = passos
    def executar(self, robo):
        robo.avancar_n(self.passos)
```
`ABC` + `@abstractmethod` recusam instanciar qualquer subclasse que não implemente
`executar` — contrato formal, porque diferente do Strategy (duck typing, sem herança
obrigatória) `Comando` já **é** uma hierarquia de herança de verdade.

`historico` guarda **objetos** (não strings) → dá pra reexecutar em outro robô sem
reparsear nada:
```python
for cmd in robo1.historico:
    cmd.executar(robo2)
```
⚠️ Armadilha: criar `ComandoAvancar(3)` não move ninguém — só guarda os dados. A ação
só acontece quando `executar(robo)` é chamado.
⚠️ Armadilha: `Comando` não é `@dataclass`, mesmo sendo um "registro de dados" como
`Posicao`/`Leitura` — algumas subclasses precisam mutar a instância depois de criada
(ex.: guardar a posição anterior pra desfazer), o que `frozen=True` bloquearia.

---

## Singleton — cuidado, não robô

```python
class Configuracao:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
```
⚠️ Armadilha: garante uma única instância — mas é estado global disfarçado. Ruim pra
teste (um teste contamina o próximo). Prefira passar a dependência explicitamente.

---

## Factory — centraliza a escolha de classe

```python
def criar_robo(tipo_nome, nome, **kwargs):
    classe = Robo._registro.get(tipo_nome)     # Robo._registro vem de __init_subclass__
    if classe is None:
        raise ValueError(f"tipo desconhecido: {tipo_nome!r}")
    return classe(nome, **kwargs)
```
Combina com Strategy: a fábrica também pode escolher a estratégia, com outro
dicionário de despacho:
```python
FABRICA_ESTRATEGIAS = {"padrao": EstrategiaPadrao, "zigzag": EstrategiaZigzag}

def criar_robo_configurado(tipo_nome, nome, estrategia_nome="padrao", **kwargs):
    robo = criar_robo(tipo_nome, nome, **kwargs)
    robo.estrategia = FABRICA_ESTRATEGIAS[estrategia_nome]()
    return robo
```
⚠️ Armadilha: `Robo._registro` só ganha uma entrada depois que o módulo com a
subclasse é **importado** — arquivo existir no disco não basta, a classe precisa ser
"vista" pelo Python.
