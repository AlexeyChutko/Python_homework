class Stack:
## Инициализация пустого стека при создании экземпляра класса
    def __init__(self):
        self.stack_list = []

    # магический метод для  определеня длины объекта внутри класса

    def __len__(self):
        return len(self.stack_list)

    def pop(self):

        #Удалаяем элемент стека и возвращаем его

        if len(self):
            return self.stack_list.pop()    # Если стек не пуст, извлекаем и возвращаем верхний элемент
        else:
            raise IndexError('Empty Stack!')

    def push(self, num: int):
        # Добавление нового элемента в верхушку стека
        self.stack_list.append(num)

    @property
    def top_element(self):
        # Получение верхнего элемента стека

        return self.stack_list[-1]
#test
stack = Stack()
stack.push(45)
stack.push(36)
stack.push(11)

print(stack.top_element)
print(len(stack))
stack.pop()
print(len(stack))


class Queue:

# Инициализация пустой очереди при создании экземпляра класса
    def __init__(self):
        self.queue_list = []

    def __len__(self):
        return len(self.queue_list)
# магический метод для  определеня длины объекта внутри класса

    def dequeue(self):

    # Если очередь не пуста, извлекаем и возвращаем первый элемент
        if len(self)>0:
            return self.queue_list.pop()
        else:
            raise IndexError('Empty Queue!')

## Добавление нового элемента в конец очереди
    def enqueue(self, num: int):

        self.queue_list.insert(0, num)


 # Получение первого элемента в очереди
    @property
    def first_element(self):

        return self.queue_list[-1]

# Получение последнего элемента в очереди
    @property
    def last_element(self):

        return self.queue_list[0]

##Test
queue = Queue()
queue.enqueue(6)
queue.enqueue(94)
queue.enqueue(29)
print(queue.first_element)
print(queue.last_element)