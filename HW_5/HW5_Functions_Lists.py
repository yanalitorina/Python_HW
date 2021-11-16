import calendar
import random
import math
import string
import gender_guesser
import gender_guesser.detector
import names
import randomtimestamp
import _strptime
from Functions_5 import *

#  - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.
#
# # 1. Написать скрипт который в создаст список целых чисел.
# list_cel = list(range(24))
# print('Cel =', list_cel)
#
# # 2. Написать скрипт который в создаст список целых чётных чисел.
# cel_chet = list(range(0, 140, 2))
# print('Cel_chet =', cel_chet)
#
# # 3. Написать скрипт который в создаст список целых нечётных чисел.
# cel_nechet = list(range(1, 141, 2))
# print('Cel_ne_chet =', cel_nechet)
#
# # 4. Написать скрипт который из списка целых чисел выведет чётные числа.
# list_all = random.sample(range(0, 80), 70)
# print('List_all =', list_all)
# chet = []
#
# for i in list_all:
#     if i % 2 == 0:
#         chet.append(i)
#
# print('Chet =', chet)
#
# # 5. Написать скрипт который из списка целых чисел выведет нечётные числа.
# list_all = random.sample(range(0, 80), 70)
# print('List all =', list_all)
# ne_chet = []
#
# for i in list_all:
#     if i % 2 != 0:
#         ne_chet.append(i)
#
# print('Ne chet =', ne_chet)
#
# # 6. Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
# list_all = random.sample(range(0, 100), 70)
# print('List all =', list_all)
# chet_na5 = []
#
# for i in list_all:
#     if (i % 2 == 0) and (i % 5 == 0):
#         chet_na5.append(i)
#
# print('Chet / 5  =', chet_na5)
#
# # 7. Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
# list_all = random.sample(range(0, 80), 70)
# print('List all =', list_all)
# chet_na5 = []
#
# for i in list_all:
#     if (i % 2 == 0) and (i % 5 == 0):
#         chet_na5.append(i)
# print('Chet / 5  =', chet_na5)
# number_cht = len(chet_na5)
# print('Kol_chet / na 5  =', number_cht)
#
# # 8. Написать скрипт который в создаст список целых рандомных чисел.
# list_cel_rand = random.sample(range(0, 100), 70)
# print('List cel random =', list_cel_rand)
#
# # 9. Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
# razbienie(list_cel)
#
# # 10. Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
# return_spiski(list_cel)
# # 11. Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
# list_1 = random.sample(range(0, 50), 5)
# list_2 = random.sample(range(0, 50), 5)
# list_3 = random.sample(range(0, 50), 5)
# print('List_1 =', list_1)
# print('List_2 =', list_2)
# print('List_3 =', list_3)
# list_all = [list_1, list_2, list_3]
# print('5_star =', list_all)
#
# # 12. Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
# list_sum = list_1 + list_2 + list_3
# print('List_sum =', list_sum)
#
# 13. Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100,
# а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”
# sum_5_stars(list_all)
#
# 14. Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
# kybishka()
#
# 15. Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из
# введенного количества лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании,
# активностей которые может делать QA. Free implementation of function body logic
# junior_salary()
#
# # 16. Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
# list_names =[]
# for i in range(70):
#     list_names.append(names.get_first_name())
# print('First names =', list_names)
#
# # 17. Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.
# list_names = []
# count = 0
# for i in range(70):
#     count += 1
#     name = 'file_' + str(count) + '.py'
#     list_names.append(name)
# print('Names files =', list_names)
#
# # 18. Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это имя пользователя
# # , а 1-й - элемент это дата регистрации.
# list_all = []
# for i in range(70):
#     list_temp = [names.get_first_name(), str(randomtimestamp.random_date())]
#     list_all.append(list_temp)
# print('All list =', list_all)
#
# # 19. Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# # 0-й - элемент - это имя пользователя,
# # 1-й - элемент - это логин,
# # 2-й - элемент - это пароль,
# # 3-й - элемент - это email (email тоже генерировать),
# # 4-й - элемент - это дата регистрации
# list_employees = []
# list_temp = []
# for i in range(10):
#     names_rand = names.get_first_name()
#     login_rand = "".join(names_rand + str(''.join(random.sample(string.digits, 5))))
#     password_rand = "".join(random.sample((string.ascii_letters + string.digits), 6))
#     email_rand = "".join(names_rand + str(''.join(random.sample(string.digits, 2))) + '@gmail.com')
#     regist_data = str(randomtimestamp.random_date())
#     list_temp = [names_rand, login_rand, password_rand, email_rand, regist_data]
#     list_employees.append(list_temp)
# print('Employees =', list_employees)
#
# # 20. Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# # 0-й - элемент - это логин,
# # 1-й - элемент - это имя,
# # 2-й - элемент - семейный статус (True, False - генерировать рандомно)
# list_family = []
# for i in list_employees:
#     family_status = random.choice([True, False])
#     list_temp = [i[1], i[0], family_status]
#     list_family.append(list_temp)
# print('Family =', list_family)
#
# # 21. Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# # 0-й - элемент - это логин,
# # 1-й - элемент - это имя,
# # 2-й - элемент - гендер (1-м, 0-ж)
# list_gender = []
# for i in list_employees:
#     gender_detector = gender_guesser.detector.Detector()
#     gender_d = gender_detector.get_gender(i[0])
#     if (gender_d == 'female') or (gender_d == 'mostly_female'):
#         gender_d = 0
#     else:
#         gender_d = 1
#     list_temp = [i[1], i[0], gender_d]
#     list_gender.append(list_temp)
# print('Gender =', list_gender)
#
# # 22. Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# # 0-й - элемент - это логин,
# # 1-й - элемент - это имя,
# # 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
# list_salary = []
# for i in list_employees:
#     salary = "".join(str(random.randint(300, 5000)) + '$')
#     list_temp = [i[1], i[0], salary]
#     list_salary.append(list_temp)
# print('Salary =', list_salary)
#
# # 23. Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$
# list_name_zp = []
# for i in list_salary:
#     if (i[2] >= '1500$') and (i[2] <= '3000$'):
#         list_name_zp.append(i[1])
# print('Salary >=1500 and >= 3000 =', list_name_zp)
#
# # # 24. Написать скрипт который создаст список имён мужчин из gender.
# list_man = []
# for i in list_gender:
#     if i[2] == 1:
#         list_man.append(i[1])
# print('Men =', list_man)
#
# # # 25. Написать скрипт который создаст список имён женщин из gender.
# list_wom = []
# for i in list_gender:
#     if i[2] == 0:
#         list_wom.append(i[1])
# print('Women =', list_wom)
#
# # 26. Написать скрипт который создаст список имён неженатых мужчин из family.
# list_false_man = []
# gender_detector = gender_guesser.detector.Detector()
# for i in list_family:
#         if i[2] == False and gender_detector.get_gender(i[1]) == 'male':
#            list_false_man.append(i[1])
# print('Single men =', list_false_man)
#
# # 27. Написать скрипт который создаст список имён незамужних женщин из family.
# list_false_women = []
# gender_detector = gender_guesser.detector.Detector()
# for i in list_family:
#         if i[2] == False and gender_detector.get_gender(i[1]) == 'female':
#            list_false_women.append(i[1])
# print('Single women =', list_false_women)
#
# # 28. Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees,
# # family, gender, salary. Реализуйте как скрипт, без функций
# list_man_zp = []
# gender_detector = gender_guesser.detector.Detector()
# for i in list_salary:
#      if i[2] == '1500$' and gender_detector.get_gender(i[1]) == 'male':
#          list_man_zp.append(i[1])
# print('Men\'s salary 1500$ =', list_man_zp)
#
# # 29. Реализуйте пункт 28 через через функции.
# print('Function salary man =', salary_man(list_salary, '1500$'))