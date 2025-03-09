import random

escolha = ["pedra", "papel", "tesoura"]

print("VAMOS JOGAR:")
print("----------------------------------")
print("    _______            _________              _______ ")
print("---'   ____)        ---'    ___)___       ---'   ____)____")
print("      (_____)                 _____)                ______)")
print("      (_____)                 _____)             _________)")
print("      (____)                   ____)             (____)")
print("---.__(___)         ---.__________)       ---.__(___)")
print("    Pedra                Papel               Tesoura")        

pont_computador = 0
pont_jogador = 0

while True:
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    if escolha_jogador not in escolha:
        print("Escolha inválida. Tente novamente.")
        continue

    escolha_computador = random.choice(escolha)
    print(f"Computador escolheu: {escolha_computador}")

    if (escolha_jogador == "pedra" and escolha_computador == "tesoura") or (escolha_jogador == "papel" and escolha_computador == "pedra") or (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        ganhador = "Jogador"
        print("Você ganhou!")
        pont_jogador += 1
        print(f"O placa está: Você {pont_jogador} x {pont_computador} Computador")

    elif escolha_jogador == escolha_computador:
        ganhador = "Empate"
        print("Empatou!")
    else:
        ganhador = "Computador"
        print("Você perdeu!")
        pont_computador += 1
        print(f"O placa está: Você {pont_jogador} x {pont_computador} Computador")

    while True:
        jogar_novamente = input(f"\nGostaria de jogar novamente? (s/n): ")
        if jogar_novamente in ['s','n']:
            break
        else:
            print("Escolha inválida. Tente novamente.")
    if jogar_novamente == 'n':
        print(f"\nPlacar final: Você {pont_jogador} x {pont_computador} Computador")
        print("Obrigado por jogar. Até mais!")
        break
