# Tarefa de extensão
# Conta quantas vezes o robô foi bloqueado (vezes_bloqueado) e imprime o total
# junto da trajetória, ao final.

LADO_GRADE = 10
DELTAS    = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}
GIRAR_ESQ = {"LESTE": "NORTE", "NORTE": "OESTE", "OESTE": "SUL", "SUL": "LESTE"}
GIRAR_DIR = {"LESTE": "SUL", "SUL": "OESTE", "OESTE": "NORTE", "NORTE": "LESTE"}

obstaculos = {(3, 2): True, (5, 5): True, (7, 1): True}
robo = {"x": 0, "y": 0, "direcao": "LESTE", "trajetoria": [(0, 0)]}
comandos = ["AVANCAR 3", "GIRAR ESQ", "AVANCAR 5", "GIRAR DIR", "AVANCAR 4", "PARAR"]

vezes_bloqueado = 0

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
                vezes_bloqueado += 1
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
print(f"Vezes bloqueado: {vezes_bloqueado}")   # 2
