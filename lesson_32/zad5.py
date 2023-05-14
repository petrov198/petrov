x = int(input())
count = 0
for i in range(x):
        z = input()
        if z.count("++"):
            count += 1
        elif z.count("--"):
            count -= 1
print(count)            