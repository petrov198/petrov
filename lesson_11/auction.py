import os

total_bets = []
triger = "yes"

while triger == "yes":
    name = input("Имя: ")
    bet = int(input("ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)
    triger = input("yes - продолжаем, no - останавливаем")
    os.system("cls||clear")

winner = {'name': '', "bet": 0}
for i in range(len(total_bets)):
    if total_bets[i]["name"] > winner['name']:
        winner["bet"] = total_bets[i]['bet']

print(f"победитель: {winner['name']}. его ставка: {winner['bet']}.")


