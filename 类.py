#coding=utf-8
#创建类
class Dog():
	"""一次模拟小狗的简单尝试"""

	def __init__(self,name,age):
		#__函数名__，函数前后加2根！！！下划线，python会在根据类创建新实例时自动运行它。
		"""初始化属性name和age"""
		'''self为类必备参数'''
		self.name = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令后蹲下"""
		print(self.name.title() + ' is now sitting.')


	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + ' rolled over!')

#根据类创建实例my_dog
my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + '.')
#print("My dog is " + str(my_dog.age) + "years old")

my_dog.sit()
my_dog.roll_over()
#创建多个实例
your_dog = Dog('lucy',3)
your_dog.sit()


#练习
class Restaurant():
	def __init__(self,name,typee):
		self.name = name
		self.typee = typee

	def describe(self):
		print("Restaurant's name is " + self.name.upper())
		print("Restaurant's type is " + self.typee.upper())

	def open(self):
		print(self.name + 'is openning')

first_restaurant = Restaurant('kfc','chicken')

first_restaurant.describe()
first_restaurant.open()


#练习
class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describle_user(self):
		print ("User's name is " + self.first_name + self.last_name)

	def greet_user(self):
		print("hello, " + self.first_name)

timmy = User("timmy","chaill")
timmy.describle_user()
timmy.greet_user()


#使用类和实例
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
#通过方法修改属性的值
	def update_odometer(self,mileage):
		'''禁止里程表调小'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('you can not roll back the odometer')
my_new_car = Car('audi','r8',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#通过方法对值递增
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('you can not roll back the odometer')

	def increment_odometer(self,miles):
		'''将里程表增加指定的量'''
		self.odometer_reading += miles

my_used_car = Car('bwm','z4','2010')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


#继承
class Car():
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('you can not roll back the odometer')

	def increment_odometer(self,miles):
		'''将里程表增加指定的量'''
		self.odometer_reading += miles

class ElectricCar(Car):
	'''继承'''
	def __init__(self,make,model,year):
		'''初始化父类属性,若要增加属性，在上行增加即可，下行无需增加'''
		super().__init__(make,model,year)
		'''super()是一个特殊函数，将父类和子类关联起来
		，让python调用父类的方法__init__()，让ElecyricCar
		实例包含父类的所有属性
		'''

my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()

#给子类定义属性和方法
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size = 70

	def describe_battery(self):

		print('This car has a ' + str(self.battery_size) + '-kwh battery')

my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#重写父类方法
#直接重新def即可

#将实例用作属性
class Battery():
	'''模拟电动汽车电瓶'''

	def __init__(self,battery_size=70):
		'''初始化电瓶属性'''
		self.battery_size=battery_size

	def describe_battery(self):
		'''
		打印一条描述电瓶容量的信息'''
		print('This car has a ' + str(self.battery_size) + '-kwh battery.')

	def get_range(self):
		'''打印一条消息，指出续航里程'''
		if self.battery_size ==70:
			range = 240
		elif self.battery_size ==85:
			range =270
		message = 'This car can= go ' + str(range)
		message += 'miles on a full charge.'
		print(message)

class ElectricCar(Car):
	def __init__(self,make,model,year):
		'''初始化'''
		super().__init__(make,model,year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#练习
class Restaurant():
	def __init__(self,name,typee):
		self.name = name
		self.typee = typee

	def describe(self):
		print("Restaurant's name is " + self.name.upper())
		print("Restaurant's type is " + self.typee.upper())

	def open(self):
		print(self.name + 'is openning')

class IceCreamStand(Restaurant):
	def __init__(self,name,typee,flavours):
		super().__init__(name,typee)
		self.flavours = flavours
		
	def print_IceCreamStand(self):
		print("Restaurant's flavours is " + self.flavours.upper())

second_restaurant = IceCreamStand('DQ','ICECREAM','ICE')
second_restaurant.print_IceCreamStand()


class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describle_user(self):
		print ("User's name is " + self.first_name + self.last_name)

	def greet_user(self):
		print("hello, " + self.first_name)

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = ['can ban post','can add post']

	def show_privileges(self):
		print(self.first_name + "'s privileges is " + self.privileges[1])

admin = Admin('timmy','cahill')
admin.show_privileges()



# #12.23 未解决
# class Privileges():
# 	def __init__(self,privileges):
# 		slef.privileges = ['can ban post','can add post','can delete post']

# 	def show_privileges(self):
# 		print('Timmy' + "'s privileges is " + self.privileges[0])

# class Admin(Privileges):
# 	def __init__(self,privileges):
# 		super().__init__(privileges)
# 		self.privileges=Privileges()
# Admin = Admin()
# Admin.privileges.show_privileges()














