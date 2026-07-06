# while True:
#     num = input("Quantos passos? (deve ser um número inteiro positivo) ")
#     if num.isdigit() and int(num) > 0: #checar API isnumeric
#         print(num)
#         break
#     print("Entrada inválida, tente de novo.")
# print(f'Você escolheu {num} passos')

numero = input("Digite um número inteiro positivo: ")
while not(numero.isdigit() and int(numero)>0):
    print("Precisa ser um número positivo!")
    numero = input("Digite um número inteiro positivo: ")
print(f'Você escolheu {numero} passos')