# Robô v5 (solução) — flood fill: contar células alcançáveis
# Grade reduzida a 5×5 nesta aula (ver starter/robo_v4_completo.py).

LADO_GRADE = 5


def flood_fill(robo, visitadas, x, y):
    # CB 1: saiu da grade
    if x < 0 or x >= LADO_GRADE or y < 0 or y >= LADO_GRADE:
        return 0
    # CB 2: obstáculo
    if (x, y) in robo['obstaculos']:
        return 0
    # CB 3: já contamos esta célula
    if (x, y) in visitadas:
        return 0
    # Marcar ANTES de chamar vizinhos (impede ciclos)
    visitadas.add((x, y))
    conta = 1                                        # esta célula conta
    conta += flood_fill(robo, visitadas, x + 1, y)    # leste
    conta += flood_fill(robo, visitadas, x - 1, y)    # oeste
    conta += flood_fill(robo, visitadas, x,     y + 1)    # norte
    conta += flood_fill(robo, visitadas, x,     y - 1)    # sul
    return conta


def celulas_alcancaveis(robo):
    visitadas = set()
    return flood_fill(robo, visitadas, robo['x'], robo['y'])


# ── Testes (ver "Saída esperada" no roteiro) ───────────────
robo_livre = {'x': 0, 'y': 0, 'obstaculos': {}}
print(celulas_alcancaveis(robo_livre))          # 25 (grade 5x5 sem obstáculos)

robo_1_obstaculo = {'x': 0, 'y': 0, 'obstaculos': {(1, 1): True}}
print(celulas_alcancaveis(robo_1_obstaculo))    # 24

robo_parede = {
    'x': 0, 'y': 0,
    'obstaculos': {(2, 0): True, (2, 1): True, (2, 2): True, (2, 3): True, (2, 4): True},
}
print(celulas_alcancaveis(robo_parede))         # 10 (parede vertical em x=2)
