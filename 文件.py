
 #coding=utf-8 
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	#rstrip()删除末尾空行
'''
	open()是使用文件必备函数,都要先打开文件,open接受一个参数，文件名称
	open()返回一个表示文件的对象
	关键字with在不需要访问文件后将其关闭，等于打开后调用close()，
	read()读取文件内容，并储存在变量中
'''
#绝对路径
file_path = 'C:\\Users\\贝鱼\\Desktop\\python\\p_digits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

#逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#创建一个包含文件各行的列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	#readlines()从文件读取每一行，并储存在lines列表中

for line in lines:
	print(line.rstrip())

#使用文件内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()
	#strip()删除全部空格

print(pi_string)
print(len(pi_string))
#len()返回字符串长度


#写入文件
#r读取 w写入 a附加 r+读取写入 省略 默认只读
filename = 'programming.txt'
with open(filename,'w') as file_object:
	#open()函数第一个实参是文件名称，第二个实参是模式，'w'告诉python是写入模式
	file_object.write('I love programming.\n')
	file_object.write('I love python.\n')

#增加到文件

filename = 'programming.txt'
with open(filename,'a') as file_object:
	#实参a表示将内容增加到文件末尾，而不是覆盖
	file_object.write('I also love c.\n')

#练习
guest = input('please enter your name:\n')
with open(filename,'w') as file_object:
	file_object.write(guest)

filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")


