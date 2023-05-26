import random

kingdoms = [
    "Bielefeld",
    "Yuden",
    "Deheon",
    "Callistia",
    "União Purpura",
    "Doherimm",
    "Khubar",
    "Wynnla",
    "Fortuna e Petrynia",
    "Pondsmânia",
    "Sckharshantallas",
    "Collen e Ahlen",
    "Tyrondir e Lamnor",
    "Zakharov",
    "Namalkah",
    "Hongari e Portsmouth",
    "Sallistick",
    "Lomatubar e Tollon",
    "Sambúrdia e Ghondriann",
    "Tapista"
]

def roll_dice():
    roll = random.randint(1, 20)
    return roll

# Dictionary to store the results with their corresponding words
results = {}

for kingdom in kingdoms:
    result = roll_dice()

    if result == 1:
        word = "Catástrofre"

    elif result in range(2, 4):
        result = 2
        word = "Turbulência política"

    elif  result == 4:
        word = "Terror mágico"

    elif  result == 5:
        word = "Praga"

    elif  result == 6:
        word = "Intriga"

    elif result in range(7, 9):
        result = 7
        word = "Criaturas míticas"

    elif result in range(9, 12):
        result = 9
        word = "Nada muito fora do habitual"

    elif  result == 12:
        word = "Tesouro Natural"

    elif  result == 13:
        word = "Descoberta"

    elif  result == 14:
        word = "Renascimento religioso"

    elif result in range(15, 17):
        result = 15
        word = "Boom comercial"

    elif result in range(17, 19):
        result = 17
        word = "Heróis"

    elif  result == 19:
        word = "Heróis"

    else:
        word = "Muita fortuna" 

    if result not in results:
        results[result] = {"word": word, "kingdoms": []}
    
    results[result]["kingdoms"].append(kingdom)

# Sort the results dictionary by key in ascending order
sorted_results = dict(sorted(results.items(), key=lambda x: x[0]))

# Open the output file in write mode with UTF-8 encoding
with open("kingdoms_destiny.txt", "w", encoding="utf-8") as file:
    for result, data in sorted_results.items():
        file.write(f"Resultado {result} - {data['word']}:\n")
        file.write("\n".join(data['kingdoms']))
        file.write("\n\n")
