#2. Reescreva a função 'maximo' do outro exercício, 
# que devolve o maior valor dentre dois inteiros recebidos, 
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

def maximo(x,y,z):
    maior = max(x,y,z)
    return maior

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

print(f">>> maximo({num1}, {num2}, {num3})")
print(maximo(num1, num2, num3))