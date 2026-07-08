# Tarefa de extensão
# Adapta celulas_alcancaveis para também devolver a lista de células
# visitadas, e usa isso para imprimir um mapa da grade (* alcançadas,
# # obstáculos).

LADO_GRADE = 5


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


def celulas_alcancaveis_com_mapa(robo):
    visitadas = set()
    total = flood_fill(robo, visitadas, robo['x'], robo['y'])
    return total, visitadas


def imprimir_mapa(robo, visitadas):
    for y in range(LADO_GRADE - 1, -1, -1):     # de cima para baixo
        linha = []
        for x in range(LADO_GRADE):
            if (x, y) in robo['obstaculos']:
                linha.append("#")
            elif (x, y) in visitadas:
                linha.append("*")
            else:
                linha.append(".")
        print(" ".join(linha))


robo = {
    'x': 0, 'y': 0,
    'obstaculos': {(2, 0): True, (2, 1): True, (2, 2): True, (2, 3): True, (2, 4): True},
}
total, visitadas = celulas_alcancaveis_com_mapa(robo)
print(f"Total alcançável: {total}")   # 10
imprimir_mapa(robo, visitadas)
