
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

x = 2
y = 3
z = 4
w = 7
print(x, y, z, w,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print('Olá mundo')
print('Olá', 'mundo')
print()
print('Teste')

def somar_numeros_lista(L):
    resultado = 0
    for e in L:
        resultado = resultado + e
    return resultado #sum(L)

### somar_numeros(n1,n2,n3,n4...)
def somar_numeros(*numeros): ## *args
    # print(type(numeros))
    resultado = 0
    for e in numeros:
        resultado = resultado + e
    return resultado #sum(numeros)

print(somar_numeros_lista([1,2,3,4,5,6]))
# print( somar_numeros_lista(1,2,3,4,5,6) ) # ERRO
print( somar_numeros(1,2,3,4,5,6) ) # somar_numeros( (1,2,3,4,5,6) )
print( somar_numeros(1,2) ) 
print( somar_numeros() ) 
print( somar_numeros(*[1,2,3]) ) 

# L1 = [1,2,3]
# T1 = *[1,2,3]


def concatenar_listas(*listas):
    resultado = []
    for lista in listas:
        resultado = resultado + lista
    return resultado
print( concatenar_listas([1,2],[3,4],[3,4],[3,4],[3,4],[3,4]) ) 


def saudacao(nome, cumprimento='Olá', pontuacao = '!'):
    return f'{cumprimento} {nome}{pontuacao}'
print(saudacao('Leopoldo'))
print(saudacao('Leopoldo', 'Oi'))
print(saudacao('Leopoldo', 'Oi', '.'))
print(saudacao('Leopoldo', pontuacao='?', cumprimento='E aí'))

def criar_perfil(**dados): 
    return dados

print(criar_perfil(nome='Leopoldo', cidade='Recife', uf='PE'))
print(criar_perfil(nome='Leopoldo', uf='PE'))
print(criar_perfil(nome='Leopoldo'))

def configurar_robo(**opcoes):
    direcao = opcoes.get('direcao', 'LESTE')
    inicio = (opcoes.get('x',0), opcoes.get('y',0))
    return direcao, inicio

print(configurar_robo())
print(configurar_robo(direcao = 'OESTE'))
print(configurar_robo(x = 4))
print(configurar_robo(y = 2, direcao = 'SUL', x = 3))
d = { 'x' : 5 , 'y' : 4}
print(configurar_robo(x = d['x'], y = d['y'], direcao = 'NORTE'))