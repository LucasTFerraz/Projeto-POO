# Pré-aula 16 — Capstone: configurar, montar e testar o robô

## O robô até aqui

O modelo de features do robô já valida tipo e estratégia antes de instanciar
qualquer coisa — `criar_robo_configurado` recusa combinações inválidas com uma
exceção customizada, `ConfiguracaoInvalida`.

## O problema que vamos resolver

Até agora, toda configuração chega como argumentos nomeados, digitados um por um.
Configuração de verdade — de arquivo, de banco, de variável de ambiente — chega
como **dado**. E como é que alguém confirma, com confiança, que o robô montado a
partir desse dado continua se comportando certo depois que o código mudar daqui a
um mês? Rodando `python arquivo.py` e olhando a tela, à mão, toda vez?

## Aquecimento (5 min — faça antes de entrar na sala)

Sem consultar código, escreva de memória a assinatura de `validar_configuracao`
(Aula 15) e o que cada uma das quatro checagens dentro dela faz, na ordem. Compare
com `notas/notas-aula-15-solucao.ipynb`.

## Leitura opcional

- pytest — "Get Started" (documentação oficial): https://docs.pytest.org/en/stable/getting-started.html
- Fixtures (documentação oficial): https://docs.pytest.org/en/stable/how-to/fixtures.html
