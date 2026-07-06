COMANDO_SAIDA = "SAIR"
while True:
    comando = input(f'Digite o comando: ')
    partes = comando.strip().upper().split()
    acao = partes[0]
    if acao == "AVANCAR":
        num_passos = partes[1]
    elif acao == "GIRAR":
        lado = partes[1]
    elif acao == COMANDO_SAIDA:
        print('Encerrando...')
        break
    else:
        print(f'Comando desconhecido: {acao}')
print("Programa encerrado.")