#################################################################

######################## #########################
#################################################################
# username = 'Admin'
# password_correct = True
# while password_correct:
#     password = input(f'Введите пароль для{username}:')
#     if len(password) < 10:
#         print('Пароль слишком короткий: ')
#     elif username in password:
#         print('Пароль содержит имя пользователя: ')
#     else:
#         print(f'Пароль для пользователя {username} установлен!')
#         password_correct = False
#########################
#
#
#
#########################
# def null_func ():
#     pass
#
# class NullClass:
#     pass
#########################
#
#
#
#########################
#for num in range(1, 5):
#     if num < 3:
#         pass
#     else:
#         print(num)
#///
# for num in range(10):
#     if num < 5:
#         print(num)
#     else:
#         break
#
#########################
#
#
# i = 0
# while i < 5:
#     if == 3:
#         break
#     else:
#         print(i)
#         i += 1
#
#########################
# username = 'Admin'
# while True:
#     password = input(f'Введите пароль для{username}:')
#     if len(password) < 10:
#         print('Пароль слишком короткий: ')
#     elif username in password:
#         print('Пароль содержит имя пользователя: ')
#     else:
#         print(f'Пароль для пользователя {username} установлен!')
#         password_correct = False
#########################
# for num in range(10):
#     if num == 4:
#         continue#С континиу будет дальше выводить#pass#
#         print('ЭТА СТРОКА НИКОГДА НЕ БУДЕТ ВЫВЕДЕНА')
#     elif num ==4:
#         pass
#         print('ЭТО СТРОКА ПРОПУЩЕНА')
#     else:
#         print(num)
#     print(f'Итерация цикла № {num} завершена полностью')
#########################
# username = 'Admin'
# password_correct = True
# password = input(f'Введите пароль для {username}: ')
# while password_correct:
#     if len(password) < 10:
#         print('Пароль слишком короткий: ')
#     elif username in password:
#         print('Пароль содержит имя пользователя: ')
#     else:
#         print(f'Пароль для пользователя {username} установлен!')
#         password_correct = False
#         continue
#     password = input(f'Введите Повторно для {username}: ')
#########################
# for num in range(10):
#     if num == 4:
#         pass#continue
#     else:
#         print(num)
# else:
#     print('Цикл завершнен')
#########################
# for num in range(10):
#     if num == 4:
#         break#Вырубает цикл до 4 и дальше код обрубается
#     else:
#         print(num)
# else:
#     print('Цикл завершнен')
#########################
#i = 0
#while i < 5:
#    if i ==3:
#        pass
#    else:
#    i += 1
#########################
#
# while True:
#     try:
#         a = input('Введите делитель: ')
#         b = input('Введите делитель: ')
#         print(f'{a} / {b} =', int(a)/int(b))
#         print(a)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя')
#     except ValueError:
#         print('Делитель можно только числа!!!')
# #    except(ValueError, ZeroDivisionError):
# #        print('Так нельзя')

# raise ValueError('Pizdec Systeme')
#
#
# Задание 1:
# написать три разных цикла выполняющих какое-нибудь просто полезное действие.
# 1. Завершить через False
# 2. Завершить через break
# 3. Использовать внутри цикла continue

# username = 'Admin'
# password_correct = True
# while password_correct:
#     password = input(f'Введите пароль для{username}:')
#     if len(password) < 10:
#         print('Пароль слишком короткий: ')
#     elif username in password:
#         print('Пароль содержит имя пользователя: ')
#     else:
#         print(f'Пароль для пользователя {username} установлен!')
#         password_correct = False
#########################


# while True:
#     vlan = int(input("Введи влан : "))
#     cmd3 = ['no shutdown']
#     cmd2 = ['switchport nonegotiate']
#     cmd1 = [f'switchport access vlan {vlan}', ' switchport mode access', ' exit']
#     if vlan >= 4:
#         print(f'Введеный вами Vlan: [ {vlan} ] слишком большой, Введи меньше 4: ')
#         break
#     elif vlan == 1:
#         print(f'На введеный вами Vlan:[ {vlan} ] применились настройки: {cmd1} ')
#         continue
#     elif vlan == 2:
#         print(f'На введеный вами Vlan: [ {vlan} ] применились настройки: {cmd2} ')
#         continue
#     elif vlan == 3:
#         print(f'На введеный вами Vlan: [ {vlan} ] применились настройки: {cmd3}')
#         vlan = False
#     break
# username = 'Admin'
# password_correct = True
# password = input(f'Введите пароль для {username}: ')
# while password_correct:
#     if len(password) < 10:
#         print('Пароль слишком короткий: ')
#     elif username in password:
#         print('Пароль содержит имя пользователя: ')
#     else:
#         print(f'Пароль для пользователя {username} установлен!')
#         password_correct = False
#         continue
#     password = input(f'Введите Повторно для {username}: ')
# nums = range(25, 1000)
# cmd1 = [f'switchport access vlan {vlan}', ' switchport mode access',no shutdown' exit']
# Vlan = int(input('Введите Vlan: '))
# while True:
#     if == nums:
#          break
#     else:
#         print(f'На введеный вами Vlan применились настройки: {cmd1} ')

try:
    vlan = []
    ciforka = int(input("Введи cifru: "))
except ValueError:
    print('ОШИБКА В СИНТАКСЕ')
else:
    print(ciforka)
finally:
    print('Запустите по новой скрипт')



