import random
import json

options = {
    "1": ["Morte", "Perde todos os bens", "Perde 1d4 níveis", "Perde 1 nível", "Perde 1 habilidade racial ou talento", "Perde 1d4 de 1d4 atributos"],
    "2": ["Aliado próximo morre se tirar 4 no d4", "É exilado do reino e perde acesso a recursos locais", "Perde a confiança das pessoas e recebe -10 em perícias originalmente relacionadas a Carisma dentro do reino", "Perde todos os tibares", "Perde um item mágico valioso", "É alvo de represálias por parte de outros grupos, recebendo -2 na CA e Resistências contra ataques e ameaças vindas desses grupos"],
    "3": ["C1", "C2", "C3", "C1", "C2", "C3"],
    "4": ["D1", "A2", "A3", "A4", "A5", "A6"],
    "5": ["E1", "A2", "A3", "A4", "A5", "A6"],
    "6": ["F1", "A2", "A3", "A4", "A5", "A6"],
    "7": ["G1", "A2", "A3", "A4", "A5", "A6"],
    "8": ["H1", "A2", "A3", "A4", "A5", "A6"],
    "9": ["I1", "A2", "A3", "A4", "A5", "A6"],
    "10": ["J1", "A2", "A3", "A4", "A5", "A6"],
    "11": ["K1", "A2", "A3", "A4", "A5", "A6"],
    "12": ["L1", "A2", "A3", "A4", "A5", "A6"]
}

# Display the available options
print("Opções:")
print("1 - Catástofre")
print("2 - Turbulência política ")
print("3 - Praga ")
print("4 - Intriga ")
print("5 - Criaturas míticas ")
print("6 - Tesouro natural ")
print("7 - Descoberta ")
print("8 - Renascimento religioso ")
print("9 - Boom comercial ")
print("10 - Heróis ")
print("11 - Avanço no conhecimento ")
print("12 - Muita fortuna ")

# Prompt the user for their choice
choice = input("Escolha a opção: ")

# Check if the chosen option is valid
if choice in options:
    sub_options = options[choice]
    
    # Prompt the user for the number of times to generate sub-options
    num_times = int(input("Para quantos NPCs? "))

    # Generate and display the sub-options
    for i in range(1, num_times + 1):
        random_sub_option = random.choice(sub_options)
        print("Destino NPC {}:".format(i), random_sub_option)
else:
    print("Opção inválida.")
