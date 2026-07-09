# enumerate e zip

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
# i = 1
# for linha in log: 
#     print(f'Linha #{i} {linha}')
#     i = i + 1

# for i, linha in enumerate(log, start=1):
#     print(f'Linha #{i} {linha}')

# zip
nomes = ['Ana', 'Bruno', 'Carla']
notas = [ 8.5 ,  6.0   ,  9.2]
print(list(zip(nomes,notas)))
cidades = ['Recife', 'Caruaru', 'Olinda']
print(list(zip(nomes,notas,cidades)))

print(dict(zip(nomes,notas)))

a = [1,2,3]
b = [10,20,30]
somas = [x+y for x,y in zip(a,b)]
print(type(somas))
print(len(somas))
print(somas)

comandos_enviados = [p['comando'] for p in log]
resultados = [p['status'] for p in log]
print(comandos_enviados)
print(resultados)
for cmd, res in zip(comandos_enviados, resultados):
    print(f'{cmd} --> {res}')