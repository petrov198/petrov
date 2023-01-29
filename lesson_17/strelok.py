import time
import random

print("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе!"
      " Когда увидишь 'СТРЕЛЯЙ',"
      " у тебя будет 0.3 секунды чтобы нажать Enter")
input("нажми Enter чтобы начать")
print("время пострелять")

time.sleep(random.randint(1, 5)) # случайное ожидание

start = time.time()
input("стреляй!")
end = time.time()
delta = end - start
print(f"{delta}сек")
if delta < 0.01:
    print("сори")


elif delta > 0.3:
    print("ёу слоули мен")
else:
    print("гуд жоп мен")