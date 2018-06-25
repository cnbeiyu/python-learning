# -*- coding:utf-8 -*-
#分析文本 split() 统计单词数
#split()函数以空格为分隔符
#将字符串拆分多个部分，并储存到一个包含字符串中所有单词的列表中
filename = 'alice.txt'

try:	
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = 'Sorry,the file ' + 'filename' + ' does not exist.'
	print(msg)
else:
	#计算文件包含多少单词
	words = contents.split() 
	# split 以空格为分隔符分割字符串，返回一个包含所有单词的列表
	num_words = len(words)
	#len()返回列表长度
	print("The file " + filename + " has about " + str(num_words) + " words.")

def count_words(filename):
	try:	
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = 'Sorry,the file ' + 'filename' + ' does not exist.'
		print(msg)
	else:
		words = contents.split() 
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','mike.txt']
for filename in filenames:
	count_words(filename)

#存储数据
#json.dump()和json.load()

import json

numbers = [2,4,6,8,10]

filename = 'numbers.json'
with open(filename,'a') as f_obj:
	json.dump(numbers,f_obj)
	
#读取用户姓名
import json
filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input('plz enter your name')
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
		print('we remeber ' + username)
else:
	print('welcome back ' + username)

#练习10.11
import json
filename = 'number.json'
try:
	with open(filename) as f_obj:
		f_number = json.load(f_obj)
except FileNotFoundError:
	f_number = input('plz enter your name')
	with open(filename,'w') as f_obj:
		json.dump(f_number,f_obj)
		print('we remeber ' + str(f_number))
else:
	print('welcome back ' + str(f_number))