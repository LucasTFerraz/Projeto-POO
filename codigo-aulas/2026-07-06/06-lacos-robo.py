n = int(input("Quantos comandos para o robô? "))
for i in range(n):
    comando = input(f'Digite o comando #{i+1}: ')
    print(f'Executando {comando}')
print('Chegamos ao fim.')