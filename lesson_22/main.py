import json
# f = open("file.json", "w", encoding="utf-8")
# #f = open("file.txt", "w")
# #f.write("true")
# peremennay = [1, 4.3, [0, 0], (0, 0), None, True, "ENG", "РУС"]
# json.dump(peremennay, f, ensure_ascii=False)
# f.close()
#
# # JSON. чтение.
#
# f = open("file.json", "r")
# #print(f.read())
# content = json.load(f)
# print(content)
# print(type(content))
# f.close()
# задача 1
# f = open("file.txt", "r", encoding="utf-8")
# u = f.readlines()
# spic = {}
# print(u)
# for i in u:
#    p = i.split(": ")
#    print(p)
#    spic[p[0]] = p[1].rstrip()
# print(spic)
#
# o = open("file.json", "w", encoding="utf-8")
# json.dump(spic, o, ensure_ascii=False)
# o.close()
# задача 2
# f = open("file.json", "r")
# sod = json.load(f)
# f.close()
# print(sod)
# for indx, elem in enumerate(sod):
#     if type(elem) == str:
#         sod[indx] += "!"
#     elif type(elem) in (int, float):
#         sod[indx] += 1
#     elif type(elem) == bool:
#         sod[indx] = not elem
#     elif type(elem) == list:
#         sod[indx] += elem
#     elif type(elem) == dict:
#         sod[indx][["newkey"] = None
# print(sod)

import requests

resp = requests.get(url="http://api.open-notify.org/iss-now.json").json()
print(resp['iss_position'])