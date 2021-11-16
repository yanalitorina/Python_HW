import math
import gender_guesser.detector


def razbienie(list):
    list_new = []
    lists = []
    for i in list:
        lists.append(i)
        if len(lists) > 4:
            list_new.append(lists)
            lists = []
        elif i == list.index(len(list) - 1):
            list_new.append(lists)
    print('List_new =', list_new)

    # Second variant
    # list_list = []
    # list_temp = []
    # for i in list:
    #     if (list.index(i) + 1) % 5 == 0:
    #         list_temp.append(i)
    #         list_list.append(list_temp)
    #         list_temp = []
    #     elif list.index(i) == len(list)-1:
    #         list_temp.append(i)
    #         list_list.append(list_temp)
    #     else:
    #         list_temp.append(i)
    # print(list_list)


def return_spiski(list):
    list_chet = []
    list_ne_chet = []
    for i in list:
        if i % 2 == 0:
            list_chet.append(i)
        else:
            list_ne_chet.append(i)
    print('Chet', list_chet)
    print('Ne_chet', list_ne_chet)


def sum_5_stars(list):
    more_100 = []
    smaller_100 = []

    for i in list:
        sum = 0
        for a in i:
            sum = sum + a
        print('sum', sum)
        if sum >= 100:
            more_100.append(i)
        else:
            smaller_100.append(i)
    if more_100 == []:
        print("MORE_100 >> No lists")
        print(smaller_100)
    elif smaller_100 == []:
        print("SMOLLER_100 >> No lists")
        print(more_100)
    else:
        print(more_100)
        print(smaller_100)


def kybishka():
    list_goals = [10000, 20000, 30000, 50000, 100000]
    age = input('Введите ваш возраст: ')
    amount_in_year = 12000
    amount_in_year_usd = round(amount_in_year / 2.44)
    for i in list_goals:
        amount_age = round(i / amount_in_year_usd + int(age))
        sobrana_age = round(i / amount_in_year_usd)
        print("Сумма ", i, "$ будет вамми собрана через ", sobrana_age, " лет (года), а вам - ", amount_age, " лет")


def salary_man(list, salary):
    gender_detector = gender_guesser.detector.Detector()
    list_temp = []
    for i in list:
        if i[2] == '1500$' and gender_detector.get_gender(i[1]) == 'male':
            list_temp.append(i[1])
    return list_temp


def junior_salary():
    sal = int(input('Введите вашу стартовую зп ____$(Например 250):'))
    experience = int(input('Введите ваш стаж (Например 3):'))
    sql = input('Владеете ли вы SQL (y/n):')
    postman = input('Владеете ли вы Postman (y/n):')
    python = input('Владеете ли вы Python (y/n):')
    english = input('Владеете ли вы English B1 и выше (y/n):')
    for i in range(experience):
        print(i + 1, "year --> zp ", sal, '$')
        if sql == 'y':
            sal += 0.1 * sal
        else:
            print('Учите SQL')
        if postman == 'y':
            sal += 0.15 * sal
        else:
            print('Учите Postman')
        if python == 'y':
            sal += 0.2 * sal
        else:
            print('Учите Python')
        if english == 'y':
            sal += 0.25 * sal
        else:
            print('Учите English')
