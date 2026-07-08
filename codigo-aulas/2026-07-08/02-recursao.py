# Recursão: caso-base e caso-recursivo 
# ── Sem caso-base — vai falhar de propósito (não descomentar) ──────
# def fatorial(n):
#     return n * fatorial(n - 1)   # vai explodir
#
# print(fatorial(5))   # RecursionError: maximum recursion depth exceeded


# 5! = 5 * 4 * 3 * 2 * 1
# 5! --> n
# = 5 * 4! --> n * (n-1)! 
# = 5 * 4 * 3!
# = 5 * 4 * 3 * 2!
# = 5 * 4 * 3 * 2 * 1!
# = 5 * 4 * 3 * 2 * 1



# ── Com caso-base — funciona ────────────────────────────────────────
def fatorial(n, DEBUG = False):
    if DEBUG:
        print(f' -> Iniciando a função fatorial({n})')
    if n<=1:                        # caso-base
        if DEBUG:
            print(f' <- caso-base: retorna 1')
        return 1
    resultado = n * fatorial(n-1)   # caso-recursivo
    if DEBUG:
        print(f' <- fatorial({n}) = {n} * fatorial({n-1}) = {resultado}')
    return resultado

print(fatorial(5))    # 120
print(fatorial(0))    # 1
print(fatorial(1))    # 1


# ── Visualizar a pilha — print de diagnóstico ───────────────────────
def fatorial_diagnostico(n):
    return fatorial(n, True)


print(fatorial_diagnostico(4))
# → prestes a calcular fatorial(4)
# → prestes a calcular fatorial(3)
# → prestes a calcular fatorial(2)
# → prestes a calcular fatorial(1)
# ← caso-base: retorna 1
# ← fatorial(2) = 2
# ← fatorial(3) = 6
# ← fatorial(4) = 24
# 24

# ── Soma de lista recursiva — ponte para o flood fill ───────────────
def soma_lista(lista_numeros):
    contador = 0
    for n in lista_numeros:
        contador = contador + n
    return contador
def soma_lista_recursiva(L):
    if len(L) == 0:                     # caso-base: lista vazia
        return 0
    return L[0] + soma_lista_recursiva(L[1:])     # caso-recursivo: primeiro + resto

print(soma_lista([3, 1, 4, 1, 5]))   # 14
print(soma_lista_recursiva([3, 1, 4, 1, 5]))   # 14
Lista = [1,2,3,4,5,6,7,8,9]
print(soma_lista(Lista))
print(soma_lista([1,2,3]))
print(soma_lista_recursiva(Lista))
print(soma_lista_recursiva([1,2,3]))

def fatorial_sem_recursao(n):
    if n>0:
        for num in range(n-1,0,-1):
            n = n*num
        return n
    return 1

# print(fatorial_sem_recursao(5))
# print(fatorial_sem_recursao(-5))