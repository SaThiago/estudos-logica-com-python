num = int(input("Digite o número "))

resto = 0

algarismos = 0

while num > 0:
    resto = num%10
    num=num//10
    algarismos = algarismos + resto


print("A soma dos algarismos do número digitado é:", algarismos)