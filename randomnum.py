from random import randint
# Parte para o computador escolher um numero aleatório entre 1 a 100
num_aleatorio = randint(1, 100)
vidas = 5
print("O computador escolheu um numero aleatório entre 1 e 100. Tente adivinhar!")
print(f"voce tem {vidas} ❤️  vidas para acertar o numero aleatório.")

# Parte para o jogador escolher um numero entre 1 a 100
Escolha = int(input("Escolha um numero entre 1 e 100: "))

# Loop para verificar se o jogador acertou o numero aleatório
while Escolha != num_aleatorio and vidas > 0:
        vidas -= 1
        
        if Escolha < num_aleatorio:
            print("O numero que você escolheu é menor que o numero aleatório.")
        elif Escolha > num_aleatorio:
            print("O numero que você escolheu é maior que o numero aleatório.")
        print(f"Você tem {vidas} ❤️  vidas restantes.")

        Escolha = int(input("Tente novamente: "))
        if Escolha == num_aleatorio:
            print("Parabéns! Você acertou o numero aleatório, que era:", num_aleatorio)
            break
        else:
            if vidas == 0:
                print("Suas vidas acabaram! O numero aleatório era:", num_aleatorio)