num = int(input("Digite um número inteiro: "))

ultimo_digito=num%10
num=num//10

while num>0:
    penultimo_digito=num%10
    if penultimo_digito == ultimo_digito:
        print("sim")
    else:
        ultimo_digito = penultimo_digito
        num = num //10

else:
    print("não")

