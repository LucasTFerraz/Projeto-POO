# ── Lista: recap de operações que voltam hoje ───────────────────────
frutas = ["maçã", "banana", "cereja"]
print(frutas[0])            # "maçã"
print(frutas[-1])           # "cereja"
print(frutas[-2])           # "banana"
print(len(frutas))          # 3
print("banana" in frutas)   # True
frutas.append("uva")
print(frutas.pop())         # "uva" (remove e devolve o último)
print(frutas)                # ["maçã", "banana", "cereja"]

# ── Fatiamento (slicing): a peça que faltava para frutas[:] ─────────
frutas = ["maçã", "banana", "cereja", "uva"]
print(frutas[1:3])   # ["banana", "cereja"]  — índices 1 e 2, fim exclusivo
print(frutas[:2])    # ["maçã", "banana"]    — início omitido = começa do 0
print(frutas[2:])    # ["cereja", "uva"]     — fim omitido = vai até o final
print(frutas[:])     # cópia da lista inteira (fatia completa)

print("banana"[1:3])   # "an" — mesma notação funciona em string

# ── A armadilha do alias (caso simples) ─────────────────────────────
frutas = ["maçã", "banana", "cereja"]
outra = frutas               # "quero guardar uma cópia separada" — mas isso é alias!
frutas.append("uva")
print(outra)                  # ["maçã", "banana", "cereja", "uva"] — mudou junto (mesmo objeto)

outra = frutas[:]            # fatia completa — objeto novo
frutas.append("melancia")
print(outra)   # ["maçã", "banana", "cereja", "uva"] — não mudou, é objeto separado

# ── Trajetória: o mesmo alias, agora no robô ────────────────────────
x, y = 0, 0
trajetoria = [(x, y)]
x += 3
trajetoria.append((x, y))
x += 2
trajetoria.append((x, y))
print(trajetoria)   # [(0, 0), (3, 0), (5, 0)]

log = trajetoria          # mesmo objeto — já sabemos o que acontece
trajetoria.append((9, 0))
print(log)                # [(0, 0), (3, 0), (5, 0), (9, 0)] — mudou junto

log = trajetoria[:]       # cópia — objeto separado
trajetoria.append((9, 1))
print(log)   # [(0, 0), (3, 0), (5, 0), (9, 0)] — não mudou

# ── Grade 2D como lista de listas — o mesmo alias, uma casca a mais ─
LADO = 4
grade = [[0] * LADO] * LADO   # jeito ingênuo — previsão: funciona?
print(grade)                   # parece OK: [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
grade[0][0] = 9
print(grade)                   # TODAS as linhas viram [9,0,0,0] — as 4 linhas são o MESMO objeto

# Intuição de list comprehension 
print([0 for _ in range(5)])      # [0, 0, 0, 0, 0]      — _ porque o valor do range não importa
print([n**2 for n in range(5)])   # [0, 1, 4, 9, 16]      — aqui n importa, é elevado ao quadrado
print([fruta.upper() for fruta in frutas])
print([fruta[0] for fruta in frutas])
print([fruta for fruta in frutas])

grade = [[0] * LADO for _ in range(LADO)]   # jeito certo — 4 objetos independentes
grade[0][0] = 9
print(grade)                   # só a primeira linha muda: [[9,0,0,0], [0,0,0,0], ...]

LADO_GRADE = 10
grade = [[0] * LADO_GRADE for _ in range(LADO_GRADE)]
# convenção: grade[y][x] — linha (y) primeiro, coluna (x) depois
grade[2][3] = 1
print(f"grade[2][3] = {grade[2][3]}")   # grade[2][3] = 1

# ── Tupla: imutabilidade + desempacotamento ─────────────────────────
posicao = (3, 7)
print(posicao[0])       # 3
print(posicao[1])       # 7
print(len(posicao))     # 2

# Erro deliberado
# posicao[0] = 5   # TypeError: 'tuple' object does not support item assignment

pos_x, pos_y = posicao       # desempacota os dois valores de uma vez
print(pos_x)                  # 3
print(pos_y)                  # 7
pos_x, pos_y = 5, 2           # forma compacta — já usada na Aula 1
dx, dy = (1, 0)                # vai aparecer muito no robô v3

# ── Tupla como chave de dict ─────────────────────────────────────────
d = {}
d[(3, 7)] = "obstáculo"   # tupla como chave — funciona
print(d[(3, 7)])           # "obstáculo"

# Erro deliberado
# d[[3, 7]] = "x"   # TypeError: unhashable type: 'list'

# ── Dict básico: criação, acesso, métodos ───────────────────────────
pontos = {"Alice": 10, "Bob": 7, "Carol": 15}
print(pontos["Alice"])         # 10

# Erro deliberado 
# print(pontos["Zé"])   # KeyError: 'Zé'

print(pontos.get("Zé", 0))     # 0 (default seguro)
pontos["Alice"] = 12            # atualizar valor
print("Bob" in pontos)          # True
print("Xicó" in pontos)         # False
print(len(pontos))              # 3

for nome, pts in pontos.items():
    print(f"{nome}: {pts}")

# ── Mapa de obstáculos + tabela de frequência ───────────────────────
obstaculos = {(3, 2): True, (5, 5): True, (7, 1): True}

nx, ny = 3, 2
if (nx, ny) in obstaculos:
    print("Tem obstáculo em (3, 2)!")
print((4, 2) in obstaculos)   # False

visitadas = {}
posicoes = [(0, 0), (1, 0), (2, 0), (1, 0), (2, 0), (2, 0)]
for pos in posicoes:
    visitadas[pos] = visitadas.get(pos, 0) + 1
print(visitadas)   # {(0, 0): 1, (1, 0): 2, (2, 0): 3}

# ── Dict substituindo o if/elif de GIRAR + dict como estado do robô ─
GIRAR_ESQ = {
    "LESTE": "NORTE",
    "NORTE": "OESTE",
    "OESTE": "SUL",
    "SUL":   "LESTE",
}
GIRAR_DIR = {
    "LESTE": "SUL",
    "SUL":   "OESTE",
    "OESTE": "NORTE",
    "NORTE": "LESTE",
}

direcao = "NORTE"
lado = "ESQ"
if lado == "ESQ":
    direcao = GIRAR_ESQ[direcao]
elif lado == "DIR":
    direcao = GIRAR_DIR[direcao]
print(direcao)   # "OESTE"

DELTAS = {
    "LESTE":  ( 1,  0),
    "NORTE":  ( 0,  1),
    "OESTE":  (-1,  0),
    "SUL":    ( 0, -1),
}
direcao = "NORTE"
dx, dy = DELTAS[direcao]
nx, ny = 0 + dx, 0 + dy
print(f"Próxima posição: ({nx}, {ny})")   # (0, 1)

robo = {
    "x": 0,
    "y": 0,
    "direcao": "LESTE",
    "trajetoria": [(0, 0)],
}
print(f"Robô em ({robo['x']}, {robo['y']}), direção {robo['direcao']}")   # Robô em (0, 0), direção LESTE
