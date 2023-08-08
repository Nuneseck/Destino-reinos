import random
import json

def roll_event_type(event_types):
    event_roll = random.randint(1, 20)
    for event in event_types:
        if event_roll in event['range']:
            return event

def load_event_types(filename):
    with open(filename, 'r') as file:
        event_types = json.load(file)
    return event_types

def get_daytime(daytime_number):
    daytime_options = {
        1: "Ao amanhecer - O sol alcança o horizonte. É hora de se preparar para o dia e desfazer o acampamento",
        2: "De manhã - O sol nasce e o dia se torna mais aconchegante. A jornada de vocês começa",
        3: "Meio-dia - O sol está em seu pico, a energia se esvai enquanto seu corpo clama por comida",
        4: "De tarde - O sol abaixa e a temperatura esfria. A viagem segue enquanto vocês ainda tem alguma luz natural",
        5: "Anoitecer - O sol afunda no horizonte. É hora de montar acampamento, acender uma fogueira e comer",
        6: "Anoitecer - O sol afunda no horizonte. É hora de montar acampamento, acender uma fogueira e comer",
        7: "De noite - A noite é sombria e cheia de horrores, hostil aos viajantes. Viajar é perigoso e é fácil de se perder",
        8: "De noite - A noite é sombria e cheia de horrores, hostil aos viajantes. Viajar é perigoso e é fácil de se perder",
        9: "Durante um descanso curto ou longo",
        10: "Durante um descanso curto ou longo",
        11: "Durante um descanso curto ou longo",
        12: "Durante um descanso curto ou longo",
        13: "Durante um descanso curto ou longo",
        14: "Durante um descanso curto ou longo",
        15: "Durante um descanso curto ou longo",
        16: "Durante um descanso curto ou longo",
        17: "Durante um descanso curto ou longo",
        18: "Durante um descanso curto ou longo",
        19: "Enquanto se preparam para um descanço longo",
        20: "Enquanto se preparam para um descanço longo"
    }
    return daytime_options.get(daytime_number, "Unknown")

def roll_event():
    while True:
        try:
            days = int(input("How many days do you want? "))
            if days <= 0:
                print("Invalid input for days.")
                continue
            break
        except ValueError:
            print("Invalid input for days.")

    while True:
        daytime = input("Day or night? ").lower()
        if daytime != "day" and daytime != "night":
            print("Invalid input for daytime.")
        else:
            break

    if daytime == "day":
        event_probabilities = {
            "Event occurred": list(range(1, 9)),
            "No event": list(range(9, 21))
        }
    elif daytime == "night":
        event_probabilities = {
            "Event occurred": list(range(1, 17)),
            "No event": list(range(17, 21))
        }

    event_types = load_event_types('event_types.json')

    for day in range(1, days + 1):
        event_occurred = random.randint(1, 20) in event_probabilities["Event occurred"]
        event_result = "Event occurred" if event_occurred else "No event"
        if event_occurred:
            event_type = roll_event_type(event_types)
            daytime_number = random.randint(1, 20)
            event_daytime = get_daytime(daytime_number)
            print(f"Day {day}: {event_result} - {event_type['type']} ({event_daytime})")
            if event_type['type'] == 'Roll two events and use both':
                event_type1 = roll_event_type(event_types)
                event_type2 = roll_event_type(event_types)
                print(f"      Additional event 1: {event_type1['type']}")
                print(f"      Additional event 2: {event_type2['type']}")
        else:
            print(f"Day {day}: {event_result}")

roll_event()
