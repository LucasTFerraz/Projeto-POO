# # Comprehensions

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

limiar = 3
grandes = [ p['comando'] for p in log
            if p['comando'].startswith('AVANCAR') and
               int(p['comando'].split()[1]) > limiar
          ]
print(grandes)

limiar = 3
palavras = ['ana','bruno','cid','daniela','edu']
tamanhos = { p : len(p) for p in palavras if len(p) > limiar}
print(tamanhos)