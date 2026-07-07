# Funções: def, parâmetros, retorno

LADO_GRADE = 10

posicao = (8,6)
px, py = posicao
if ((0 <= px < LADO_GRADE) and 
    (0 <= py < LADO_GRADE)):
    print(f'{posicao} é uma posição válida')
else:
    print(f'{posicao} é uma posição inválida')

def posicao_valida(x, y):
    return 0 <= x < LADO_GRADE and 0 <= y < LADO_GRADE

if posicao_valida(px,py):
    print(f'{posicao} é uma posição válida')
else:
    print(f'{posicao} é uma posição inválida')

print(posicao_valida(3, 5))    # True
print(posicao_valida(10, 0))   # False (10 == LADO_GRADE — limite exclusivo)
print(posicao_valida(-1, 5))   # False


# ── Retorno vs. print — o maior ponto de confusão ───────────────────
def saudacao_com_bug(nome):
    print(f"Olá, {nome}!")   # imprime, mas não retorna

resultado = saudacao_com_bug("Alice")
print(f"Resultado: {resultado}")   # Resultado: None — a função não usou return

def saudacao(nome):
    return f"Olá, {nome}!"

resultado = saudacao("Alice")
print(f"Resultado: {resultado}")   # Resultado: Olá, Alice!

print(type(posicao_valida(3, 5)))      # <class 'bool'>
print(type(saudacao_com_bug("Ana")))   # <class 'NoneType'>

def dobro(x):
    result = x * 2
    return          # return vazio → entrega None!
    return result   # nunca chega aqui
print(dobro(5))   # None

# ── Parâmetros com valor padrão ──────────────────────────────────────
def saudacao_com_padrao(nome, cumprimento="Olá"):
    return f"{cumprimento}, {nome}!"

print(saudacao_com_padrao("Ana"))         # "Olá, Ana!" — usa o padrão
print(saudacao_com_padrao("Ana", "Oi"))   # "Oi, Ana!"  — sobrescreve o padrão

# ── Erro deliberado: argumento padrão mutável ───────────────────────
def registrar(evento, lista_eventos=[]):   # BUG: mutável como default
    lista_eventos.append(evento)
    return lista_eventos

print(registrar("A"))   # ["A"] — parece OK
print(registrar("B"))   # ["A", "B"] — mesma lista da chamada anterior!

def registrar_corrigido(evento, lista_eventos=None):
    if lista_eventos is None:
        lista_eventos = []
    lista_eventos.append(evento)
    return lista_eventos

print(registrar_corrigido("A"))   # ["A"]
print(registrar_corrigido("B"))   # ["B"] — lista nova a cada chamada
