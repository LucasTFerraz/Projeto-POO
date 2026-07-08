# Robô v4 completo — início da Aula 3
# Herdado da Aula 2: cada operação é uma função,
# todas recebem `robo` como primeiro argumento — semente do `self` da D2.
# Grade reduzida a 5×5 nesta aula

LADO_GRADE = 4
DELTAS    = {"LESTE": (1, 0), "NORTE": (0, 1), "OESTE": (-1, 0), "SUL": (0, -1)}
GIRAR_ESQ = {"LESTE": "NORTE", "NORTE": "OESTE", "OESTE": "SUL", "SUL": "LESTE"}
GIRAR_DIR = {"LESTE": "SUL", "SUL": "OESTE", "OESTE": "NORTE", "NORTE": "LESTE"}
# obstaculos = {(1, 3): True, (2, 1): True}
obstaculos = {(1, 3): True, (1, 2): True, (2, 1): True, (3, 0): True}

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

def flood_fill(robo, visitadas, obstaculos, x, y):
    # Caso base 1 --> Fora da Grade (x ou y)
    if x < 0 or x >= LADO_GRADE or y < 0 or y >= LADO_GRADE:
        return 0
    # Caso base 2 --> (x,y) é um obstáculo
    if (x,y) in obstaculos:
        return 0
    # Caso base 3 --> já visitei (contei) esta célula
    if (x,y) in visitadas:
        return 0
    #Marcar a célula como visitada
    visitadas.add((x,y))
    conta = 1
    conta += flood_fill(robo, visitadas, obstaculos, x+1, y) # LESTE
    conta += flood_fill(robo, visitadas, obstaculos, x-1, y) # OESTE
    conta += flood_fill(robo, visitadas, obstaculos, x, y+1) # NORTE
    conta += flood_fill(robo, visitadas, obstaculos, x, y-1) # SUL
    return conta

def _busca(robo, visitadas, obstaculos, x, y, xd, yd):
    # Caso base 1 --> Fora da Grade (x ou y)
    if x < 0 or x >= LADO_GRADE or y < 0 or y >= LADO_GRADE:
        return False
    # Caso base 2 --> (x,y) é um obstáculo
    if (x,y) in obstaculos:
        return False
    # Caso base 3 --> já visitei (contei) esta célula
    if (x,y) in visitadas:
        return False
    if x == xd and y == yd:
        return True 
    #Marcar a célula como visitada
    visitadas.add((x,y))
    return (
        _busca(robo, visitadas, obstaculos, x+1, y, xd, yd) or # LESTE
        _busca(robo, visitadas, obstaculos, x-1, y, xd, yd) or # OESTE
        _busca(robo, visitadas, obstaculos, x, y+1, xd, yd) or # NORTE
        _busca(robo, visitadas, obstaculos, x, y-1, xd, yd)    # SUL
    )

def existe_caminho(robo, obstaculos, xd, yd):
    return _busca(robo, set(), obstaculos, robo['x'], robo['y'], xd, yd)    

def celulas_alcancaveis(robo, obstaculos):
    visitadas = set()
    return flood_fill(robo,visitadas,obstaculos,robo['x'],robo['y'])

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
        print(f"  [{acao}] Robô em ({robo['x']}, {robo['y']}), dir {robo['direcao']}")

r = criar_robo()
num_celulas_alcancaveis = celulas_alcancaveis(r, obstaculos)
print(f'Robô {r} alcança {num_celulas_alcancaveis} células na grade')

x, y = 3, 3
num_celulas_alcancaveis = flood_fill(r, set(), obstaculos, x, y)
print(f'{num_celulas_alcancaveis} células alcançáveis a partir de ({x},{y})')

xd, yd = 0, 3
print(f'Robô atualmente em ({r["x"]},{r["y"]}) consegue chegar em ({xd},{yd})? {existe_caminho(r, obstaculos, xd, yd)}')