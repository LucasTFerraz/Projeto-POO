# # Comprehensions

# log = [
#     {"x": 3, "y": 0, "comando": "AVANCAR 3",  "status": "OK"},
#     {"x": 3, "y": 0, "comando": "GIRAR ESQ",  "status": "OK"},
#     {"x": 3, "y": 2, "comando": "AVANCAR 5",  "status": "PAREDE"},
#     {"x": 3, "y": 2, "comando": "GIRAR DIR",  "status": "OK"},
#     {"x": 6, "y": 2, "comando": "AVANCAR 4",  "status": "PAREDE"},
#     {"x": 6, "y": 2, "comando": "GIRAR ESQ",  "status": "OK"},
#     {"x": 6, "y": 4, "comando": "AVANCAR 2",  "status": "OK"},
#     {"x": 6, "y": 4, "comando": "GIRAR DIR",  "status": "OK"},
#     {"x": 6, "y": 4, "comando": "AVANCAR 3",  "status": "PAREDE"},
# ]

# # for linha in log:
# #     print(f'({linha['x']},{linha['y']})')
# ## (3,0)
# ## (3,0)
# ## (3,2)
# ## ...
# ## (6,6)

# # coords = [ f'({linha['x']},{linha['y']})' for linha in log ]
# # print("\n".join(coords))

# # for linha in log:
# #     if linha['status'] == 'OK':
# #         print(f'({linha['x']},{linha['y']})')

# coords = [ f'({linha['x']},{linha['y']})' for linha in log if linha['status'] == 'OK']
# print(coords)
# print(len(coords))

# # #Atomos de Confusao
# # # x = (y>0 ? 'ok' : 'erro');
# # # if y>0:
# # #   x = 'ok'
# # # else:
# # #   x = 'erro'
# # y = 0
# # # x = 'ok' if y > 0 else 'erro'
# # x = 'ok' if y > 0 else None
# # print(x)

# ## ---
# lista_x = [p['x'] for p in log]
# print(lista_x)
# print(type(lista_x))

# tupla_x = (p['x'] for p in log)
# print(tupla_x)
# print(type(tupla_x))

# tupla_x = tuple((p['x'] for p in log))
# print(tupla_x)
# print(type(tupla_x))
# tupla_status = tuple((p['status'] for p in log))
# print(tupla_status)

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
coords = [ (linha['x'],linha['y']) for linha in log ]
print(coords)
print(coords.count((6,4)))
contagem = { pos : coords.count(pos) for pos in set(coords) }
# contagem = { pos : coords.count(pos) for pos in coords }
print(contagem)
mais_visitada = max(contagem, key=contagem.get)
print(mais_visitada, contagem[mais_visitada])
print(max(contagem))
print(max([2,4,1,5,3,8,6,9]))
# mapa = { (p['x'],p['y']) : p['status'] for p in log }
# print(mapa)
# print(type(mapa))
# print(len(mapa))

# def dobro(n):
#     return n*2
# l = [1,2,3,4,5,6,7,8,9]
# ao_quadrado = {e : e**2 for e in l}
# dobrado = {e : dobro(e) for e in l}
# print(ao_quadrado)
# print(dobrado)

# capitais = {'PE':'Recife', 'CE':'Fortaleza', 'BA':'Salvador', 'RJ':'Rio de Janeiro'}
# inverter = {cidade : uf for uf,cidade in capitais.items()}
# print(capitais)
# print(inverter)