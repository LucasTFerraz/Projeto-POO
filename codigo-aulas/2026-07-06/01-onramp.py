# # int x = 5;
# # -- 1. Tipos dinâmicos
# x = 5
# print(x)
# print(type(x))
x = "agora sou uma string"
# print(x)
# print(type(x))
# x = 5 > 0
# print(x)
# print(type(x))

# # -- 2. Indentação é a sintaxe! 
# # if (x == "agora sou uma string") {
# #     System.out.println("a indenta...");
# #     System.out.println("esta linha faz...");
# # }

# if x == "agora sou string":
#   print("a indentação define o bloco")
#   print("esta linha faz parte do if")

# print("esta linha não faz parte!")


# -- 3. f-strings

nome = "robozinho"
x, y = 6, 7
print("O "+str(nome)+" está na posição ("+str(x)+", "+str(y)+")")
print(f'O {nome} está na posição ({x}, {y})')