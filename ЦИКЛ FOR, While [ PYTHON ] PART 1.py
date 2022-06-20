#####################

######Цикл FOR #######
#####################

#1 Пример
######################################
#lower_words = ['ya', 'kak', 'iuda']
#upper_words = []
#
#for words in lower_words:
#    upper_words.append(words.upper())
#    print(words)
#    print(upper_words)
######################################


#2 Пример
######################################
#vlan = (2,3,4,100,200,300)
#for id in vlan:
#    print(f'vlan{id}')
#    print(f' name VLAN_{id}')
#    print(' exit\n')
######################################


#3 Пример
######################################

#  router = {
#     'hostname': 'R1',
#     'ip domain-name': 'ithub.ru',
#     'int loopback0': '1.1.1.1',
# }
# for key in router:      #key рандомное название переменной : Ключи
#     print(key)
#
# print('\n')
#
# for zna4eniya in router:    #Цикл фор с выводом только значений
#     print(router[zna4eniya])
######################################


#4 Пример
######################################
# router = {
#      'hostname': 'R1',
#      'ip domain-name': 'ithub.ru',
#     'int loopback0': '1.1.1.1',
# }
#
# for key in router:
#     print(key, router[key])
#
# print('\n')
#
# for key, value in router.items():
#     print(key, value)
######################################


#!1 Лайфхак
######################################
#string = 'Python'
#for letter in string:
#    print(letter)
#Вывожит по букве слово P y t h o n
######################################


#!2 Лайфхак
######################################
#list1 = [1,2,3,4,5,6,7,8,9,10]
#print(list1)
#
#range1 = list(range(1,16))
#print(range1)
######################################


######################################
#for i in range(1,25):
#    print(f'interface FastEthernet 0/{i}')
#    print(' no shut down')
#    print(' exit')
######################################


######################################
# cmd = ['no shutdown','exit']
# intf = [0,1,2,3] #intf = range(0,4)
#
# for i in intf:
#     print(f'interface FastEthernet 0 / {i}')
#     for on in cmd:
#         print(on)
######################################


######################################
# access_cmd = ['switchport mode access', 'switchport access vlan']
# access_intf_vlan = {'0/0': 100, '0/1': 200, '0/2': 300, '0/3': 400}
#
# for intf, vlan in access_intf_vlan.items():
#     print(intf, vlan)
#     print(f'interface GigabitEthernet' + intf)
#     for cmd in access_cmd:
#         if cmd.endswith('access vlan'):
#             print(f'{cmd} {vlan}')
#         else:
#             print(f'{cmd}')
######################################
