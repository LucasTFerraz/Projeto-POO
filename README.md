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

## Dicas de estudo

- **Não leia o notebook passivamente.** Complete os `# TODO` antes de ver a solução —
  é o que consolida o aprendizado.
- **Use o cheat sheet durante os exercícios**, não para estudar — ele é referência,
  não tutorial.
- **Os exercícios avançados** conectam o conteúdo da aula com testes de software —
  são o mais próximo do que você vai fazer no laboratório à tarde.
- Se travar num exercício por mais de 20 min, consulte o notebook de solução e
  tente de novo do zero.