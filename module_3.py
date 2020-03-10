# 3.3 Строковые методы



# print(input().split('"\''))

# print(input().replace('(','|'))

# c1,c2 = [input() for _ in range(2)]
# print(''.join(map(lambda c: c==c2 and c+c1 or c, input())))

# l = 'abqwdfaasasdasda'
# print(l[:len(l)//2 - (not len(l)%2)],l[-len(l)//2+1:],sep='')

# str = 'a : b : c : d'.split(':')
# print(str[0],str[-1],sep='')

# str = 'Привет'
# print(*[(not i%2) and c.upper() or c for i,c in enumerate(str)],sep='')

# prev = '.'
# res = []
# for c in str.split():
#     res += [('.' in prev) and c.capitalize() or c.lower()]
#     prev = c
# print(*res)

# lst = ['фывфв', 'Бфвфыфыв', 'фывфы', 'Дфыв', 'ФЫФывфывыфв', 'фывфывфыаыв', 'Аывфывфв', 'авыавыавыа', 'Асмчсмсчм', 'Асмчсмчсмчс', 'Ачмчмвыауц', 'уцкцукуц', 'Ыфвафывывф']
# ans = ['исправить', 'верно', 'исправить', 'верно', 'верно', 'исправить', 'верно', 'исправить', 'верно', 'верно', 'верно', 'исправить', 'верно']
# print(*map(lambda word: word[0].isupper() and 'верно' or 'исправить', lst ),sep='\n') # iter(input,'стоп')
# print()
# print(*ans,sep='\n')

lst = 'Привет,Пока,Прощай,Знай,Думать'.split(',')
s = lst[1]
lst[1] = s[:-2]+s[-1:]
print(','.join(lst))


