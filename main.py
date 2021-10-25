# 1) Создать переменную типа String
string_type = 'Yana Litorina'

# 2) Создать переменную типа Integer
integer_type = 25

# 3) Создать переменную типа Float
float_type = 12.34

# 4) Создать переменную типа Bytes
bytes_type = bytes(11)

# 5) Создать переменную типа List
list_type = [12, 'Yana', ['Litorina', 25]]

# 6) Создать переменную типа Tuple
typle_type = (12, 'Yana')

# 7) Создать переменную типа Set
set_type = set('yana')
# 8. Создать переменную типа Frozen set
frozenset_type = frozenset('129754')

# 9) Создать переменную типа Dict
dict_type = {'name': 'Yana',
             'key': 1234}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(string_type), string_type)
print(type(integer_type), integer_type)
print(type(float_type), float_type)
print(type(bytes_type), bytes_type)
print(type(list_type), list_type)
print(type(typle_type), typle_type)
print(type(dict_type), dict_type)
print(type(set_type), set_type)
print(type(frozenset_type), frozenset_type)

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
a = 'Yana '
b = 'Litorina'
c = a + b
print(c)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
k = 'Hello'
d = 123
print(k, d)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
name = 'Yana'
age = 25
rez = name + str(age)
print(rez)
