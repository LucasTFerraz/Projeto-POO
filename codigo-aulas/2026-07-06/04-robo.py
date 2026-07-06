LADO_GRADE = 10
x = 0
y = 0
print(f'Robô está em ({x},{y})')
passos = int(input("Quantos passos para o leste? "))
novo_x = x + passos
passos = int(input("Quantos passos para o norte? "))
novo_y = y + passos

x_valido = 0 <= novo_x < LADO_GRADE
y_valido = 0 <= novo_y < LADO_GRADE

if x_valido and y_valido:
    x = novo_x
    y = novo_y
    print(f'Robô está em ({x},{y})')
elif x_valido and not(y_valido):
    print("Problema na quantidade de passos para o norte")
elif not(x_valido) and y_valido:
    print("Problema na quantidade de passos para o leste")
else:
    print("Problema na quantidade de passos para o norte E para o leste")

borda_x = x==0 or x==LADO_GRADE-1
borda_y = y==0 or y==LADO_GRADE-1
if borda_x and borda_y:
    print("Está no canto")
elif borda_x or borda_y:
    print("Está em uma borda")
else:
    print("Está no interior")