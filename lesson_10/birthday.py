import random
import datetime

while True:
    number = input("сколько дней рождения мы генерим? (До  70)")
    if not number.isdigit() or int(number) < 2:
        print("это по твоему смешно? Число от 2 до 70.")
        print("=" * 10)
    else:
        number = int(number)
        break

birthdays = []
startOfyear = datetime.date(2022, 1, 1)   # год, месяц, день

for _ in range(number):
    shiftOfDays = datetime.timedelta(random.randint(0, 364))
    birthday = startOfyear + shiftOfDays
    birthdays.append(birthday)

for index in range(number):
    print(f"{index + 1}) {birthdays}")

print("=" * 10)
for i in set(birthdays):
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)}")

