# 1) написати функцію (notebook) на замикання, котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
#
# – перший записує в список нову справу
#
# – другий повертає всі записи
#
# (приклад сигнатури функції notebook у вкладенні )

# def notebook():
#     todo_list:list[str] = []
#     def add_list(todo:str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#     def get_all()->list[str]:
#         nonlocal todo_list
#         return todo_list.copy()
#
#     return add_list,get_all
#
# add1, get_all1 = notebook()
# add2, get_all2 = notebook()
#
# add1('apple')
# add2('HP')
# add1('go to home')

# print(get_all1())
# print('*********************************')
# print(get_all2())



# 3) створити функцію, котра буде повертати суму розрядів числа у вигляді строки(також використовуємо типізацію)
#
# Приклад:
#
# expanded_form(12)  # return ’10 + 2′
#
# expanded_form(42)  # return ’40 + 2′
#
# expanded_form(70304)  # return ‘70000 + 300 + 4’
#

# def expanded_form(num:int) ->str:
#     st = str(num)
#     length = len(st)-1
#     res=[]
#     for i, ch in enumerate(st):
#         if ch != '0':
#             res.append(ch + '0' * (length - i))
#     return ' + '.join(res) + f' = {st}'
#
# print(expanded_form(243544))

# 4) створити декоратор, котрий буде підраховувати, скільки разів була запущена функція, продекорована цим декоратором, та буде виводити це значення після виконання функцій
#
# приклад декоратору у вкладенні

def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')

    return inner


@count_decor
def func1():
    print('func1')


@count_decor
def func2():
    print('func2')

func1()
func1()
func2()
func2()
func1()
func1()
func1()
func2()