# possível linha é a string "AVANCAR 4"
def parsear(linha):
    partes = linha.strip().upper().split()
    acao = partes[0]
    valor = int(partes[1])
    return acao, valor

# print(parsear("AVANCAR 4"))
# print(parsear("GIRAR ESQ"))
# print(parsear(""))

def parsear_seguro_v1(linha):
    try:    
        partes = linha.strip().upper().split()
        acao = partes[0]
        valor = int(partes[1])
        return acao, valor
    except:
        print(f'Comando inválido (ignorado): {linha}')
        return None

# print(parsear_seguro_v1("AVANCAR 4"))
# print(parsear_seguro_v1("GIRAR ESQ"))
# print(parsear_seguro_v1(""))

def parsear_seguro_v2(linha):
    try:    
        partes = linha.strip().upper().split()
        acao = partes[0]
        valor = int(partes[1])
        return acao, valor
    except ValueError:
        print(f'Valor não numérico na linha: {linha}')
        return None
    except IndexError:
        print(f'Linha mal formatada (esperado "ACAO VALOR"): {linha}')
        return None

# print(parsear_seguro_v2("AVANCAR 4"))
# print(parsear_seguro_v2("GIRAR ESQ"))
# print(parsear_seguro_v2("GIRAR 1"))
# print(parsear_seguro_v2(""))

arq = 'arquivo_inexistente.txt'
try:
    with open(arq) as f:
        conteudo = f.read()
except FileNotFoundError:
    print(f'O arquivo {arq} não foi encontrado!')

class RoboError(Exception):
    pass
class ParedeError(RoboError):
    pass

LADO_GRADE = 10

def avancar_ou_reclamar(robo, novo_x):
    if not(0 <= novo_x < LADO_GRADE):
        # print(f'Bateu na parede leste em x={novo_x}')
        raise ParedeError(f'Bateu na parede leste em x={novo_x}')
    else:
        robo['x'] = novo_x
robo = {'x':0,'y':0}
print(robo['x'])

try:
    avancar_ou_reclamar(robo, 8)
    print(robo['x'])
    avancar_ou_reclamar(robo, 15)
    print(robo['x'])    
except ParedeError as erro:
    print(f'Erro do robô: {erro}')