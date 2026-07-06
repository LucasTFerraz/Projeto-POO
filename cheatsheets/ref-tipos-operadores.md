# Referência rápida — Tipos, operadores e conversões

## Variáveis e atribuição

```python
x = 0                    # guarda o valor 0 em x
x = x + 3               # lado direito calcula primeiro (→ 3), depois guarda em x
LADO_GRADE = 10          # constante: MAIÚSCULA = "não mude durante o programa"
```
⚠️ Armadilha: reatribuir descarta o valor anterior sem aviso. `x = 0; x = 5` → `x` é `5`.

---

## Tipos básicos

```python
type(0)           # <class 'int'>   — posição do robô (casas inteiras)
type(3.14)        # <class 'float'> — cálculos com decimal
type("LESTE")     # <class 'str'>   — direção como texto
type(True)        # <class 'bool'>  — resultado de comparação
```
⚠️ Armadilha: `type(10)` e `type("10")` são diferentes — o segundo é texto, não número.

---

## Conversões

```python
# input() SEMPRE devolve str — converter antes de calcular
passos = int(input("Passos para o leste: "))   # str → int

int("10")     # 10
float("3.5")  # 3.5
str(10)       # "10"
```
⚠️ Armadilha: `int("abc")` → `ValueError`. Todo texto que não é número inteiro quebra.

---

## Operadores aritméticos

```python
x + passos      # soma — andar para leste/norte
x - passos      # subtração — andar para oeste/sul (passos negativo)
passos * 2      # multiplicação
10 // 3         # divisão inteira → 3
10 % 3          # resto → 1
```
⚠️ Armadilha: `2 + 3 * 10` é `32`, não `50` — precedência é a da matemática. Use parênteses.

---

## Operadores de comparação (devolvem bool)

```python
novo_x < 0               # True se saiu pela parede oeste
novo_x >= LADO_GRADE     # True se saiu pela parede leste
x == 0                   # igualdade: DOIS sinais de igual
x != LADO_GRADE - 1      # diferente
0 <= x < LADO_GRADE      # encadeamento Python — dentro da grade
```
⚠️ Armadilha: `=` atribui, `==` compara. `if x = 5:` → `SyntaxError`.

---

## f-string (padrão do curso)

```python
print(f"Robô em ({x}, {y})")       # insere variáveis diretamente no texto
print(f"Passos dados: {passos}")    # qualquer expressão funciona dentro de {}
print(f"Destino: {x + passos}")    # expressão dentro das chaves
```
⚠️ Armadilha: esquecer o `f` antes das aspas → `{x}` sai como texto literal, não como valor.
