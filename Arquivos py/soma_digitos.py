n = int(input("Digite um número inteiro: "))

soma = 0

i = 0

while i < n:
    num = n%10
    soma = soma + num
    n = n//10
     
print(f'{soma}')