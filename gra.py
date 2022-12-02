import random

class geeks:
    def __init__(self, name, number):
        self.name = name
        self.number = number  

def draw_number(amount, total_amount):
    list_of_numbers = []
    for x in range(amount):
        number = random.randint(0, total_amount)
        if number is not list_of_numbers:
            list_of_numbers.append(number)
        elif number in list_of_numbers:
            continue
    return(list_of_numbers)

players = []


print("""Gra polega na tym że ty i 3 innych graczy(komputer) mogą wylosować 6 cyfer 
z pośród49, wygrwa gracz z największą sumą liczb, w nagrode dostaje wylosowane 6 cyfer, którymi 
może zagrać w lottoi potencjalnie wygrać""")

name = str(input("wpisz swoje imię: "))


players.append(geeks(str(name), draw_number(6, 100)))
players.append(geeks("Gracz1", draw_number(6, 100)))
players.append(geeks("Gracz2", draw_number(6, 100)))
players.append(geeks("Gracz3", draw_number(6, 100)))


print("Oto lista graczy i ich losowe liczby:")
for element in players:
    print(element.name, element.number, sep= " ")

for element in players:
    print(f"Suma wylosowanych liczb od każdego gracza to : {sum(element.number)}")
    wynik = sum(element.number)
   ## print(f"najwyższy wynikt to {players[max(sum(wynik))]}")



#zrobiłęś wsyzstko prawie, tylko musisz wylosować ktory gracz zdobył max punktów i jesli nasz gracz główny
#to dać mu losowe liczbyy, kombinuj z max() i moze w ostatniej pętli jakos bys to zrobił? hmm