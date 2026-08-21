# tuple1=1,2
#
# a,b = tuple1
#
# print(a,b)
#
# a = 5
# b = 7
# a,b = (b,a)
#
# l = [2,4,1,7,4,7]
#
# # _,b,*_,y,z=l
#
# *_,x,y,z = l
# print(x,y,z)
#
# arg=[2,3,4]
#
# dict_args ={
#     'arg1':8,
#     'arg2':9,
#     'arg3':10,
# }
#
# def func(arg1, arg2, arg3):
#     print(arg1,arg2,arg3)
#
# func(**dict_args)
#
# def decor(func):
#     def inner(*args, **kwargs):
#         print('*************************')
#         func(*args, *kwargs)
#         print('*************************')
#     return inner
#
# def decor2(func):
#     def inner(*args, **kwargs):
#         print('--------------------------')
#         func(*args, *kwargs)
#         print('--------------------------')
#     return inner
#
# @decor
# @decor2
# def greeting(name):
#     print(f"Hello, {name}")
#
# greeting("Olga")
#
# greeting_decor = decor(greeting)
#
# greeting_decor("Max")
# name = 'max'

# def func():
#     pass
# for i in range(5):
#     print(i)
# print(i)
#
# print(globals())

# name = 'Oleg'
#
# def a():
#     name = 'Max'
#     print(locals())
#
# print(globals())
#
# a()
#
# def a():
#     name = 'Vasya'
#
#     def b():
#         nonlocal name
#         # global name
#         name = 'Petia'
#         print(name)
#     b()
#     print(name)
#
# a()
# print(name)

# def counter():
#     count=0
#     def inner():
#         nonlocal count
#         count +=1
#         return count
#     return inner
#
# counter_1 = counter()
# counter_2 = counter()
#
# print(counter_1())
# print(counter_2())
# print(counter_1())
# print(counter_1())
# print(counter_1())
# print(counter_2())

# func = lambda a,b: a+b
#
# print(func(5,6))
#
# l = [1,2,3,4,5]
#
# m=map(lambda item: item **2, l)
# f = filter(lambda x: x % 2 == 0, l)
# for i in m:
#     print(i)
# for i in f:
#     print(i)

# users =[
#     {'name':'max', 'age':2},
#     {'name':'olha', 'age':35},
#     {'name':'karina', 'age':20},
#     {'name':'kamila', 'age':1},
# ]
#
# users.sort(key=lambda x: len(x['name']))
#
# print(users)
#
# def func(names:list[str])->dict:
#     name = '333'
#     return {'name':name}
#
# import typing

from typing import Any, TypedDict, Callable

# a:int = 'sdfdsg'
#
# print(a)

# my_type = str|int|bool
#
# def func ()->my_type:
#     return True

# def func()-> None:
#     return

# User = TypedDict('User', {'name':str, 'age':int, 'house':int})
#
# users:list[User] = [
#     {'name':'Max', 'age':15, 'house':55},
#     {'name':'Max', 'age':15, 'house':100},
# ]

def counter(a:str, b:int)-> Callable[[bool,list[str]],int]:
    count = 0

    def inner(f:bool,y:list[str])->int:
        nonlocal count
        count +=1
        return count
    return inner