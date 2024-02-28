# text = 'Hello World'
# print(hex(id(text)))
#
# text = 'Hello World 2'
# print(hex(id(text)))


# text = 'Hello World'
# print(hex(id(text)))
#
# text += ' Salom Dunyo'
# print(hex(id(text)))
#
#
# num1 = 45

# --------------------------------------------------------------

# users = ['Toxir', 'Sobir']
# print(users)
# print(hex(id(users)))
#
# users.append('Akmal')
# print(users)
# print(hex(id(users)))


# def add_user(l: list):
#     username = input("User: ")
#     l.append(username)
#
# users = ['Toxir', 'Sobir']
#
# add_user(users)
# print(users)



# def add_user(l = []):
#     if l:
#         users_list = l.copy()
#     else:
#         users_list = []
#     username = input("User: ")
#     users_list.append(username)
#     print(users_list)
#
# users = ['Toxir', 'Sobir']
#
# add_user()
# print(users)


# ------------------------------------------------------------------------------------------------------
# str, list, tuple, dict

# text = 'Hello World'
#
# print(text.title())
# print(text.capitalize())
# print(text.upper())
# print(text.lower())
# print(text.startswith('Hello'))
# print(text.endswith("ld"))
# print(text.center(20, '*'))
# print(text.split('l'))
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.isprintable())

# ------------------------------------------------------------------------------------------------------

# list

# l = []
# l2 = list()
#
# print(l)
# print(l2)


# users = ['Toxir', 'Sobir']
# users[1] = 'Jalil'
#
# users.append('Sobir')
# users.append('Akmal')
# users.append('Kamol')
# users.insert(2, 'Ali')
# users.extend(['Kim', 'Chen', 'In'])
# users.extend(('Abdusalom',))

# ----------------------------------------------
# list(start:end:step)

# users = ['Toxir', 'Jalil', 'Ali', 'Sobir', 'Akmal', 'Kamol', 'Kim', 'Chen', 'In', 'Abdusalom']

# print(users[1:5])
# print(users[3::])
# print(users[1:5:2])
# print(users[1::2])
# print(users[::-1])

# cars


# ----------------------------------------------
# .pop(), .remove(), del

# users = ['Toxir', 'Jalil', 'Ali', 'Sobir', 'Akmal', 'Kamol', 'Kim', 'Chen', 'In', 'Abdusalom']

# users.remove('Ali')
# new_users = [users.pop(2)]
# print(new_users)

# del users[0]
#
# print(users)

#
# --------------------------------------------------------------------------------------------------

# t = tuple()
# t2 = ()

# index(value, start, end)

# users = ('Toxir', 'Sobir', 'Jalil', 'Akmal', 'Botir', 'Jalil')
#
# # print(users[3])
# # print(users.count('Jalil'))
# print(users.index('Jalil', 3))


# users = ('Toxir', 'Sobir', 'Jalil', 'Akmal', 'Botir', 'Jalil')


# while True:
#     username = input("Username: ")
#     index = users.index(username)
#     print(index)
#     command = input(">>>: ")
#     if command == 'next':
#         try:
#             index = users.index(username, index + 1)
#             print(index)
#         except:
#             print("Jo'q")


# user1, user2 = ['Toxir', 'Sobir']
#
# print(user1)
# print(user2)


# --------------------------------------------------------------------------------------------------
# [], (), {}

# d1 = {}
# d2 = dict()
#
# print(d1)
# print(d2)


# user_info = {'name': "Sobirjon", 'lastname': 'Sobirov', 'age': 20}

# user_info['name'] = 'Toxir'

# user_info['phone'] = '+998991234567'

# print(user_info.get('name'))

# print(user_info.get('address'))

