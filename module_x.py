# n = int(input())
# lst = list(iter(input, '\\'))
# print(len(set(lst[:n])-set(lst[n:])))

# rep = []
# words = []
# while True:
#     s = input()
#     if s in rep:
#         break
#     if s not in words:
#         words.append(s)
#     else:
#         rep.append(s)
#
# print(*words)


# print(len(set(input().lower())))

# lst = [input() for _ in range(int(input()))]
# lst = ['ап', 'ап', 'ап', 'ап', 'ап', 'ап', 'рп', 'ап']
# print(len(set(filter(lambda a: lst.count(a)>1, lst))))
# res = []
# for a in lst:
#     if a not in res and lst.count(a)>1:
#         res.append(a)
# print(len(res))

# m = {input():int(input()) for _ in range(int(input()))}
# print(*sorted(m,key=m.get))

# lst = [input() for _ in range(int(input()))]
# print(*map(len,lst),max(lst, key=len),sep='\n')


# a,b,c,d = map(int,[input() for _ in range(4)])
# print(*filter(lambda a: a % d == c, range(a,b+1)))

# for i in range(1,int(input())+1):
#     print('* '*i)

# print(*['* '*n]*n, sep='\n')

# inp = 'Привет'
# vowels = 'аоэеиыуёюя'
# print(len(list(filter(lambda a: a in vowels, list(inp)))))

# print(*inp.split()[1:])
# print(len(list(filter(lambda a: len(a) == 1, inp.split()))))
# print(len(list(filter(methodcaller('isdigit'),list(inp)))))

# print('-2'.isdigit())
# n,a,b = map(int, [input() for _ in range(3)])
# lst = map(int, [input() for _ in range(n)])
# print(sum(islice(lst,a-1,b)))
# print(*islice(lst,a-1,b))



# a = int(input())
# b = int(input())
# st = (1,-1)[a>b]
#
# print(*range(a,b+st,st))


# print(*list(input())[::-1],sep='\n')

# n = input().lower().count('я')
# if n>0:
#     print(n)
# else:
#     print('"Я" тут нет!')

# a, b = 8, 3
# step = 1
# if a>b:
#     b -=1
#     step = -1
# else:
#     b +=1
#
# print(*list(range(a,b,step)))

# print(*input().split()[:-1])

# for i in range(n):
#     d = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
#     print(d[i%7])

# p1 = [int(input()) for _ in range(int(input()))]
# p2 = map(lambda x: re.sub(r'\.0$','',f'{x*0.9:.1f}'), p1)
#
# print('Цена товаров:',*p1,sep='\n')
# print('\nЦена товаров со скидкой:',*p2,sep='\n')


# print(''.join([w[0].capitalize() for w in input.split()]))
# [print(*row) for row in zip(*map(lambda a:(int(a),int(a)+1),input.split()))]
# print(reversed([int(input()) for _ in range(int(input()))]))
# [print(i,i.startswith('123')) for i in input().split()]
# print(input().replace('+',' * '))
# print(*list(str(int(''.join(input().split(' - '))) + 103)),sep=' - ')

# n = len(w)
# cap = len(re.sub(r'[^А-Я]','',w))
# low = len(re.sub(r'[^а-я]','',w))
# sp = w.count(' ')
#
# print(f'Количество символов в тексте: {n}')
# print(f'Количество заглавных букв: {cap}')
# print(f'Количество прописных букв: {low}')
# print(f'Количество пробелов: {sp}')
# toremove = ['у','р','д','в','ц','т']
# print(re.sub(r'[урдвцт]','',w))

# print(input().capitalize())

# a = l.index(min(l))
# b = l.index(max(l))
# l[a], l[b] = l[b], l[a]
# print(*l)

# .append()
# lst = list(map(int, input().split()))
# lst.append(int(input()))
# print(sorted(lst))

# lst = [1, 2, 3, 4, 5, 6]
# lst = [123, 34, 324, 123, 567, 213]
# print(lst[1:-1])
# l = lst.copy()
# l.remove(min(l))
# l.remove(max(l))
#
# if 2 in l or 123 in l:
#     print(set(l))
# else:
#     raise ValueError(lst)

# h = list(map(int, iter(input, '0')))
# print(h.index(max(h))+1)

# print(("НЕТ", "НОЛЬ ТУТ ЕСТЬ")['0' in iter(input, 'стоп')])

# n, k = [int(input()) for _ in range(2)]
# [print(f'{i}. {" ".join(map(str,range(1,k+1)))} ') for i in range(1,n+1)]

