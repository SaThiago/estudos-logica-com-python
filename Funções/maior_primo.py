# 2. Primos: escrever função "maior_primo" que receba um número inteiro maior ou igual a 2 como parâmetro e devolva o maior número primo menor ou igual ao número passado à função

def éPrimo(k):
    if k==2:
        return True
    i = 2
    while i * i <= k:
        if k%i==0:
            return False
        i = i + 1
    return True


def maior_primo(x):
    while x>1:
        if éPrimo(x):
            return x
        x = x - 1
    return None

        
n = int(input("Digite um número maior ou igual a 2: "))
while n<=1:
    n = int(input("Digite um número maior ou igual a 2: "))

print(f">>> maior_primo ({n})")
print(maior_primo(n))
