
# 4.2 Кортежи
# import time
#
# passN = int(input())
# freecells = list(range(int(input()),0,-1))
# occupied = []
#
# for _ in range(passN):
#     surname, timeFrom, timeTo = input().split()
#     timeFrom = time.strptime(timeFrom,'%H:%M')
#     timeTo = time.strptime(timeTo,'%H:%M')
#     n = None
#     for cell in occupied:
#         if timeFrom >= cell[1]:
#             n = cell[0]
#             occupied.remove(cell)
#             occupied.append((n,timeTo))
#     if not n and freecells:
#         n = freecells.pop()
#         occupied.append((n, timeTo))
#     print(surname, n)

# lst = [tuple(input().split()) for _ in range(int(input()))]
# lst.sort(key=lambda l: int(l[0]))
# [print(*l,end=' ') for l in lst]



# 4.3 Словари

# d = {}
# for _ in range(int(input())):
#     lst = input().split(' - ')
#     d[lst[0]] = lst[1].split(', ')
# print(d)
# d2 = {}
# for k, values in d.items():
#     for val in values:
#         f = d2.get(val,[])
#         f += [k]
#         d2[val] = f
# print(len(d2))
# for k in sorted(d2.keys()):
#     print(f'{k} - {", ".join(d2[k])}')

# tree = {}
#
# for _ in range(int(input()) - 1):
#     child, parent = input().split()
#     tree.setdefault(parent, [])
#     tree.setdefault(child, []).append(parent)
#
#
# def count_parents(parents):
#     if parents:
#         c = len(parents)
#         for par in parents:
#             c += count_parents(tree[par])
#         return c
#     return 0
# e = {}
#
# for k,v in tree.items():
#     e[k] = count_parents(v)
#
# for i in sorted(e):
#     print(i,e[i])

# goods = {}
#
# for _ in range(int(input())):
#     buyer, item, quant = input().split()
#     d = goods.setdefault(buyer, dict())
#     d.setdefault(item, 0)
#     goods[buyer][item] += int(quant)
#
# for buyer in sorted(goods):
#     print(f'{buyer}:')
#     for item in sorted(goods[buyer]):
#         print(item,goods[buyer][item])

# d = {}
# for _ in range(int(input())):
#     tmp = input().split()
#     d[tmp[0]] = tmp[1:]
# for _ in range(int(input())):
#     city = input()
#     [print(k) for k, v in d.items() if city in v]


# files = {}
# d = {'read':'R','write':'W','execute':'X'}
# for _ in range(int(input())):
#     attr = input().split()
#     filename = attr[0]
#     attr.remove(filename)
#     files[filename] = attr
#
# for _ in range(int(input())):
#     op, file = input().split()
#     print(('Access denied','OK')[d[op] in files[file]])

# line = input().split()
# for i,word in enumerate(line):
#     if word not in line[:i]:
#         print(f'Слово: {word}\tКоличество: {line.count(word)}')

# d = {}
# for _ in range(int(input())):
#     c, n = input().split()
#     d.setdefault(c, 0)
#     d[c] += int(n)
#
# for c in sorted(d):
#     print(c, d[c])

# lst = [input().split() for _ in range(int(input()))]
# word = input()
#
# for t in lst:
#     if word in t:
#         t.remove(word)
#         print(*t)


