# Referência rápida — Metaprogramação

## Módulos são objetos

```python
import math
print(type(math))          # <class 'module'>
print(math.pi)              # notação de ponto = atributo de objeto, igual robo1.x
print(math.__name__)        # 'math'
```
⚠️ Armadilha: `from modulo import *` traz os nomes de dentro do módulo, mas nunca o
nome do módulo em si — depois disso, `modulo.algo` quebra com `NameError`.

---

## `sys.modules` — o cache do import

```python
import sys
print("math" in sys.modules)              # True, depois do primeiro import
print(sys.modules["math"] is math)        # True — mesmo objeto
```
⚠️ Armadilha: editar um arquivo já importado, com o interpretador ainda aberto, não
recarrega nada — `sys.modules` continua apontando pro objeto antigo.

---

## `if __name__ == "__main__"`

```python
# dentro de robo.py
if __name__ == "__main__":
    print("rodando robo.py direto")
```
`__name__` vale `"__main__"` quando o arquivo é **executado diretamente**; vale o
nome do arquivo (`"robo"`) quando é **importado** por outro.
⚠️ Armadilha: código fora desse `if` roda **toda vez** que o arquivo é importado —
não só quando é executado direto.

---

## `__getattr__` — atributo sob demanda

```python
class Robo:
    def __getattr__(self, nome_attr):
        cache = self.__dict__.setdefault("_cache_leituras", {})
        if nome_attr in cache:
            return cache[nome_attr]
        if nome_attr.startswith("leitura_"):
            valor = calcular_leitura(nome_attr)   # sua lógica aqui
            cache[nome_attr] = valor
            return valor
        raise AttributeError(f"Robo não tem atributo {nome_attr!r}")
```
`__getattr__` só roda quando a busca normal (`__dict__` da instância, depois a
classe) **falha** — nunca para um atributo que já existe.
⚠️ Armadilha 1: sempre levante `AttributeError` no caso não tratado — outra exceção
(`KeyError`, por exemplo) quebra `hasattr()`/`getattr(obj, nome, default)`.
⚠️ Armadilha 2: dentro de `__getattr__`, nunca leia/escreva com `self.atributo = ...`
ou `hasattr(self, "algo")` sobre um atributo que também dispararia `__getattr__` —
vira `RecursionError`. Vá direto ao `self.__dict__`.

---

## `__setattr__` — auditando toda escrita

```python
class Robo:
    def __setattr__(self, nome_attr, valor):
        log = self.__dict__.setdefault("_log_mudancas", [])
        log.append((nome_attr, valor))
        super().__setattr__(nome_attr, valor)   # sem isso, nada é gravado!
```
Roda para **toda** atribuição, sempre — mesmo as que o `__init__` faz.
⚠️ Armadilha: esquecer `super().__setattr__(...)` no fim não quebra a criação do
objeto — quebra **silenciosamente** cada leitura futura, com `AttributeError`
confuso vindo do `__getattr__`.

---

## `__init_subclass__` — toda subclasse se registra sozinha

```python
class Robo:
    _registro = {}

    def __init_subclass__(cls, categoria="geral", **kwargs):
        super().__init_subclass__(**kwargs)   # sempre repasse o que sobrar
        Robo._registro[cls.__name__] = cls
        cls.categoria = categoria


class RoboVeloz(Robo, categoria="ofensivo"):
    pass


print(Robo._registro)         # {'RoboVeloz': <class ...>} — sozinho, sem tocar em Robo
```
Roda uma vez, no momento em que a **subclasse é definida** — não em `__init__`, não
por instância.
⚠️ Armadilha: esquecer `**kwargs` na assinatura (ou esquecer de repassar pro
`super().__init_subclass__(**kwargs)`) quebra com `TypeError: got an unexpected
keyword argument` assim que alguém passar um argumento de classe (`categoria=...`).
