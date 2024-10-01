"""
Задача 4. Односвязный список
Мы продолжаем тему структур данных и алгоритмов.
И в этот раз вам нужно реализовать односвязный список.
Связный список — это структура данных, которая состоит из элементов, называющихся узлами.
В узлах хранятся данные, а между собой узлы соединены связями.
Связь — это ссылка на следующий или предыдущий элемент списка.

В односвязном списке связь — это ссылка только на следующий элемент,
то есть в нём можно передвигаться только в сторону конца списка.
Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования
стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей.

Для реализации напишите два класса: Node и LinkedList.
В Node должна быть логика работы одного узла (хранение данных и указателя).

Для структуры реализуйте следующие методы:
append — добавление элемента в конец списка;
get — получение элемента по индексу;
remove — удаление элемента по индексу.
Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

Пример основной программы:
> my_list = LinkedList()
> my_list.append(10)
> my_list.append(20)
> my_list.append(30)
> print('Текущий список:', my_list)
> print('Получение третьего элемента:', my_list.get(2))
> print('Удаление второго элемента.')
> my_list.remove(1)
> print('Новый список:', my_list)

Результат:
> Текущий список: [10 20 30]
> Получение третьего элемента: 30
> Удаление второго элемента.
> Новый список: [10 30]
"""

from typing import Any, Optional


class Node:
    """
    class Node - describe a node
    Attributes:
    data - value: Any
    next - Link to the following node: Optional[Node]
    """

    def __init__(self, data: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.data = data    # Node value
        self.next = next    # Link to next node

    def __str__(self) -> str:
        return f'Node [{self.data}]'


class LinkedList:
    """
    class LinkedList - singly linked list
    head - First node pointer
    lenght - length counter
    """

    head: Optional[Node]

    def __init__(self) -> None:
        self.head = None
        self.length = 0
        self.current = self.head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        tmp = self.current
        self.current = self.current.next
        return tmp

    def __str__(self) -> str:

        if self.head is not None:
            current = self.head
            values = [str(current.data)]
            while current.next is not None:
                current = current.next
                values.append(str(current.data))
            return f'[{" ".join(values)}]'
        return 'LinkedList []'

    def append(self, elem: Any) -> None:
        """
        Method to add elem to the end of the list
        """
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        """
        Method to remove an elem by index
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        prev.next = cur_node.next
        self.length -= 1

    def get(self, index):
        """
        Method to get an elem by index
        """
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Current list:', my_list)
print('Get the third elem:', my_list.get(2))
print('Remove the second elem')
my_list.remove(1)


print('New list:', my_list)

print('\nCycle')
for num in my_list:
    print(num)
