# Referência rápida — Funções

---

## Definir e chamar

```python
def posicao_valida(x, y):
    return 0 <= x < LADO_GRADE and 0 <= y < LADO_GRADE

print(posicao_valida(5, 3))    # True
print(posicao_valida(10, 0))   # False
```
⚠️ Armadilha: esquecer o `:` no `def` → `SyntaxError`. Corpo deve ser indentado.

---

## Parâmetros com default

```python
def criar_robo(x=0, y=0, direcao='LESTE'):
    return {'x': x, 'y': y, 'direcao': direcao, 'trajetoria': [(x, y)]}

criar_robo()              # usa os defaults: (0,0,'LESTE')
criar_robo(3, 5, 'NORTE') # sobrescreve tudo
```
⚠️ Armadilha: **nunca liste ou dict como default** — é criado uma vez e compartilhado.
Use `None` e crie dentro: `def f(itens=None): itens = itens or []`.

---

## `return` vs `print`

```python
# print — imprime mas o chamador recebe None
def sem_retorno(nome):
    print(f'Olá, {nome}!')

resultado = sem_retorno('Robô')   # imprime 'Olá, Robô!'
print(resultado)                  # None — não retornou nada!

# return — entrega o valor ao chamador
def com_retorno(nome):
    return f'Olá, {nome}!'

msg = com_retorno('Robô')         # msg == 'Olá, Robô!'
```
Regra: **use `return`** quando o chamador precisar usar o valor. `print` é para exibição.

---

## Modificar in-place vs retornar novo valor

```python
# Modificar in-place: dict é mutável — as alterações refletem fora da função
def girar(robo, lado):
    robo['direcao'] = GIRAR_ESQ[robo['direcao']]   # sem return necessário

r = criar_robo()
girar(r, 'ESQ')
print(r['direcao'])   # NORTE — o dict foi alterado in-place
```
⚠️ Armadilha: listas e dicts passados como argumento são compartilhados (não copiados).
Se quiser não modificar o original, passe `dict(robo)` ou `robo.copy()`.

---

## Padrão do robô: `robo` como primeiro argumento

```python
# Toda função que opera sobre o robô recebe robo como 1º parâmetro
def sensor_frente(robo, obstaculos): ...
def avancar(robo, obstaculos): ...
def girar(robo, lado): ...
def executar(robo, obstaculos, comandos): ...
```
Este padrão é a **semente do `self`** da D2: na programação orientada a objetos,
`avancar(robo, obs)` vira `robo.avancar(obs)` onde `self` é o `robo` de hoje.
