# map e filter

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

#map 
# -> recebe uma função f e uma lista L e 
#    aplica f a todos os elementos de L
# -> como resultado, devolve uma lista do mesmo tamanho

numeros = [1,2,3,4]
x = 1
s = str(x)
print(x, type(x))
print(s, type(s))
print(numeros, type(numeros), id(numeros))
numeros_str = list(map(str,numeros))
print(numeros_str, type(numeros_str), id(numeros_str))
numeros_int = list(map(int,numeros_str))
print(numeros_int, type(numeros_int), id(numeros_int))

def multiplica_por_5(n):
    return n*5

f = lambda n: n*5

print(list(map(multiplica_por_5, numeros)), type(multiplica_por_5))
print(list(map(f, numeros)), type(f))
print(list(map(lambda n: n*5, numeros)), type(lambda n: n*5))
print([n*5 for n in numeros])

# filter -> recebe uma função f e uma lista L
#           e com base no retorno de f (T ou F)
#           decide se o elemento fica ou sai

def par(n):
    return n%2==0

print(list(filter(par, numeros)))
print(list(filter(lambda n: n%2 == 0, numeros)))
print(list(filter(str.isdigit, ['12', 'ab', '3a', '42', 'c3'])))