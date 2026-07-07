# Robô v3 — grade 2D com obstáculos

LADO_GRADE = 10

DELTAS    = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}
GIRAR_ESQ = {"LESTE": "NORTE", "NORTE": "OESTE", "OESTE": "SUL", "SUL": "LESTE"}
GIRAR_DIR = {"LESTE": "SUL", "SUL": "OESTE", "OESTE": "NORTE", "NORTE": "LESTE"}

grade = [[0] * LADO_GRADE for _ in range(LADO_GRADE)]
obstaculos = {(3, 2): True, (5, 5): True, (7, 1): True}

robo = {"x": 0, "y": 0, "direcao": "LESTE", "trajetoria": [(0, 0)]}

comandos = ["AVANCAR 3", "GIRAR ESQ", "AVANCAR 5", "GIRAR DIR", "AVANCAR 4", "PARAR"]

for cmd in comandos:
    partes = cmd.strip().upper().split()
    acao = partes[0]
    if acao == "PARAR":
        print("Robô parou.")
        break
    elif acao == "AVANCAR":
        passos = int(partes[1])
        for _ in range(passos):
            dx, dy = DELTAS[robo["direcao"]]
            nx, ny = robo["x"] + dx, robo["y"] + dy
            if (0 <= nx < LADO_GRADE and
                0 <= ny < LADO_GRADE and
                (nx, ny) not in obstaculos):
                robo["x"], robo["y"] = nx, ny
                robo["trajetoria"].append((nx, ny))
            else:
                print(f"  Bloqueado em ({robo['x']}, {robo['y']})")
                break
    elif acao == "GIRAR":
        lado = partes[1]
        if lado == "ESQ":
            robo["direcao"] = GIRAR_ESQ[robo["direcao"]]
        elif lado == "DIR":
            robo["direcao"] = GIRAR_DIR[robo["direcao"]]
    print(f"  [{acao}] Robô em ({robo['x']}, {robo['y']}), direção {robo['direcao']}")

print(f"Trajetória: {robo['trajetoria']}")

# Saída esperada:
#   [AVANCAR] Robô em (3, 0), direção LESTE
#   [GIRAR] Robô em (3, 0), direção NORTE
#   Bloqueado em (3, 1)
#   [AVANCAR] Robô em (3, 1), direção NORTE
#   [GIRAR] Robô em (3, 1), direção LESTE
#   Bloqueado em (6, 1)
#   [AVANCAR] Robô em (6, 1), direção LESTE
# Robô parou.
# Trajetória: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (6, 1)]

# Bônus (ver roteiro, [100:00]) — imprimir o tabuleiro:
for linha_y in range(LADO_GRADE - 1, -1, -1):   # de cima (y alto) para baixo
    for col_x in range(LADO_GRADE):
        pos = (col_x, linha_y)
        if pos == (robo["x"], robo["y"]):
            print("R", end=" ")
        elif pos in obstaculos:
            print("X", end=" ")
        elif pos in set(robo["trajetoria"]):
            print(".", end=" ")
        else:
            print("_", end=" ")
    print()
