logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
is_game = "y"
while is_game == "y":

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    hand_player = [random.choice(cards)]
    hand_computer = [random.choice(cards)]
    score_player = 0
    score_computer = 0
    get_card = "y"
    while get_card == "y":
        hand_player.append(random.choice(cards))

        # если туз и > 21
        if sum(hand_player) > 21 and 11 in hand_player:
            for i in range(0, len(hand_player)):
                 if hand_player[i] == 11:
                     hand_player[i] = 1

        score_player = sum(hand_player)
        print(f"твоя рука: {hand_player}. очков: {score_player}")
        print("первая карта компутера:", hand_computer[0])
        if score_player > 21:
            get_card = "n"
        else:
            get_card = input("y - взять карту, n - остановиться")

        while sum(hand_computer) < 17:
            hand_computer.append(random.choice(cards))

            # если туз и > 21
            if sum(hand_computer) > 21 and 11 in hand_computer:
                for i in range(0, len(hand_computer)):
                    if hand_computer[i] == 11:
                        hand_computer[i] = 1
        score_computer = sum(hand_computer)
        print("=" * 10)
        print(f"твоя итоговая рука: {hand_player}. очков: {score_player}")
        print(f"компутера итоговая рука: {hand_computer}. очков: {score_computer}")

        if score_computer > 21 and score_player > 21:
            print("перелёт у обоих. ничья.")
        elif score_player > 21:
            print("твой перебор. проиграл.")
        elif score_computer > 21:
            print("пербор компутера. выйграл.")
        elif score_player > score_computer:
            print("победа.")
        elif score_player < score_computer:
            print("проиграл.")
        else:
            print("ничья.")

        is_game = input("ещё разочек? y - да, n - нет: ")



