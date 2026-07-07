# Robô v4 
# Liberado ao fim do teste integrado. Todas as funções que operam sobre o robô
# recebem `robo` como primeiro argumento — semente do `self` (ver roteiro, [88:00]).

LADO_GRADE = 10
DELTAS    = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}
GIRAR_ESQ = {"LESTE": "NORTE", "NORTE": "OESTE", "OESTE": "SUL", "SUL": "LESTE"}
GIRAR_DIR = {"LESTE": "SUL", "SUL": "OESTE", "OESTE": "NORTE", "NORTE": "LESTE"}

def posicao_valida(x, y):
    return 0 <= x < LADO_GRADE and 0 <= y < LADO_GRADE


def criar_robo(x=0, y=0, direcao="LESTE"):
    return {"x": x, "y": y, "direcao": direcao, "trajetoria": [(x, y)]}


def sensor_frente(robo, obstaculos):
    dx, dy = DELTAS[robo["direcao"]]
    nx, ny = robo["x"] + dx, robo["y"] + dy
    return posicao_valida(nx, ny) and (nx, ny) not in obstaculos


def avancar(robo, obstaculos):
    if sensor_frente(robo, obstaculos):
        dx, dy = DELTAS[robo["direcao"]]
        robo["x"] += dx
        robo["y"] += dy
        robo["trajetoria"].append((robo["x"], robo["y"]))
        return True
    return False


def girar(robo, lado):
    if lado == "ESQ":
        robo["direcao"] = GIRAR_ESQ[robo["direcao"]]
    elif lado == "DIR":
        robo["direcao"] = GIRAR_DIR[robo["direcao"]]


def executar(robo, obstaculos, comandos):
    for cmd in comandos:
        partes = cmd.strip().upper().split()
        acao = partes[0]
        if acao == "PARAR":
            print("Robô parou.")
            break
        elif acao == "AVANCAR":
            passos = int(partes[1])
            for _ in range(passos):
                if not avancar(robo, obstaculos):
                    print(f"  Bloqueado em ({robo['x']}, {robo['y']})")
                    break
        elif acao == "GIRAR":
            girar(robo, partes[1])
        elif acao == "SENSOR":
            livre = sensor_frente(robo, obstaculos)
            print(f"  Sensor: {'LIVRE' if livre else 'BLOQUEADO'}")
        print(f"  [{acao}] Robô em ({robo['x']}, {robo['y']}), dir {robo['direcao']}")

# ── Testes ao vivo dos segmentos [44:00]–[70:00] (ver "Saída esperada" no roteiro) ──
obstaculos = {(3, 2): True, (5, 5): True, (7, 1): True}

r = criar_robo(3, 1, "NORTE")        # aponta para (3,2) — tem obstáculo
print(sensor_frente(r, obstaculos))  # False
r2 = criar_robo(0, 0, "LESTE")
print(sensor_frente(r2, obstaculos))  # True

r = criar_robo(0, 0, "LESTE")
print(avancar(r, obstaculos))    # True
print(r["x"], r["y"])            # 1 0

r = criar_robo()
print(r["direcao"])   # LESTE
girar(r, "ESQ")
print(r["direcao"])   # NORTE
girar(r, "DIR")
print(r["direcao"])   # LESTE

# ── Teste integrado ─────────────────────────────────────────────────
robo = criar_robo()
comandos = ["AVANCAR 3", "GIRAR ESQ", "AVANCAR 5", "GIRAR DIR", "AVANCAR 4", "PARAR"]
executar(robo, obstaculos, comandos)
print(f"Posição final: ({robo['x']}, {robo['y']})")
print(f"Trajetória: {robo['trajetoria']}")

# Saída esperada do teste integrado:
#   [AVANCAR] Robô em (3, 0), dir LESTE
#   [GIRAR] Robô em (3, 0), dir NORTE
#   Bloqueado em (3, 1)
#   [AVANCAR] Robô em (3, 1), dir NORTE
#   [GIRAR] Robô em (3, 1), dir LESTE
#   Bloqueado em (6, 1)
#   [AVANCAR] Robô em (6, 1), dir LESTE
# Robô parou.
# Posição final: (6, 1)
# Trajetória: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1), (6, 1)]
