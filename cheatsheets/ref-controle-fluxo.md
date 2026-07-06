# Referência rápida — Controle de fluxo

## Booleanos: and / or / not

```python
# and: os DOIS precisam ser True
0 <= novo_x and novo_x < LADO_GRADE   # True se dentro da grade (forma explícita)
0 <= novo_x < LADO_GRADE              # True — encadeamento Python (preferido)

# or: basta UM ser True
novo_x < 0 or novo_x >= LADO_GRADE   # True se fora da grade

# not: inverte
not (0 <= novo_x < LADO_GRADE)        # True se fora da grade (igual ao or acima)
```
⚠️ Armadilha: `not x > 0` aplica `not` a `x` antes de comparar. Use parênteses: `not (x > 0)`.

---

## if / elif / else

```python
novo_x = x + passos         # calcula o DESTINO antes de decidir

if novo_x < 0:
    print("Parede oeste!")       # bateu à esquerda
elif novo_x >= LADO_GRADE:
    print("Parede leste!")       # bateu à direita
else:
    x = novo_x                   # cabe — atualiza a posição
    print(f"Robô em ({x}, {y})")
```
⚠️ Armadilha: esquecer `:` no final do `if`/`elif`/`else` → `SyntaxError`.  
⚠️ Armadilha: indentação com tab + espaço misturados → `IndentationError`. Use 4 espaços.

---

## if/elif vs. ifs independentes

```python
# IFs INDEPENDENTES: todos são avaliados (use quando as perguntas não se excluem)
if x == 0:   print("borda oeste")
if y == 0:   print("borda sul")    # roda mesmo que o anterior tenha sido True

# ESCADA if/elif: para no PRIMEIRO verdadeiro (use quando os casos se excluem)
if novo_x < 0:
    print("oeste")
elif novo_x >= LADO_GRADE:
    print("leste")      # só avaliado se o if anterior foi False
else:
    x = novo_x
```
Regra: casos que se **excluem mutuamente** → `if/elif`. Perguntas **independentes** → `if` separados.

---

---

## `for` com range e lista

```python
for i in range(5):          # 0, 1, 2, 3, 4  — fim é exclusivo
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1  (passo negativo)
    print(i)

for cmd in comandos:        # sem índice — Pythônico
    print(cmd)

for _ in range(passos):     # _ = índice não usado
    x += 1
```
⚠️ Armadilha: `range(10)` vai de 0 a **9**, não de 1 a 10. `range(n)` tem `n` elementos.

---

## `while` com sentinela e `break`

```python
# Padrão sentinela — para quando a condição de saída é complexa
while True:
    cmd = ler_proximo_comando()
    if cmd == 'PARAR':
        break
    executar(cmd)

# Forma alternativa — quando a condição é simples
while x < LADO_GRADE:
    x += 1
```
⚠️ Armadilha: esquecer o `break` cria loop infinito (Ctrl+C para sair). Nunca coloque `break` dentro de `if verdadeiro_desde_o_início`.

---

## Strings: métodos para o parser

```python
s = '  avancar  3  '
s.strip()                    # 'avancar  3'   — remove espaços das bordas
s.strip().upper()            # 'AVANCAR  3'   — converte para maiúsculas
s.strip().upper().split()    # ['AVANCAR', '3'] — divide por espaços

partes = 'AVANCAR 3'.split()
acao  = partes[0]            # 'AVANCAR'
valor = int(partes[1])       # 3  (split devolve str — converter com int!)

'AVAN' in 'AVANCAR'         # True  — checar substring
len('NORTE')                # 5     — comprimento
'NORTE'[0]                  # 'N'   — indexação (imutável: não dá atribuir)
```
⚠️ Armadilha: strings são **imutáveis** — `s[0] = 'X'` gera `TypeError`. Construa nova string.
