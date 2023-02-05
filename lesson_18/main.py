import easygui

# while True:
#     print(easygui.msgbox(
#     msg="Hello world!",
#     title="усиленно приветствую",
#     ok_button="понято",
#     image="img/star.png"
# ))
#
# easygui.buttonbox(
#     msg="какой ты сегодня?",
#     title="выбор",
#     choices=("Загадочный",),
#     images=["img/math.png", "img/star.png"]
# )

#  x = easygui.integerbox(
#      msg="сколько 1 + 1 = ",
#      upperbound=2,
#      lowerbound=2,
#      image="img/math.png"
#
#  )
# print(x)

name = easygui.enterbox(
    msg="какое погоняло собаки(друга)?",
    default="Никита"
)
print(name)