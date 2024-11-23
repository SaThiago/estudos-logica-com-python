# Definir o número secreto
numero_secreto = 7
adivinhado = False

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10.")

# Loop enquanto o número não for adivinhado
while not adivinhado:
    # Solicitar um palpite ao usuário
    palpite = int(input("Digite seu palpite: "))

    # Verificar o palpite
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        adivinhado = True  # Sair do loop
    else:
        print("Errado! Tente novamente.")

print("Obrigado por jogar!")