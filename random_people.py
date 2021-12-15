import random
import sqlite3


names = ['Александр', 'Михаил', 'Дмитрий', 'Даниил', 'Иван', 'Кирилл', 'Роман', 'Егор', 'Матвей', 'Тимофей', 'Максим',
         'Максим', 'Павел' ,'Сергей' ,'Ярослав' ,'Алексей' ,'Константин' ,'Артем', 'Юрий']
surnames = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Захаров', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Федоров',
            'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семёнов', 'Кузьмин', 'Павлов', 'Козлов', 'Степанов']
print('\n')
phone_regions = ['900', '932', '999', '921', '911', '950', '969']
alhabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
mails = ['mail.ru', 'gmail.com', 'yandex.ru', 'bk.ru']
for i in range(43):
    s = ''
    for i in range(7):
        s += random.choice("0123456789")
    print('7' + random.choice(phone_regions) + s)
    # print(random.choice(names), random.choice(surnames))
    # for i in range(random.choice([5, 6, 7, 8, 9, 10, 11, 12])):
    #     s += (random.choice([random.choice(numbers), random.choice(alhabet)]))
    # print(s + "@" + random.choice(mails))



