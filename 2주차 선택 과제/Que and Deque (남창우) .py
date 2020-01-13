class Que:
    def __init__(self):
        self.__arr = []

    def push(self, item):
        self.__arr.append(item)

    def isEmpty(self):
        if self.__arr:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return False
        else:
            item = self.__arr[0]
            del (self.__arr[0])

            return item

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.__arr[0]


class Deque:
    def __init__(self):
        self.__arr = []

    def push(self, item):
        self.__arr.append(item)

    def isEmpty(self):
        if self.__arr == []:
            return True
        else:
            return False

    def pop_rear(self):
        if self.isEmpty():
            return False
        else:
            item = self.__arr[-1]
            del (self.__arr[-1])

            return item

    def pop_front(self):
        if self.isEmpty():
            return False
        else:
            item = self.__arr[0]
            del (self.__arr[0])

            return item

    def peek_rear(self):
        if self.isEmpty():
            return False
        else:
            return self.__arr[-1]

    def peek_front(self):
        if self.isEmpty():
            return False
        else:
            return self.__arr[0]


