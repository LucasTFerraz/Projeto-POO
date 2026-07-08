def saudacao(nome):
    return f'Olá, {nome}'
def despedida(nome):
    return f'Tchau, {nome}'

# f = saudacao
# saudacao = 'Leopoldo'
# print(f('Leopoldo'))
# x = 'Ana'
# print(saudacao(x))
# print(type(x))
# print(type(saudacao))
# print(type(despedida))
# print('-----')
# v = saudacao
# print(type(v))
# print(v)
# print(saudacao)

# print(saudacao('Leopoldo'))
# print(v('Leopoldo'))

acoes = {
    'oi': saudacao,
    'tchau': despedida
}

print(acoes['oi']('Leopoldo'))
print(acoes['tchau']('Leopoldo'))