#x = 7
#
#if x < 10:  # больше либо равно
#    print("я сработал!")
#else:
#    print("ну я тоже сработав")
#
#phrase = "я карта"
#if phrase == "ya karta":  # равно ли?
#    print("мы краты!")
#
#game = "dota2"
#if game = "brawl stars":  # не равно?
#    print("ну можно и п

#number = int(input("введи число:"))
#if number > 0:
#    print("положительное")
#elif number == 0:  # elif = else if (иначе если)
#   print("нулик")
#else:
#    print("отрицательное")

#year = int(input("введи год: "))
#if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#    print("високосненько")
#else:
#    print("не высокосный ._.")

# = int(input("введи первое число:"))
#operation = input("введи опnumber_1ерацию(-,+,*,/):").strip()
#number_2 = int(input("введи второе число:"))
#lst = ["-", "+", "*", "/"]
#
#if operation in lst:
#   if operation == "-":
#       print(number_1 - number_2)
#   elif operation == "+":
#       print(number_1 + number_2)
#   elif operation == "*":
#       print(number_1 * number_2)
#   elif operation == "/":
#       print(number_1 / number_2)


#number_1 = int(input("введи первое число:"))
#number_2 = int(input("введи второе число:"))
#number_3 = int(input("введи третье число:"))
#
#counter_pol = 0
#counter_otr = 0
#
# проверка первого числа
#if number_1 < 0:
#    counter_otr += 1
#else:
#    counter_pol += 1
# проверка второго числа
#if number_1 < 0:
#    counter_otr += 1
#else:
#    counter_pol += 1
# проверка третьего числа
#if number_1 < 0:
#    counter_otr += 1
#else:
#    counter_pol += 1
#
#print("положительных:", counter_pol)
#print("отрицательных:", counter_otr)


#number_1 = int(input("введи первое число:"))
#number_2 = int(input("введи второе число:"))
#number_3 = int(input("введи третье число:"))
#
#lst = [number_1, number_2, number_3]
#
#
# maxi = max(lst)
# mini = min(lst)
# print("минимум:", mini)
# print("максимум:", maxi)






ticket = input("введи номер билета(6 знаков):")
if len(ticket) == 6:
    first_half = ticket[3:]
    last_half =  ticket[-3:]

    first_sum = first_half[0] + first_half[1] + first_half[2]
    last_sum = last_half[0] + last_half[1] + last_half[2]
    if first_sum == last_sum:
        print("счастье")
    else:
        print("несчастье :(")
else:
    print("введи пж нормально!")