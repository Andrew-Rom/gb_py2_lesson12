"""
📌Создайте класс-генератор.
📌Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
📌Если переданы два параметра, считаем step=1.
📌Если передан один параметр, также считаем start=1.
"""


# class Factorial:
#     def __init__(self, *args):
#         self.start, self.stop, self.step = 1, 1, 1
#         if args:
#             args = list(map(int, args))
#             match len(args):
#                 case 1:
#                     self.stop = args[0]
#                 case 2:
#                     self.start, self.stop = args
#                 case 3:
#                     self.start, self.stop, self.step = args
#         self._value = self._fact()
#
#     def _fact(self):
#         result = []
#         number = 1
#         for i in range(self.start, self.stop, self.step):
#             number *= i
#             result.append(number)
#         return result
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self._value:
#             return self._value.pop(0)
#         raise StopIteration
#
#
# a = Factorial(2,20,2)
#
# for i in a:
#     print(i)


class Factorial:
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.num <= self.stop:
            self.num = self.num * self.start
            self.start += self.step
            return self.num
        raise StopIteration


a = Factorial(stop=1000)
print('1 - ', a.__next__())
print('2 - ', a.__next__())
print('3 - ', a.__next__())
print('4 - ', a.__next__())
print('5 - ', a.__next__())
print('6 - ', a.__next__())
print('7 - ', a.__next__())
print('8 - ', a.__next__())
