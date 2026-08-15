# print('Hello from Python')
#
# print(1,2,'text',sep='-',end='\n\n')

i = 3
# f = 1.3
# b = True # False
# s = 'text' # ""
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
# a=b=c=10
#
# print(a, b, c)
#
# fi = int(f)
#
# print(fi)
#
# # print(int('15ddd'))
#
# # a = 0
# #
# # # a++
# # # ++aa
# # a+=1
#
# a = 7
# b = 2
# # #
# print(a+b)
# print(a-b)
# print(a/b)
#
# print(a // b)

# res = isinstance('text', str)
# print(res)


# if a<b:
#     print('yes')
# elif a>b:
#     print('no')
# else:
#     print('else')

# f = True
#
# if not f and a>b or a==b:

# num = int(input('Enter a number:'))
#
# res = 'yes' if num>5 else 'no'
#
# print(res)

# l = [1, 2, 3, 4, 5, 6, 7]
# # print(l[0])
# # # print(l[55])
# # print(l[-2])
# # l[3]=5
# # print(l)
# #
# # l2 = l
# #
# # l2[0]=7777
# #
# #
# # print(l)
# # print(l2)
#
# l2 = l.copy()


# l1 = [7,3,4]
# l2 = [1, 2, 3, 2,4, 5, 6]
# #
# # l2.append(77)
# # l2.insert(55, 55)
# # print(l2)
#
# pop = l2.pop(4)
# print(pop)
# print(l2)
# l2.remove(2)
# print(l2)
# l1.extend(l2)
# print(l1)

# l3 = l1 + l2
# l1+=l2
# print(l1)

# l = [1, 2, 3, 2,4, 5, 6]

# # print(l.index(2, 6, 66))
#
# l.reverse()
# l.sort()
# l.sort(reverse=True)
# print(l)
# print(l.count(2))
# l.clear()
#
# print(l)

# print(l[::-2])
#
# my_tuple  = (1,2,3)
# print(my_tuple)
# print(my_tuple[1])
# print(my_tuple[11])
# my_tuple[1]=6
#
# l = list(my_tuple)
#
# l[2]=55
#
# # print(l)
#
# l = [1,2,4]
# dictionary = {
#     'name':'max',
#     True:1,
#     False:6,
# }
# # # print(dictionary['name'])
# # # print(dictionary['name1'])
# # print(dictionary.get('name1', 'Karina'))
# # dictionary.clear()
# # dictionary.copy()
#
# keys = ['name', 'age', 'house']
#
# # d= dict.fromkeys(keys,1)
# #
# # print(d)
#
# # print(dictionary.items())
# # print(dictionary.keys())
# # print(list(dictionary.values()))
#
# name = dictionary.pop('name')
# print(name)
# value = dictionary.popitem()
# print(dictionary)

# dictionary = {
#     'name':'max'
# }
# dictionary2 = {
#     'house':99
# }
# dictionary['house'] = 100
# dictionary.setdefault('name', 55)
# print(dictionary)
#
# dictionary.update(dictionary2)
# dictionary|=dictionary2
# print(dictionary)

# l = [1,2,1,4,2,5,1]
#
# s = list(set(l))
# # print(s)
# #
# s={}
#
#
#
# s = set()
# # print(type(s))
# s.add(5)
# s.add(3)
# s.add(2)
# s.add(25)
# s.add(5)
# s.add(3)
# # print(s)
# # print(s[0])
#
# s1={6,7,8,4,1}
# s2={1,2,3,4}
# # print(s)
# pop = s.pop()
# # print(pop)
# # print(s)
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# print(s1.isdisjoint(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# s1.update(s2)
# # s1.remove(77)
# s1.discard(7)
# print(s1)

# print(s)
# l =[1,2,5,7,8,9,5]
# print(len(l))

# print('*'*25)
# name = 'Max'
# age = 18
# weight = 70.5
#
string = 'hlello, my name is Max, I`m 18 and my weight 70.5kg'
# string = 'Hello, my name is '+name+', I`m '+str(age)+' and my weight '+str(weight)+'kg'
# string = 'Hello, my name is %s, I`m %d and my weight %fkg' %(name, age, weight)
# string = 'Hello, my name is {}, I`m {} and my weight {}kg'.format(name, age, weight)
# string = 'Hello, my name is {name}, I`m {age} and my weight {weight}kg'.format(age=age, weight=weight, name=name)
# string = f'Hello, my name is {name}, I`m {age} and my weight {weight}kg'
# print(string)

# print(string.index('ll'))
# print(string.find('lll'))
# print(string.count('l'))
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(string.startswith('h'))
# print(string.endswith('h'))
# print(['   sssss   '.strip()])
# print(['   sssss   '.lstrip()])
# print(['   sssss   '.rstrip()])
# print(['aaaa   sssss   aaa'.strip('a ')])
#
# print('hello-world'.split('-'))
# print('hello is not good'.partition('is'))
#
# l1 = ['apple', 'car', 'pen']
#
# print(''.join(l1))
#
# print('hellloll'.replace('ll','0'))
# # string[::3]
#
# # min(3,4,5,2)
# # min([3,4,5,2])
# #
# #
# # max()
# #
# # sum()
#
# print(sorted([3,4,6,1],reverse=True))
#
# print(pow(2, 25))
#
# print(2**25)

# def fun(name, age=4, *args, **kwargs):
#     print('Hello', name, age)
#     print(args)
#     print(kwargs)
#
# fun('Max', 55, 'Karina', True, 100, name_='Oleg', house=55)
#
# def func(a,b,c):
#     print(a,b,c)
#
# l =[1,4,7]
# func(*l)

 # i = 5
# while i >0:
#     i-=1
#     if i ==2:
#         continue
#     print(i)
# else:
#     print('finish')
#
# l1 = [1,2,3,4,5,6]
# r = range(10)
# for i in range(1, 11,2):
#     print(i)
# else:
#     print('finish')

# d = {
#     'name':'Max',
#     'house':25
# }
#
# for k, v in d.items():
#     print(f'{k=}: {v=}')
#     print(v)

l2 = [4,2,7,2,4,1]
# res = [i for i in l2 if i%2==0]
# res= [i*2 for i in l2]
# res= [ i*2 for i in l2 if i%2==0]
# res= [i*2 if i%2==0 else i for i in l2]
# print(res)

l2d = [
    [1,2,3,4,5],
    [6,7,8,9,10]
]
# l=[i for j in l2d for i in j]

l= []
for j in l2d:
    for i in j:
        l.append(i)

print(l)

for i in range(10):
    print(i)