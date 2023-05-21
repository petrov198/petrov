a = input().split()
pribl1 = int(a[0])
pribl2 = int(a[1])
count = 0
while pribl2 >= pribl1:
    pribl2 *= 2
    pribl1 *= 3
    count += 1
print(count)