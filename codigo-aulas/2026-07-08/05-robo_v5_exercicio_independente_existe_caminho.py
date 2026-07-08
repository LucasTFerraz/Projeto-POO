# Exercício
# existe_caminho(robo, xd, yd): adapta o flood fill para parar ao achar o
# destino, em vez de contar todas as células alcançáveis.

LADO_GRADE = 5


def _busca(robo, visitadas, x, y, xd, yd):
    if x < 0 or x >= LADO_GRADE or y < 0 or y >= LADO_GRADE:
        return False
    if (x, y) in robo['obstaculos']:
        return False
    if (x, y) in visitadas:
        return False
    if x == xd and y == yd:
        return True
    visitadas.add((x, y))
    return (_busca(robo, visitadas, x + 1, y, xd, yd) or
            _busca(robo, visitadas, x - 1, y, xd, yd) or
            _busca(robo, visitadas, x,     y + 1, xd, yd) or
            _busca(robo, visitadas, x,     y - 1, xd, yd))


def existe_caminho(robo, xd, yd):
    return _busca(robo, set(), robo['x'], robo['y'], xd, yd)


# Parede vertical em x=2 (todo o eixo y) — divide a grade em dois lados
robo = {
    'x': 0, 'y': 0,
    'obstaculos': {(2, 0): True, (2, 1): True, (2, 2): True, (2, 3): True, (2, 4): True},
}
print(existe_caminho(robo, 1, 1))   # True  — mesmo lado da parede
print(existe_caminho(robo, 4, 4))   # False — do outro lado da parede
