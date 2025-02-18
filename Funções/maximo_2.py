# 1. Máximo: função "maximo" que receba 2 números como parâmetros e devolva o maior deles

def maximo(x,y):
    maior = max(x,y)
    return maior

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

print(f">>> maximo({num1}, {num2})")
print(maximo(num1, num2))