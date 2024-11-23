n = int(input("Digite o valor de n: "))

i = 1

fat = 1

while n > 0 and i <= n:
    fat = fat * i
    i = i + 1
    
print(f'{fat}')