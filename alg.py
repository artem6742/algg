# class Student:
#
#     def __init__(self, name, age, scores):
#         self.name = name
#         self.age = age
#         self.scores = scores
#
#     def info(self):
#         print('Имя', self.name)
#         print('возраст', self.age)
#         print('оценки', self.scores)
#
#     def avarage_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# student2 = Student('вамы ыамыимыкимы', 12, '58', [5, 4, 4, 5])
# student2.info()
#
# print('Cредний балл >>>', student2.avarage_score())





# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.wingth = width
#
#     def info(self):
#         print('длина > ', self.length)
#         print('ширина > ', self.wingth)
#
#     def Calculation(self):
#         return self.length * self.wingth
#
# s = Rectangle(8, 4)
# s.info()
# print('площадь >>>', s.Calculation())

# class Car:
#      def __init__(self, mark, model, year, runned):
#          self.mark = mark
#          self.model = model
#          self.year = year
#          self.runned = runned
#
#      def mark(self, mark):
#          self.mark = mark
#
#      def model(self, model):
#          self.model = model
#
#      def year(self, year):
#          self.year = year
#
#      def runned(self, runned):
#          self.runned = runned
#
#      def info(self):
#          return f'''Марка: {self.mark}
# Модель: {self.model}
# Год выпуска: {self.year}
# Пробег: {self.runned} км'''
#
#
# car = Car('mersedes', '1', '2020', 123456)
# print(car.info())



# class BankAccount:
#     def __init__(self, balance, interest_rate, name, surname):
#         self.name = name
#         self.surname = surname
#         self.balance = balance
#         self.interest_rate = interest_rate
#         self.transactions = []
#
#     def klient(self):
#         print(f'Имя и фимилия: {self.name} {self.surname}')
#
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Внесение наличных на счет: {amount}")
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.transactions.append(f'Снятие наличных: {amount}')
#         else:
#             print("Недостаточно средств на счете")
#
#     def add_interest(self):
#         sum_balance_interest = self.balance * self.interest_rate
#         self.balance += sum_balance_interest
#         self.transactions.append(f'Начислены проценты по вкладу {sum_balance_interest}')
#
#     def history(self):
#         for transaction in self.transactions:
#             print(transaction)
#
#
# account = BankAccount(100000, 0.05, 'Игорь', 'Васильевич')
# account.klient()
# account.deposit(15000)
# account.withdraw(7500)
# account.add_interest()
# account.history()



# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def answer(self):
#         if self.a == self.b == self.c:
#             return 'Треугольник равносторонний'
#         elif ((self.a == self.b) and (self.a != self.c and self.b != self.c)) or ((self.a == self.c) and (self.a != self.b and self.b != self.c)) or ((self.c == self.b) and (self.a != self.c and self.b != self.a)):
#             return 'Треугольник равнобедренный'
#         elif self.a == 0 or self.b == 0 or self.c == 0:
#             return 'Такого треугольника не существует'
#         else:
#             return 'Треугольник разносторонний'
#
# tring = Triangle(3,4,5)
# print(tring.answer())












