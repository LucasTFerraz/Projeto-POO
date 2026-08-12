# Referência rápida — Métodos especiais (dunder)

## `__repr__`/`__str__`: dois níveis de representação

```python
class Robo:
    def __repr__(self):
        return f"Robo({self.nome!r}, x={self.x}, y={self.y})"   # para quem programa

    def __str__(self):
        return f"{self.nome} em ({self.x}, {self.y})"           # para quem lê
```
⚠️ Armadilha: dentro de listas/tuplas/dicts, o Python **sempre** usa `__repr__` dos
itens, nunca `__str__` — mesmo que o objeto tenha os dois definidos.

---

## `__eq__`: comparar por valor, com guarda

```python
class Posicao:
    def __eq__(self, outra):
        if not isinstance(outra, Posicao):
            return NotImplemented
        return self.x == outra.x and self.y == outra.y
```
⚠️ Armadilha: sem `__eq__`, `==` compara **identidade** (`is`), não conteúdo — dois
robôs com o mesmo `x`/`y` dão `False`. E sem o `isinstance`, comparar com um tipo
inesperado (`robo1 == (3, 4)`) estoura `AttributeError` em vez de devolver `False`.

---

## `__len__`: medir com `len()`

```python
class Robo:
    def __len__(self):
        return len(self.trajetoria)   # posições visitadas
```
⚠️ Armadilha: `__len__` sempre precisa devolver um `int >= 0` — devolver negativo
(ou qualquer coisa que não seja inteiro) quebra com `ValueError`/`TypeError` na hora.

---

## `__iter__`: percorrer com `for`

```python
class Robo:
    def __iter__(self):
        return iter(self.trajetoria)   # cria um iterador NOVO a cada chamada
```
⚠️ Armadilha: `__iter__` precisa devolver um **iterador**, não só algo iterável —
`return self.trajetoria` (a lista, sem `iter()`) quebra com `TypeError: iter()
returned non-iterator`.

---

## `__getitem__`/`__contains__`: indexar com `[]` e testar com `in`

```python
class Grade:
    def __getitem__(self, pos):
        return "X" if pos in self.obstaculos else "."

    def __contains__(self, pos):
        return pos in self.obstaculos    # deixa "pos in grade" funcionar
```
⚠️ Armadilha: `__getitem__` não valida nada por padrão — `grade[999]` (índice sem
sentido) não dá erro, só devolve o valor "não encontrado" calado. Se quiser recusar
índices inválidos, a validação precisa ser escrita à mão.
