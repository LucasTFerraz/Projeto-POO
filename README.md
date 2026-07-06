# Curso de Python — Residência em Robótica e IA
## Material do estudante · CIn/UFPE–Softex

Este repositório contém o material de apoio das aulas. Ao longo do curso vamos construir,
peça por peça, um robô que anda numa grade, decide para onde ir, lê um programa de um
arquivo e registra por onde passou. Cada aula deixa o robô mais esperto.

---

## Setup inicial (fazer uma vez)

**1. Clonar o repositório**
```bash
git clone <URL-do-repo> residencia-python-alunos
cd residencia-python-alunos
```

**2. Verificar Python**
```bash
python --version    # ou python3 --version
# Precisa ser 3.8 ou superior
```

**3. Abrir no VS Code**
```bash
code .
```
Quando o VS Code perguntar sobre instalar a extensão Python → instalar.
Quando pedir para selecionar o interpretador → escolher Python 3.x.
Ao abrir o primeiro arquivo `.ipynb` (pasta `notas/`), o VS Code vai sugerir instalar a
extensão **Jupyter** (da Microsoft) → instalar também. É ela que permite rodar os notebooks
direto no editor, sem precisar de um servidor Jupyter separado.

**Plano B (se der problema na instalação):** acesse https://pythontutor.com ou
use o Python online em https://www.online-python.com.

---

## Estrutura do material

```
pre-aula/          Leia NA NOITE ANTERIOR a cada aula (≤ 5 min)
notas/             Notebooks pós-aula — abrir no VS Code após a aula
cheatsheets/       Referência rápida por tópico — consulte durante os exercícios
exercicios/        Prática graduada: básico → médio → avançado
dados/             Arquivos de entrada usados pelos exercícios
```

---

## Fluxo por aula

**Na noite anterior:**
```bash
git pull                             # pegar o teaser da próxima aula
```
Abrir `pre-aula/teaser-aula-NN.md` e fazer o aquecimento de 5 min.

**Após a aula:**
```bash
git pull                             # pegar o notebook e os exercícios
```
Abrir `notas/notas-aula-NN.ipynb` no VS Code e completar os `# TODO`.

**24h depois:**
```bash
git pull                             # pegar o notebook com soluções
```
`notas/notas-aula-NN-solucao.ipynb` estará disponível para conferência.

---

## Rodando os notebooks no VS Code (extensão Jupyter)

Cada vez que você abre um notebook (ou reinicia o VS Code), o **kernel começa vazio** — mesmo
que as saídas de execuções antigas ainda apareçam na tela, nenhuma variável existe até você
rodar as células de novo nesta sessão. Isso é o funcionamento normal do Jupyter, não um bug
do notebook.

- **Reabriu o notebook? Clique em "Run All"** (▷▷, no topo da barra de ferramentas do
  notebook) antes de mexer em qualquer célula. É o hábito mais importante desta lista.
- **Quer rodar só uma célula no meio do notebook** (ex.: pulou direto para a seção 3)? Passe
  o mouse sobre a célula — vai aparecer uma seta ▷ com uma setinha (▾) ao lado — e escolha
  **"Run Above"** (ou clique com o botão direito na célula → **"Execute Above Cells"**). Isso
  roda automaticamente tudo que vem antes, sem precisar procurar manualmente a célula de
  constantes lá no topo.
- **`NameError: name 'X' is not defined`** quase sempre significa isso: uma célula anterior
  (geralmente a de constantes, logo no início) não rodou nesta sessão do kernel. A solução é
  sempre uma das duas acima — não é um erro no conteúdo do notebook.
- **O número entre colchetes à esquerda da célula (`[ ]`)** mostra a ordem de execução.
  Vazio = a célula nunca rodou nesta sessão. Um número bem menor que o das células vizinhas =
  rodou há um tempo, possivelmente antes de alguma mudança — rode de novo para garantir.
- **Travou, deu erro estranho, ou uma variável parece ter o valor errado?** Use **"Restart"**
  (ícone de reload no topo da barra) e em seguida **"Run All"** — isso limpa todo o estado do
  kernel e recomeça do zero.

---

## Dicas de estudo

- **Não leia o notebook passivamente.** Complete os `# TODO` antes de ver a solução —
  é o que consolida o aprendizado.
- **Use o cheat sheet durante os exercícios**, não para estudar — ele é referência,
  não tutorial.
- **Os exercícios avançados** conectam o conteúdo da aula com testes de software —
  são o mais próximo do que você vai fazer no laboratório à tarde.
- Se travar num exercício por mais de 20 min, consulte o notebook de solução e
  tente de novo do zero.