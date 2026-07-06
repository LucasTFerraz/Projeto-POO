LADO_GRADE = 10
x = 4
y = 0
print(f'Robô está em ({x},{y})')
# passos = 3
# x = x + passos
# print(f'Robô está em ({x},{y})')
passos = int(input("Quantos passos para o leste? "))
x = x + passos
# print(f'Robô está em ({x},{y})')
passos = int(input("Quantos passos para o norte? "))
y = y + passos
print(f'Robô está em ({x},{y})')
