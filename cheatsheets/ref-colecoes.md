# Referência rápida — Coleções

## Lista: operações essenciais

```python
trajetoria = [(0,0), (1,0), (2,0)]
trajetoria[0]               # (0,0)  — indexação
trajetoria[-1]              # (2,0)  — último elemento
len(trajetoria)             # 3
(1,0) in trajetoria         # True   — busca O(n)
trajetoria.append((3,0))    # adiciona ao fim
trajetoria.pop()            # remove e retorna o último → (3,0)
copia = trajetoria[:]       # cópia independente (trajetoria[:] ≠ trajetoria)
```
⚠️ Armadilha: `b = a` cria **alias** (mesmo objeto). `b = a[:]` cria **cópia**.

---

## Fatiamento (slicing)

`lista[inicio:fim]` devolve uma **fatia** — uma lista nova com os elementos do índice
`inicio` até `fim - 1` (o `fim` é exclusivo, igual em `range()`). Omitir `inicio` começa do
0; omitir `fim` vai até o final. A mesma notação funciona em string.

```python
frutas = ["maçã", "banana", "cereja", "uva"]
frutas[1:3]      # ["banana", "cereja"]  — índices 1 e 2
frutas[:2]       # ["maçã", "banana"]    — do início até o índice 1
frutas[2:]       # ["cereja", "uva"]     — do índice 2 até o fim
frutas[:]        # cópia da lista inteira (fatia completa)

"banana"[1:3]    # "an" — mesma sintaxe em string
```
⚠️ Armadilha: toda fatia cria uma lista (ou string) **nova** — inclusive `frutas[:]`, que é
exatamente por isso que serve para copiar em vez de aliasar.

**Métodos adicionais de lista** (não cobertos na condução da Aula 2 — referência):
```python
frutas.insert(1, "kiwi")   # insere na posição 1, empurrando o resto
frutas.remove("banana")    # remove a primeira ocorrência pelo valor (não pelo índice)
frutas.extend(["pera"])    # concatena outra lista ao final (append adicionaria a lista inteira como 1 item)
sorted(frutas)              # devolve uma lista nova, ordenada — não muda `frutas`
frutas.sort()                # ordena `frutas` in-place — não devolve nada (None)
```

---

## List comprehension (introdução mínima)

`[expressão for variável in iterável]` cria uma lista nova: para cada valor que `variável`
assume percorrendo `iterável`, calcula `expressão` e guarda o resultado. Quando o valor do
`for` não importa — só queremos repetir N vezes — a convenção é chamar a variável de `_`.

```python
[0 for _ in range(5)]      # [0, 0, 0, 0, 0]  — _ porque o valor do range não é usado
[n**2 for n in range(5)]   # [0, 1, 4, 9, 16] — aqui n importa
```
Profundidade real (condicionais, comprehensions aninhadas, `dict`/`set` comprehension) vem
na Aula 4 — aqui é só o suficiente para ler a linha da grade abaixo sem decorar.

---

## Lista 2D (grade 10×10)

```python
LADO = 10
# CORRETO: list comprehension cria listas independentes
grade = [[0] * LADO for _ in range(LADO)]
grade[y][x] = 1     # convenção: linha (y) primeiro, coluna (x) depois

# ERRADO: [[0]*LADO]*LADO — todas as linhas são o mesmo objeto (aliasing)
```
⚠️ Armadilha: `grade[y][x]` — y primeiro, x depois. Robô em `(x=3,y=2)` → `grade[2][3]`.

---

## Tupla: registro imutável

```python
posicao = (3, 7)
x, y = posicao            # desempacota em uma linha
dx, dy = DELTAS['NORTE']  # (0, 1) — mesmo padrão

# Tupla como chave de dict (lista não pode — não é hashável)
obstaculos[(3, 7)] = True
```
⚠️ Armadilha: `posicao[0] = 5` gera `TypeError`. Crie nova tupla: `posicao = (5, posicao[1])`.

---

## Dicionário: criação e acesso

```python
robo = {'x': 0, 'y': 0, 'direcao': 'LESTE', 'trajetoria': [(0,0)]}
robo['x']                   # 0
robo.get('velocidade', 1)   # 1 — default seguro (sem KeyError)
'direcao' in robo           # True
robo['x'] += 1              # atualizar valor

for chave, valor in robo.items():
    print(chave, valor)
```
⚠️ Armadilha: `robo['chave_inexistente']` lança `KeyError`. Use `.get(chave, default)`.

---

## Dict: padrões do robô

```python
# Tabela de transição (substitui if/elif com 8 ramos)
GIRAR_ESQ = {'LESTE':'NORTE','NORTE':'OESTE','OESTE':'SUL','SUL':'LESTE'}
nova_dir = GIRAR_ESQ[robo['direcao']]   # uma linha

# Mapa esparso de obstáculos (eficiente para grades grandes)
obstaculos = {(3,2): True, (5,5): True}
if (nx, ny) in obstaculos: ...

# Tabela de deltas de movimento
DELTAS = {'LESTE':(1,0),'NORTE':(0,1),'OESTE':(-1,0),'SUL':(0,-1)}
dx, dy = DELTAS[robo['direcao']]
```
⚠️ Armadilha: `GIRAR_ESQ['NORDESTE']` → `KeyError`. Normalizar entrada com `.upper().strip()`.

---

## Contador com dict

```python
visitadas = {}
for pos in robo['trajetoria']:
    visitadas[pos] = visitadas.get(pos, 0) + 1   # padrão: d[k] = d.get(k,0) + 1
```
