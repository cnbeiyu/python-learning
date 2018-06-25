#username 形参 timmy 实参
def greet_user(username):
  print('hello world,' + username.title() + "!")

greet_user("timmy")


#位置实参
def describe_pet(type,name):
  print('\nI have a ' + type + '.')
  print('My ' + type + ' named ' + name.title() + '.')

a = input('type\n')
b = input('name\n')
describe_pet(a,b)
a = input('type\n')
b = input('name\n')
#关键字实参,可以打乱实参顺序
describe_pet(type=a,name=b)


# 形参可以指定默认值，有默认值的形参一定要放在无默认值的形参后面！！！

def _pet(name, type='qqq'):
    print(type, name)
_pet('www')

# 返回值


def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name.title()

musician = get_formatted_name('timmy', 'tommy')
print(musician)

# 让实参变成可选的


def get_name(first, last, middle=''):
    if middle:
        # 如果有middle，middle将为ture
        full = first+' '+middle + ' '+last
    else:
        full = first + " " + last
    return(full)

musician = get_name('a','c','b')
print(musician)
musician = get_name('a','c')
print(musician)

#返回字典

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('a', 'b', 27)
print(musician)

#函数中while死循环和退出
def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name.title()

while True:
    print("\nplease tell me your name")
    print("(enter'q'at any time to quit)")

    f_name = input('First name:')
    if f_name == 'q':
        break

    l_name = input('Last name:')
    if f_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nhello,'+formatted_name+'!')

# 传递列表


def greet_users(names):
    for name in names:
        msg = 'hello,' + name.title()+"!"
        print(msg)

usernames = {'hannah', 'ty', 'margot'}
greet_users(usernames)


#在函数中修改列表
def print_models(unprinted_designs,completed_models):
    '''模拟打印直到没有未打印的设置
    打印后移到列表completed_models中
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟打印
        print('printing model :'+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nthe following models have been prined:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['a','b','c']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#禁止函数修改列表
'''在上方代码块中用切片表示法[:]
    用print_models(unprinted_designs[:],completed_models)调用
    这样使用的是列表副本，而不是列表本身。
'''

#传递任意数量的实参 *创建空元组，**创建空字典
def make_pizza(*toppings):
    '''
        *toppings让函数收到的所有值都封装到一个名为toppings的空元组中
    '''
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushuroom','apple','cheese')

def make_pizza(*toppings):
    '''
        *toppings让函数收到的所有值都封装到一个名为toppings的空元组中
    '''
    print('\nmake a pizza with these toppings:')
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushuroom','apple','cheese')




def build_profile(first,last,**user_info):
    '''**userr_info让函数创建一个名为user_info的空字典，并将所收到的值-对封装'''
    '''创建一个字典，其中包含用户的一切'''
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

#导入模块
'''import 模块名
调用函数 模块名.函数()
#导入特定函数
from 模块名 import 函数名
#导入任意数量函数
from 模块名 import 函数名1,函数名2，。。。

#使用as给函数指定别名
from 模块名 import 函数名 as 新函数名
from pizza import make_pizza as mp

#导入模块所有函数
from 模块名 import*'''