# n, k = [int(input()) for _ in range(2)]
# print(*filter(lambda x:not x%n, range(1,k+1)))

# a = int(input())
# b = int(input())
# step = 1
# if a > b:
#     b -=1
#     step =-1
# else:
#     b +=1
# print(*range(a,b,step),sep=', ')


# n = mean(map(int, iter(input, 'стоп')))
#
# if 4.5<=n<=5.0:
#     print("Молодец, ты отличник, так держать")
# elif 3.5<=n<=4.49:
#     print("Молодец, ты хорошист, но можно и лучше")
# elif 2.5<=n<=3.49:
#     print("Есть к чему стремиться. Ты троечник")
# elif n < 2.5:
#     print("Это очень плохо. Ты двоечник")

# c1 = c2 = 1
# a = int(input())
# while c1 < 5:
#     b = int(input())
#     c1 = c1 + 1 if b - a == 1 else 1
#     a = b
#     c2 += 1
#
# print('Молодец, ты научилась считать до 5')
# print(c2)

# n = int(input())
# d = list(map(str, filter(lambda x:not n%x,range(2,n))))
# if d:
#     print(f'{n} - непростое, есть еще делители: {" ".join(d)}')
# else:
#     print(f'{n} - простое')

# print(('НЕТ',f'{n} - простое')[all(map(lambda x:bool(n%x),range(2,n)))])
# print(*range(1,int(input())+1,2),sep='\n')

# print(*range(1,101),sep=', ')
# print([input().replace("'",'"') for _ in range(3)].count('"'))

# print(' '.join(map(lambda x:x.replace('пол', 'два ') if x.startswith('пол') else x,w.split())))

# op = {"+":add, "-":sub, "*":mul, "/":truediv}
# a, o, b = int(input()), input(), int(input())
# try:
#     print(op[o](a,b))
# except ZeroDivisionError:
#     print('Ошибка')

# d = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
#
# print(d[int(input())%7])

# w = 'Привет как дела?'
# a = 5
#
# [print(w[i-1]+['\n',''][bool(i%a)],end='') for i in range(1,len(w)+1)]

# w = 'А собака боса'.lower().replace(' ','')
#
# print(("Нет","Да")[w == w[::-1]])

# s = str(len(re.sub(r'[^а-яa-z]+','',w.lower())))
#
#
# if int(s[-1]) in [0]+list(range(5, 10)) or len(s)>1 and int(s[-2]) == 1:
#     print(s,"букв")
# elif int(s[-1]) in range(2,5):
#     print(s,"буквы")
# else:
#     print(s,"буква")

# [print(' '*i+w[i]) for i in range(len(w))]
# [print(' '*i+w[i:[None,-1*i][i>0]]) for i in range(bool(len(w)%2)+len(w)//2)]
# print(*map(lambda a: (len(w)-len(a))*' '+a, accumulate(w[::-1],lambda a,b:b+a)),sep='\n')

# i = [input() for _ in range(3)]
# i = [1,2,3,4,5,6,-1,0]
# print(len(list(filter(lambda x:x>0,map(int,[input() for _ in range(3)])))))
# print(len(list(filter(lambda x:x>0,i))))


# print(('НЕТ', 'Интересное')[i[0]+i[-1] == i[-1]+i[-2]])

# print(('Зима', 'Весна', 'Лето', 'Осень')[((int(input())+1)//3)%4])
#     12 1 2   3 4 5    6 7 8   9 10 11


# a, b = [int(input())for _ in range(2)]
# print(('Ты не прав!','Молодец, ты прав!')[int(input(f'Сколько будет {a}+{b}?'))==a+b])


# s = 'оанвморианыынао'
# try:
#     s[s.index('м'):len(s)-s[::-1].index('р')].index('и')
#     print('Найдено')
# except ValueError:
#     print('Нет')


# print(('Найдено','Нет')[input().find('мир')<0])

# print(('Стоп','Беги')['теш' == ''.join([input()[-1] for _ in range(3)])])

# c = ''.join([input()[-1] for _ in range(3)])
# if 'теш' == ''.join(a[-1] for a in c):
#     print('Беги')
# else:
#     raise ValueError(c)


# email = 'ivano v@bk.ru'
# print((f'{email} - некорректный','OK')['@' in email and '.' in email and ' ' not in email])

# print(''.join(sorted(input())).lstrip('0'))
# print(''.join(sorted(input())))


# a,b = [int(input())for _ in range(2)]
# print(['q','e','r'][a<=b +a==b)
# print(('Первое','Второе','Числа одинаковые')[(a==b)<<1|(a<b)])
# print(min([int(input()) for _ in range(2)]))
