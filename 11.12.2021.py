# Задание 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

# def card_hide(card):
#     return '*' * (len(card)-4) + card[-4:]
# print(card_hide("4916984512364578"))

# Задание 2. Напишите функцию, которая проверяет: является ли слово палиндромом

# def reverse(a):
#     return a[::-1]
#
# def is_palindrome(a):
#     rev = reverse(a)
#     if (a == rev):
#         return True
#
#     return False
#
# a = "dovod"
# an = is_palindrome(a)

# Задание 3. Решите задачу:
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.

# class Tomato:
#     states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#     def grow(self):
#         self._change_state()
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         self._print_state()
#
#     def _print_state(self):
#         print(f'Tomato {self._index} is {Tomato.states[self._state]}')
#
# class TomatoBush:
#
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     def give_away_all(self):
#         self.tomatoes = []
#
# class Gardener:
#
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         print('Gardener is working...')
#         self._plant.grow_all()
#         print('Gardener finished')
#
#     def harvest(self):
#         print('Gardener is harvesting...')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Harvesting is finished')
#         else:
#             print('Too early! Your plant is green and not ripe.')
#
#     @staticmethod
#     def knowledge_base():
#         print('''Harvest time for tomatoes should ideally occur
# when the fruit is a mature green and
# then allowed to ripen off the vine.
# This prevents splitting or bruising
# and allows for a measure of control over the ripening process.''')
#
# if __name__ == '__main__':
#     Gardener.knowledge_base()
#     great_tomato_bush = TomatoBush(4)
#     gardener = Gardener('Emilio', great_tomato_bush)
#     gardener.work()
#     gardener.work()
#     gardener.harvest()
#     gardener.work()
#     gardener.harvest()
#


