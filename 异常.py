# #处理ZeroDivisionError异常
# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print('You cannot divide by zero')
# '''
# 	try-except代码块，如果try代码没问题，将跳过except代码块
# 	如果try代码块有报错，python将查找这样dexcept代码块，并运行其中代码
# 	用户将看到友好的错误信息，而不是traceback
# '''

# #使用异常避免崩溃
# print('Please give me two numbers,and i will divide them')
# print("Enter 'q' to quit.")

# while True:
# 	first_number = input('First number:')
# 	if first_number =='q':
# 		break
# 	second_number = input('Secondnumber')
# 	try:
# 		answer = int(first_number)/int(second_number)
# 	except ZeroDivisionError:
# 		print('You cannot divide by 0!')
# 	else:
# 		print(answer)

#处理FileNotFoundError异常
filename = 'alice.txt'

try:	
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = 'Sorry,the file ' + 'filename' + ' does not exist.'
	print(msg)









