# Referência rápida — Python idiomático

## List comprehension (recap + filtro)

```python
coords = [(p["x"], p["y"]) for p in log]                  # transformação
passos_ok = [p for p in log if p["status"] == "OK"]        # + filtro
```
⚠️ Armadilha: `if` de filtro sempre depois do `for` — `[p if cond for p in log]` é `SyntaxError`.

---

## Tuple comprehension? Não existe — generator expression

```python
gen = (p["status"] for p in log)      # generator, NÃO tupla
tup = tuple(p["status"] for p in log)  # tuple(...) materializa de verdade
```
⚠️ Armadilha: `(...)` sozinho nunca vira tupla — só `list`/`dict`/`set` têm comprehension de
verdade; parêntese é generator, sempre.

---

## Nested comprehension e a armadilha `[[...]] * N`

```python
grade = [[0] * LADO_GRADE for _ in range(LADO_GRADE)]   # LADO_GRADE objetos distintos
```
⚠️ Armadilha: `[[0] * LADO_GRADE] * LADO_GRADE` cria **uma** linha repetida — mudar
`grade[0][0]` muda todas. Prove com `id(grade[0]) == id(grade[1])`.

---

## Dict comprehension

```python
mapa = {(p["x"], p["y"]): p["status"] for p in log}                  # chave repetida sobrescreve
posicoes = [(p["x"], p["y"]) for p in log]
visitas = {pos: posicoes.count(pos) for pos in set(posicoes)}         # conta sem Counter
mais_visitada = max(visitas, key=visitas.get)                         # máximo sem ordenar tudo
```
⚠️ Armadilha: iterar `posicoes` direto (sem `set()`) ainda funciona, mas refaz `.count()` para
cada repetição — mais lento, não é o padrão.

---

## `*args`

```python
def relatorio(*passos):          # passos vira uma tupla
    return [f"({p['x']}, {p['y']})" for p in passos]

relatorio(*log[:3])              # desempacota a lista em argumentos separados
```
⚠️ Armadilha: `relatorio(log)` (sem `*`) passa a lista **inteira** como um único argumento —
`passos` vira `(log,)`, uma tupla de 1 elemento.

---

## `**kwargs`

```python
def configurar_robo(**opcoes):
    lado = opcoes.get("lado", 10)          # .get evita KeyError se a opção não vier
    return lado, opcoes.get("inicio", (0, 0))
```
⚠️ Armadilha: `**kwargs` só captura argumentos **nomeados** (`chave=valor`) — argumentos
posicionais quebram com `TypeError`.

---

## `enumerate` / `zip`

```python
for i, passo in enumerate(log, start=1):
    print(i, passo["status"])

comandos = [p["comando"] for p in log]
resultados = [p["status"] for p in log]
para_dict = dict(zip(comandos, resultados))    # zip + dict(): idiomatismo comum
```
⚠️ Armadilha: `zip` para no **menor** iterável, silenciosamente — sem erro, sem aviso.

---

## `map` / `filter` (com `lambda`)

```python
acoes = list(map(lambda p: p["comando"].split()[0], log))     # transforma cada elemento
passos_ok = list(filter(lambda p: p["status"] == "OK", log))   # seleciona elementos
```
⚠️ Armadilha: `map`/`filter` devolvem objetos preguiçosos — precisam de `list(...)` para
mostrar o conteúdo. E: comprehension geralmente é preferida a `map`/`filter`+`lambda`.

---

## `reduce`

```python
from functools import reduce                      # não é builtin — precisa importar

valores = [int(p["comando"].split()[1]) for p in log if p["comando"].startswith("AVANCAR")]
total = reduce(lambda acc, v: acc + v, valores)     # combina tudo num valor só
```
⚠️ Armadilha: `sum`/`max`/`min` já resolvem os casos comuns — só use `reduce` quando não há
builtin pronto (ex.: um "maior string por critério customizado").
