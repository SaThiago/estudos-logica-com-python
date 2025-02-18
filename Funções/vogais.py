# 3. Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(c):
    if c=="A" or c=="a" or c=="E" or c=="e" or c=="I" or c=="i" or c=="O" or c=="o" or c=="U" or c=="u":
        return True
    else:
        return False
    
letra = input("Insira uma letra:").strip()

while True:
    if len(letra)==1 and letra.isalpha():
        break
    else:
        letra = input("Insira uma letra:").strip()


print(f">>> vogal('{letra}')")
resultado = vogal(letra)
print(resultado)