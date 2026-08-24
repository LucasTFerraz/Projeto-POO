# Referência rápida — Variabilidade e Linha de Produtos de Software

## Modelo de features: mandatória, opcional, alternativa

```python
TIPOS_VALIDOS = set(Robo._registro)          # alternativa: escolhe exatamente uma
ESTRATEGIAS_VALIDAS = {"padrao", "esquiva", "zigzag"}   # alternativa também

# opcional: 0 ou N observadores plugados
# mandatória: Sensor sempre existe; só o parâmetro (alcance) varia
```
⚠️ Armadilha: `set(Robo._registro)` é um **retrato**, tirado no instante em que a
linha roda — uma subclasse definida **depois** não aparece nele. Pra validação de
verdade, consulte `Robo._registro` direto, não uma cópia guardada antes.

---

## `requires`/`excludes`: restrições entre features

```python
EXCLUI = {
    "RoboBlindado": {"zigzag"},              # RoboBlindado não aceita zigzag
}
REQUER = {
    "RoboExplorador": {"zigzag", "esquiva"},  # exige UMA destas — nunca "padrao" sozinho
}
```
⚠️ Armadilha: `EXCLUI`/`REQUER` sozinhos não impedem nada — são só dados. Sem um
validador que os leia, é documentação que ninguém é obrigado a respeitar.

---

## Validador de configuração — recusar antes de instanciar

```python
class ConfiguracaoInvalida(Exception):
    pass

def validar_configuracao(tipo_nome, estrategia_nome):
    if tipo_nome not in Robo._registro:
        raise ConfiguracaoInvalida(f"tipo desconhecido: {tipo_nome!r}")
    if estrategia_nome in EXCLUI.get(tipo_nome, set()):
        raise ConfiguracaoInvalida(f"{tipo_nome} exclui a estratégia {estrategia_nome!r}")
    exigidas = REQUER.get(tipo_nome)
    if exigidas and estrategia_nome not in exigidas:
        raise ConfiguracaoInvalida(f"{tipo_nome} exige uma destas: {sorted(exigidas)}")

def criar_robo_configurado(tipo_nome, nome, estrategia_nome="padrao", **kwargs):
    validar_configuracao(tipo_nome, estrategia_nome)   # ANTES de criar qualquer coisa
    robo = criar_robo(tipo_nome, nome, **kwargs)
    robo.estrategia = FABRICA_ESTRATEGIAS[estrategia_nome]()
    return robo
```
⚠️ Armadilha: validar **depois** de instanciar deixa o objeto inválido existir por
um instante antes da exceção — valide sempre antes de qualquer efeito colateral
irreversível.

---

## *Binding time*: quando a escolha é resolvida

```python
Robo._registro                 # resolvido em tempo de DEFINIÇÃO (__init_subclass__, Aula 8)
criar_robo("RoboVeloz", ...)   # resolvido em tempo de EXECUÇÃO (o nome só chega em runtime)
```
⚠️ Armadilha: "ponto de variação" e "quando ele é resolvido" são perguntas
diferentes. Herança fixa o catálogo de variantes em tempo de definição, mas ainda
precisa de uma decisão em runtime pra escolher **qual** instanciar.
