#coding=utf-8 
# message = input('please\n')
# print(message)

# name = input('please enter your name�� ')
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

# # ��ģ������жϼ�ż
# number = input('please enter a number')
# number = int(number)
# if number % 2 == 0:
#     print('oushu')
# else:
#     print('qishu')

# # FOR���ڼ����е�һ������飬whileѭ����������
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

# # ʹ�ñ�־
# prompt = '\ntell me some thing:'
# prompt += "\nenter 'quit' to end it"

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# # break��� �˳�ѭ��
# prompt = '\ntell me some thing:'
# prompt += "\nenter 'quit' to end it"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print('go on')

# # continue��� ����ѭ����ͷ
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


# #while �����б�֮����ƶ� pop()ɾ����᷵��ɾ��ֵ
# unconfirmed_users = ['alics','brian','candace']
# confirmed_users = []

# while unconfirmed_users:#��һ�в���
# 	current_user = unconfirmed_users.pop()

# 	print('verifying user:' + current_user.title())
# 	confirmed_users.append(current_user)

# print('\nThe following users have been confirmed:')
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

#ɾ�������ض�ֵ�������б��� remove()
pets = ['dog','ca��','dog','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#ʹ���û�����������ֵ�
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
