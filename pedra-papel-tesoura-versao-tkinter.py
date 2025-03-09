import tkinter as tk
import random

# Função para atualizar o resultado do jogo
def jogar(escolha_jogador):
    escolha_computador = random.choice(escolha)
    label_computador.config(text=f"Computador escolheu: {escolha_computador}")
    
    if (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
       (escolha_jogador == "papel" and escolha_computador == "pedra") or \
       (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        ganhador = "Jogador"
        resultado.config(text="Você ganhou!", fg="green")
        global pont_jogador
        pont_jogador += 1
        
    elif escolha_jogador == escolha_computador:
        ganhador = "Empate"
        resultado.config(text="Empatou!", fg="orange")
    else:
        ganhador = "Computador"
        resultado.config(text="Você perdeu!", fg="red")
        global pont_computador
        pont_computador += 1

    placar.config(text=f"Placar: Você {pont_jogador} x {pont_computador} Computador")

# Função para resetar o jogo
def resetar():
    global pont_computador, pont_jogador
    pont_computador = 0
    pont_jogador = 0
    placar.config(text="Placar: Você 0 x 0 Computador")
    resultado.config(text="Escolha uma opção para começar!", fg="black")
    label_computador.config(text="Computador escolheu:")

# Iniciar o Tkinter
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")

# Configurações iniciais
escolha = ["pedra", "papel", "tesoura"]
pont_computador = 0
pont_jogador = 0

# Título
titulo = tk.Label(root, text="VAMOS JOGAR PEDRA, PAPEL E TESOURA", font=("Arial", 16))
titulo.pack(pady=10)

# Placar
placar = tk.Label(root, text="Placar: Você 0 x 0 Computador", font=("Arial", 14))
placar.pack(pady=10)

# Resultado
resultado = tk.Label(root, text="Escolha uma opção para começar!", font=("Arial", 14))
resultado.pack(pady=10)

# Opções do jogo
botao_pedra = tk.Button(root, text="Pedra", width=20, height=2, command=lambda: jogar("pedra"))
botao_papel = tk.Button(root, text="Papel", width=20, height=2, command=lambda: jogar("papel"))
botao_tesoura = tk.Button(root, text="Tesoura", width=20, height=2, command=lambda: jogar("tesoura"))

botao_pedra.pack(pady=5)
botao_papel.pack(pady=5)
botao_tesoura.pack(pady=5)

# Computador escolhe
label_computador = tk.Label(root, text="Computador escolheu:", font=("Arial", 14))
label_computador.pack(pady=10)

# Botão para resetar o jogo
botao_resetar = tk.Button(root, text="Reiniciar Jogo", width=20, height=2, command=resetar)
botao_resetar.pack(pady=20)

# Iniciar a interface
root.mainloop()