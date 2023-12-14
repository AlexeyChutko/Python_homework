class Element:
    #Элемент связанного списка.Хранит информацию о значении и следующем (связанном) элементе 


    # Инициализация элемента связанного списка
    def __init__(self, value: int):
        self.value = value
        self.next_element = None


class LinkedList:
# Инициализация пустого связанного списка
    def __init__(self):
        self.first_element = None

    def is_empty(self):

        return not self.first_element  # если First element == None, значит в нем нет элементов

    def __len__(self):
        # возвращает длину связанного списка
        current_element = self.first_element
        length = 0
        while current_element:
            length += 1
            current_element = current_element.next_element
        return length


    def contains(self, num):

        # Выполняет поиск элемента со значением  num в связанном списке и возвращает, был ли элемент найден
        current_element = self.first_element

        while current_element:
            if current_element.value == num:
                return True  # элемент найден !
            current_element = current_element.next_element  # продоление поиска
        return False

    def add_element(self, num):

        #Добавляет элемент со значением num в начало связанного списка

        element_to_add = Element(num)
        element_to_add.next_element = self.first_element
        self.first_element = element_to_add

    def remove_element(self, num):

        #Удаляет элемент со значением num из связанного списка

        current_element = self.first_element
        previous_element = None

       # если выполнять удаление до конца списка, т.е. (current_element == None), то такого элемента в списке нет
        while current_element:
            if current_element.value == num:  # если найдено значение
                if not previous_element:  # если найденный элемент является первым элементом
                    self.first_element = current_element.next_element  # делает элемент первым
                    return
                else:  # соединяет предыдущий и следующий элементы
                    previous_element.next_element = current_element.next_element
                    current_element.next_element = None
                    return
            # next iteration
            previous_element = current_element
            current_element = current_element.next_element

        print(f'There is no {num} in list')  # Если цикл завершился без возврата, то выводится сообщение о том, что такого элемента в списке нет

#test
llist = LinkedList()
llist.add_element(9)
llist.add_element(5)
llist.add_element(11)

print(llist.contains(5))

llist.remove_element(11)
llist.add_element(0)
llist.add_element(1)

print(llist.contains(10000))

print(len(llist))