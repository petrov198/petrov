a = input().split()
summa = 0
count = 0
cost_banan = int(a[0])
deneg = int(a[1])
kolvo_banan = int(a[2])
for i in range(1,kolvo_banan +1):
    summa += cost_banan * i
if summa - deneg > 0:
    print(summa - deneg)
else:
    print(0)