# from string import ascii_lowercase
# alphabet = ascii_lowercase
# vihod = 0
# x = input().lower()
# a = input().lower()
#
# for i in range(len(x)):
#     if x[i] != a[i]:
#         b = alphabet.index(x[i])
#         z = alphabet.index(a[i])
#         if b < z:
#            vihod = -1
#         else:
#            vihod = 1
#         break
# print(vihod)
x = input().lower()
a = input().lower()
if x < a:
    print(-1)
elif x > a:
    print(1)
else:
    print(0)    
