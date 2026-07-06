COMANDO_SAIDA = "SAIR"
while True:
    comando = input(f'Digite o comando: ')
    if comando == COMANDO_SAIDA:
        break
    print(f'Executando {comando}')
print("Programa encerrado.")