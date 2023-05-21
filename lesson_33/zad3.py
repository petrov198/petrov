input()
color = list(input())
per = 0
del_count = 0
while per != len(color) - 1:
    if color[per] == color[per + 1]:
        color.pop(per)
        del_count += 1
    else:
        per += 1
print(del_count)

