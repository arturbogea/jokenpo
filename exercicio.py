import random

print("Bem-vindo ao jogo Pedra ✊, Papel ✋ e Tesoura ✌️!")

opcoes_escolha = ["🪨 Pedra", "📄 Papel", "✂️ Tesoura"]
minha_escolha = int(input("Escolha uma das seguintes opções: 0 - pedra, 1 - papel, 2 - tesoura  "))
escolha_pc = random.randint(0, 2)

print(f"Você escolheu: {opcoes_escolha[minha_escolha]}")
print(f"O computador escolheu: {opcoes_escolha[escolha_pc]}")

if minha_escolha == 0:
    if escolha_pc == 1:
        print("O computador venceu! 🤖")
    elif escolha_pc == 2:
        print("Você venceu! 😄")
    else:
        print("Empate! 🤝")

elif minha_escolha == 1:
    if escolha_pc == 0:
        print("Você venceu! 😄")
    elif escolha_pc == 2:
        print("O computador venceu! 🤖")
    else:
        print("Empate! 🤝")

elif minha_escolha == 2:
    if escolha_pc == 0:
        print("O computador venceu! 🤖")
    elif escolha_pc == 1:
        print("Você venceu! 😄")
    else:
        print("Empate! 🤝")

else:
    print("Escolha uma opção válida.")