import easygui
import random

def rock_paper_scissors():
    b="img/б.png"
    k="img/к.png"
    n="img/н.png"
    user=easygui.buttonbox(
        images=[b, k, n],
        choices=("выйти",),
    )
    comp=random.choice([b,k,n])




    if user == b and comp == b:easygui.msgbox(msg="ничья")
    elif user == b and comp == k:easygui.msgbox(msg="ты выйграл")
    elif user == b and comp == n:easygui.msgbox(msg="компьютер выйграл")
    elif user == k and comp == n:easygui.msgbox(msg="you win")
    elif user == k and comp == k:easygui.msgbox(msg="ничья")
    elif user == k and comp == b:easygui.msgbox(msg="компьютер выйграл")
    elif user == n and comp == n:easygui.msgbox(msg="ничья")
    elif user == n and comp == b:easygui.msgbox(msg="ты выйграл")

    print(user,comp)





def guess_the_number():
    chislo = random.randint(1, 100)
    gn = easygui.integerbox(upperbound=100,lowerbound=1,msg="отгадай число от 1 до 100")
    while gn != chislo:
        if gn > chislo:
            gn = easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нет, нужно число меньше чем{gn}", image="img/м.png")
        elif gn < chislo:
            gn = easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нет, нкжно число больше чем{gn}", image="img/щ.png")
        if gn == chislo:
            gn = easygui.msgbox(msg=f"win",image="img/star.png")


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()