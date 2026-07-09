# Exercício integrador
# Complete os # TODO na ordem

from functools import reduce

# Enunciado — Relatório do log. Dado log (lista de dicts com x, y, status, comando), produzir um dict com:
# "coords_ok": lista de (x, y) dos passos bem-sucedidos (list comprehension com filtro)
# "visitas_por_celula": dict (x, y) → quantas vezes visitada (dict comprehension sobre um set, igual ao Bloco 1)
# "mais_visitada": a coordenada com mais visitas (max(..., key=...))
# "linhas": lista de strings "N. COMANDO → STATUS" para todos os passos (enumerate + zip + f-string)
# "total_passos_avancados": soma dos valores de todo comando AVANCAR (reduce, ou sum)


log = [
    {"x": 3, "y": 0, "comando": "AVANCAR 3",  "status": "OK"},
    {"x": 3, "y": 0, "comando": "GIRAR ESQ",  "status": "OK"},
    {"x": 3, "y": 2, "comando": "AVANCAR 5",  "status": "PAREDE"},
    {"x": 3, "y": 2, "comando": "GIRAR DIR",  "status": "OK"},
    {"x": 6, "y": 2, "comando": "AVANCAR 4",  "status": "PAREDE"},
    {"x": 6, "y": 2, "comando": "GIRAR ESQ",  "status": "OK"},
    {"x": 6, "y": 4, "comando": "AVANCAR 2",  "status": "OK"},
    {"x": 6, "y": 4, "comando": "GIRAR DIR",  "status": "OK"},
    {"x": 6, "y": 4, "comando": "AVANCAR 3",  "status": "PAREDE"},
]


def relatorio(log):
    # TODO: list comprehension com filtro — coordenadas (x, y) dos
    # passos com status "OK".
    coords_ok = None

    # TODO: dict comprehension sobre um set de posições — conta
    # quantas vezes cada (x, y) aparece no log (padrão do Bloco 1).
    visitas_por_celula = None

    # TODO: a coordenada com mais visitas — max(..., key=...) sobre
    # visitas_por_celula, sem precisar ordenar tudo.
    mais_visitada = None

    # TODO: lista de strings "N. COMANDO → STATUS" para cada
    # passo — combine enumerate com zip(comandos, resultados), start=1.
    linhas = None

    # TODO: soma dos valores de todo comando AVANCAR do log —
    # use reduce (ou sum, se preferir) sobre a lista de valores extraídos.
    total_passos_avancados = None

    return {
        "coords_ok": coords_ok,
        "visitas_por_celula": visitas_por_celula,
        "mais_visitada": mais_visitada,
        "linhas": linhas,
        "total_passos_avancados": total_passos_avancados,
    }


# TODO (tarefa de extensão — quem terminar rápido): acrescente ao
# dict devolvido por `relatorio` uma sexta chave, "revisitadas" — as
# coordenadas com mais de uma visita e sua contagem (dict comprehension
# sobre visitas_por_celula.items(), filtrando por contagem > 1).


if __name__ == "__main__":
    print(relatorio(log))
