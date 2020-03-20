
# 4.4 Вложенные списки

n, a, b, c, d, o = '7 % ? * ( 0'.split()
n = int(n)
m = [[o]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i < j < n-i-1:
            m[j][i] = a
            m[i][j] = b
        if i > j > n-i-1:
            m[j][i] = c
            m[i][j] = d

for line in m:
    print(*line)


# m, n, k = map(int, input().split())
# a = 0
# lst = []
#
# for i in range(n):
#     line = []
#     for j in range(m):
#         a += 1
#         line += [a]
#     line += ['|']+[i+k for i in line]
#     lst += [line]
#
# for line in lst:
#     print(''.join(["{:<5}".format(i) for i in line]).rstrip())

# "{:>3}".format(i)

# from itertools import repeat
#
# a = zip(repeat(0),[1,2,3],repeat(0))
# print(*a)

# m = [input().split()]
# m += [input().split() for _ in range(len(m[0])-1)]
#
# for i in range(len(m)-1,-1,-1):
#     print(*reversed(m[i]))


# from functools import partial
#
# n, x = map(int, input().split())
# lst = map(partial(map,lambda v:int(v)+x), [input().split() for _ in range(n)])
# for line in lst:
#     print(list(line))


# n, g, d, w = input().split()
# res = []
# for i in range(int(n)):
#     line = []
#     for j in range(int(n)):
#         if j < i:
#             line.append(g)
#         elif j > i:
#             line.append(w)
#         else:
#             line.append(d)
#     res += [line]
#
# print(*res,sep='\n')

# _, n = map(int, input().split())
# print(*[list(map(int,input().split())) for _ in range(n)],sep='\n')

# n,m,s = input().split()
# print(*[[s]*int(m)]*int(n), sep='\n')


# 4.2 Кортежи
# import time


# lst = [tuple(map(int,input().split())) for _ in range(int(input()))]
# filt = list(filter(lambda l: l[0] % 2 ^ l[1] % 2, lst))
# n = len(lst) - len(filt)
# repl = max(filt, key=sum)
# print(n)
# for p in map(lambda l: bool(l[0] % 2) == bool(l[1] % 2) and repl or l,lst):
#     print(*p)


# def tribonach(n):
#     prev = (1,1,1)
#     while n:
#         yield prev[0]
#         prev = (*prev[1:],sum(prev))
#         n -= 1
#
#
# print(*tribonach(5))

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
# for _ in range(len(lst)):
#     m = min(lst,key=lambda l: int(l[0]))
#     print(*m, end=' ')
#     lst.remove(m)

    # lst.remove(t)


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


