#coding=utf-8 
# message = input('please\n')
# print(message)

# name = input('please enter your name： ')
# print('hello,' + name)

# prompt = 'if you tell us'
# prompt += '\nyourname'
# name = input(prompt)

# print(name)


# age = input('how old are you?')
# age = int(age)
# if age >= 18:
#     print('you can do anything')
# else:
#     print('sorry you cannot')

# # 求模运算符判断寄偶
# number = input('please enter a number')
# number = int(number)
# if number % 2 == 0:
#     print('oushu')
# else:
#     print('qishu')

# # FOR用于集合中的一个代码块，while循环不断运行
# current_number = 1
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# prompt = '\ntell me some thing:'
# prompt += "\nenter 'quit' to end it"
# message = 'hi'
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# # 使用标志
# prompt = '\ntell me some thing:'
# prompt += "\nenter 'quit' to end it"

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# # break语句 退出循环
# prompt = '\ntell me some thing:'
# prompt += "\nenter 'quit' to end it"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print('go on')

# # continue语句 返回循环开头
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#     	continue
#     print(current_number)


# number = input("please enter a number")
# number = int(number)
# if number %10 == 0:
# 	print('bingo')
# else:
# 	print('ohno')


# #while 处理列表之间的移动 pop()删除后会返回删除值
# unconfirmed_users = ['alics','brian','candace']
# confirmed_users = []

# while unconfirmed_users:#这一行不懂
# 	current_user = unconfirmed_users.pop()

# 	print('verifying user:' + current_user.title())
# 	confirmed_users.append(current_user)

# print('\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

#删除包含特定值的所有列表函数 remove()
pets = ['dog','ca的','dog','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
	name = input('\nwhats your name')
	response = input('which mountain would you like to climb someday')

	responses[name] = response

	repeat = input('would you like to let another person respond(yes/no)')
	if repeat =='no':
		polling_active = False
print('\n---results---')
for name,response in responses.items():
	print(name + 'would like to climb' + response + ".")
