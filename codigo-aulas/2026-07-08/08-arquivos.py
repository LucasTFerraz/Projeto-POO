with open('programa.txt') as arq:
    linhas = [linha.strip() for linha in arq]
    # for linha in arq:
    #     print(linha.strip())
print(linhas)

trajetoria = [(0,0), (1,0), (2,0), (2,1), (3,1)]
with open('log.txt', 'w') as log:
    for x,y in trajetoria:
        log.write(f'{x},{y}\n')
print('Log gravado em arquivo.')