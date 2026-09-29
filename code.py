import random

numero = random.randint(1, 100)
tentativas = 0

print("Adivinha o número entre 1 e 100!")

while True:
    try:
        palpite = int(input("O teu palpite: "))
    except ValueError:
        print("Escreve um número válido.")
        continue

    tentativas += 1

    if palpite < numero:
        print("Mais alto ⬆️")
    elif palpite > numero:
        print("Mais baixo ⬇️")
    else:
        print(f"Acertaste em {tentativas} tentativas! 🎉")
        break