# Referência rápida — Recursão, Exceções e Arquivos

## Recursão: o padrão CB + CR

```python
def recursiva(problema):
    if <trivial>:                          # caso-base: responde sem se chamar
        return <resposta>
    return <parte> + recursiva(<menor>)   # caso-recursivo: problema menor

# Exemplo: fatorial
def fatorial(n):
    if n <= 1:                 # CB
        return 1
    return n * fatorial(n - 1)  # CR
```
⚠️ Armadilha: sem CB → `RecursionError: maximum recursion depth exceeded`.
Comece sempre pelos CBs. "Qual é o menor problema que respondo sem me chamar?"

---

## Visualizar a pilha com print de diagnóstico

```python
def fatorial(n):
    print(f"  -> fatorial({n})")    # subindo (empilhando)
    if n <= 1:
        return 1
    r = n * fatorial(n - 1)
    print(f"  <- fatorial({n}) = {r}")  # descendo (retornando)
    return r
```
`->` aparecem todos antes do primeiro `<-`. O CB é o que inverte o sentido.
Funciona para depurar qualquer função recursiva.

---

## Flood fill — exploração recursiva da grade

```python
def flood_fill(robo, visitadas, x, y):
    if x < 0 or x >= LADO_GRADE or y < 0 or y >= LADO_GRADE:
        return 0          # CB 1: fora da grade
    if (x, y) in robo['obstaculos']:
        return 0          # CB 2: obstáculo
    if (x, y) in visitadas:
        return 0          # CB 3: já contado
    visitadas.add((x, y))   # marcar ANTES de chamar os vizinhos
    return (1
            + flood_fill(robo, visitadas, x + 1, y)   # leste
            + flood_fill(robo, visitadas, x - 1, y)   # oeste
            + flood_fill(robo, visitadas, x,     y + 1)  # norte
            + flood_fill(robo, visitadas, x,     y - 1)) # sul

def celulas_alcancaveis(robo):
    return flood_fill(robo, set(), robo['x'], robo['y'])
```
⚠️ Armadilha: esquecer `visitadas.add` antes dos vizinhos → loop infinito → `RecursionError`.
`visitadas` é um `set` (busca O(1)); passado por referência — a mesma instância vai a todos os vizinhos.

---

## `try/except`: capturar exceções específicas

```python
def parsear_seguro(linha):
    try:
        partes = linha.split()
        acao = partes[0]
        valor = int(partes[1])
        return acao, valor
    except ValueError:       # int('ESQ') falha
        print(f"Valor inválido: {linha!r}")
        return None
    except IndexError:       # lista vazia ou curta demais
        print(f"Linha incompleta: {linha!r}")
        return None
```
⚠️ Armadilha: `except:` nu captura **tudo**, incluindo `NameError` e `TypeError` de bugs
de programação — esconde erros reais. Use sempre `except NomeDaExcecao:`.
Exceções são classes: começam com maiúscula (`ValueError`, não `valueerror`).

---

## Exceções customizadas (teaser da D2)

```python
class RoboError(Exception):
    pass

class ParedeError(RoboError):        # subclasse — categoria mais específica
    pass

def avancar_ou_reclamar(robo, novo_x):
    if not (0 <= novo_x < LADO_GRADE):
        raise ParedeError(f"bateu na parede leste em x={novo_x}")
    robo['x'] = novo_x

try:
    avancar_ou_reclamar(robo, 15)
except RoboError as erro:            # captura ParedeError (é subclasse de RoboError)
    print(f"Erro do robô: {erro}")
```
⚠️ Armadilha: `except ValueError` não captura `ParedeError` — só a classe pedida (e suas
subclasses) é capturada. `class X(Exception): pass` já é uma exceção válida e completa.

---

## Arquivos texto com `with open`

```python
# Ler linha a linha (rstrip remove o '\n' do fim de cada linha)
with open("programa.txt") as arq:
    for linha in arq:
        print(linha.rstrip())

# Ler tudo como lista de uma vez
with open("programa.txt") as arq:
    linhas = [linha.rstrip() for linha in arq]

# Gravar ("w" sobrescreve; "a" acrescenta ao fim)
with open("log.txt", "w") as log:
    for x, y in trajetoria:
        log.write(f"{x},{y}\n")

# Arquivo inexistente
try:
    with open("programa.txt") as arq:
        conteudo = arq.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
```
⚠️ `"w"` sobrescreve o arquivo (cria se não existir); `"a"` acrescenta; sem modo = `"r"` (leitura).
`with` fecha o arquivo automaticamente — mesmo que haja exceção. Não use `f.close()` manual.

---

## Funções são valores

```python
def saudacao(nome):
    return f"Olá, {nome}!"

f = saudacao          # sem parênteses: f guarda a função em si, não um resultado
print(f("Ana"))         # os parênteses aqui chamam a função guardada em f

acoes = {"OI": saudacao}       # dá pra guardar função como valor num dict...
print(acoes["OI"]("Ana"))      # ...e chamar depois de buscar pela chave
```
Isso é a base do **despacho por dicionário**: em vez de `if acao == "AVANCAR": ... elif ...`,
guarda-se `{"AVANCAR": avancar_n, "GIRAR": girar_delta}` e chama-se `tabela[acao](robo, valor)`.

---

## Capstone robô v6 — três responsabilidades

```python
def carregar_programa(caminho):        # 1. ler e parsear
    comandos = []
    try:
        with open(caminho) as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha or linha == "PARAR":
                    break
                cmd = parsear_seguro(linha)
                if cmd is not None:
                    comandos.append(cmd)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho!r}")
    return comandos

# avancar/girar esperam obstaculos + "ESQ"/"DIR", não o inteiro do parser —
# dois adaptadores finos traduzem, sem alterar avancar/girar:
def avancar_n(robo, passos):
    for _ in range(passos):
        if not avancar(robo, robo['obstaculos']):
            break

def girar_delta(robo, delta):
    if delta == 1:
        girar(robo, "DIR")
    elif delta == -1:
        girar(robo, "ESQ")

def executar(robo, comandos):          # 2. executar e acumular trajetória
    trajetoria = [(robo['x'], robo['y'])]
    tabela = {'AVANCAR': avancar_n, 'GIRAR': girar_delta}
    for acao, valor in comandos:
        if acao in tabela:
            tabela[acao](robo, valor)
            trajetoria.append((robo['x'], robo['y']))
    return trajetoria
```
`gravar_log(trajetoria)` é o passo 3 — igual ao bloco "Gravar" da seção de arquivos, acima.

```python
if __name__ == "__main__":
    ...   # só roda quando este arquivo é executado diretamente, não quando é importado
```
Convenção padrão do Python: separa "definições" (`def`, reaproveitáveis por quem importar o
arquivo) do "programa de verdade" (que não deve rodar sozinho ao importar).
