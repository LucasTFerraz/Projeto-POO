# Robô v6 — starter.
# v4 + flood fill + parser seguro + adaptadores já prontos. Complete os dois
# # TODO: carregar_programa e gravar_log. Ressincronize com
# solucao/robo_v6.py se precisar.

LADO_GRADE = 5
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

def flood_fill(robo, visitadas, x, y):
    if x < 0 or x >= LADO_GRADE or y < 0 or y >= LADO_GRADE:
        return 0
    if (x, y) in robo['obstaculos']:
        return 0
    if (x, y) in visitadas:
        return 0
    visitadas.add((x, y))
    conta = 1
    conta += flood_fill(robo, visitadas, x + 1, y)
    conta += flood_fill(robo, visitadas, x - 1, y)
    conta += flood_fill(robo, visitadas, x,     y + 1)
    conta += flood_fill(robo, visitadas, x,     y - 1)
    return conta

def celulas_alcancaveis(robo):
    visitadas = set()
    return flood_fill(robo, visitadas, robo['x'], robo['y'])

def parsear_seguro(linha):
    try:
        partes = linha.split()
        acao = partes[0]
        valor = int(partes[1])
        return acao, valor
    except ValueError:
        print(f"Valor não numérico na linha: {linha!r}")
        return None
    except IndexError:
        print(f"Linha mal formatada (esperado 'ACAO VALOR'): {linha!r}")
        return None

# `parsear_seguro` sempre devolve um inteiro como valor — passos (AVANCAR) ou
# delta de giro (GIRAR). `avancar`/`girar` acima não entendem inteiro direto,
# então dois adaptadores finos traduzem sem tocar nas funções do v4:
def avancar_n(robo, passos):
    for _ in range(passos):
        if not avancar(robo, robo['obstaculos']):
            break

def girar_delta(robo, delta):
    if delta == 1:
        girar(robo, "DIR")
    elif delta == -1:
        girar(robo, "ESQ")

def executar(robo, comandos):
    trajetoria = [(robo['x'], robo['y'])]
    tabela = {'AVANCAR': avancar_n, 'GIRAR': girar_delta}
    for acao, valor in comandos:
        if acao in tabela:
            tabela[acao](robo, valor)
            trajetoria.append((robo['x'], robo['y']))
    return trajetoria

def carregar_programa(caminho):
    comandos = []
    try:
        with open(caminho) as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha or linha == 'PARAR':
                    break
                cmd = parsear_seguro(linha)
                if cmd is not None:
                    comandos.append(cmd)
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {caminho}')
    return comandos

def gravar_log(trajetoria, caminho="log.txt"):
    with open(caminho, 'w') as log:
        for x,y in trajetoria:
            log.write(f'{x},{y}\n')
    print(f'Log gravado em {caminho} ({len(trajetoria)} posições).')

if __name__ == "__main__":
    robo = {
        'x': 0, 'y': 0, 'direcao': 'NORTE', 'trajetoria': [(0, 0)],
        'grade': [[0] * LADO_GRADE for _ in range(LADO_GRADE)],
        'obstaculos': {(2, 2): True},
    }

    programa = carregar_programa("programa.txt")
    trajetoria = executar(robo, programa)
    gravar_log(trajetoria)

    acessiveis = celulas_alcancaveis(robo)
    print(f"Robô terminou em ({robo['x']}, {robo['y']}), direção {robo['direcao']}.")
    print(f"Células alcançáveis a partir desta posição: {acessiveis}")
