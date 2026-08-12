# Pré-aula 7 — Métodos especiais (dunder)

## O robô até aqui

`Robo` já protege o próprio estado: `x`, `y`, `bateria` e `direcao` são `@property`,
com setters que validam (recusam sair da grade) ou prendem (bateria entre 0 e 100).
`posicao` e `historico` são somente leitura.

## O problema que vamos resolver

Apesar de tudo isso, `print(robo1)` ainda mostra algo como
`<__main__.Robo object at 0x7f8a1c0b3d90>` — inútil para debugar. E se vocês
criarem dois robôs na mesma posição, `robo1 == robo2` dá `False`, mesmo que os dois
estejam exatamente no mesmo lugar. O Python simplesmente não sabe "imprimir um
robô" nem "comparar duas posições" — porque ninguém ensinou isso a ele ainda. Existe
um jeito de ensinar uma classe a se comportar como os tipos embutidos do Python
(`print`, `==`, `len`, `for`, `[]`)?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a assinatura completa do setter de `x` do
`Robo` (o `@property`/`@x.setter` da Aula 6): qual exceção ele levanta, e sob qual
condição. Depois, escreva de memória a diferença entre a estratégia usada em `x`
(recusar) e a usada em `bateria` (prender/*clamp*) — por que cada atributo usa uma
estratégia diferente. Compare com `notas/notas-aula-06-solucao.ipynb`.

## Leitura opcional

- Métodos especiais (visão geral) — Data model: https://docs.python.org/3/reference/datamodel.html#special-method-names
- `__repr__` vs `__str__` — Real Python: https://realpython.com/python-repr-vs-str/
- Iteradores — Tutorial oficial: https://docs.python.org/3/tutorial/classes.html#iterators
