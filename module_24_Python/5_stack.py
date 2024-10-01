"""
Задача 5. Стек
Мы уже говорили, что в программировании нередко необходимо создавать свои собственные структуры
данных на основе уже существующих.
Одной из таких базовых структур является стек.
Стек — это абстрактный тип данных, представляющий собой список элементов,
организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).

Напишите класс, который реализует стек и его возможности
(достаточно будет добавления и удаления элемента).

После этого напишите ещё один класс — «Менеджер задач».
В менеджере задач можно выполнить команду «новая задача»,
в которую передаётся сама задача (str) и её приоритет (int).
Сам менеджер работает на основе стека (не наследование).
При выводе менеджера в консоль все задачи должны быть отсортированы по следующему приоритету:
чем меньше число, тем выше задача.

Вот пример основной программы:
> manager = TaskManager()
> manager.new_task("сделать уборку", 4)
> manager.new_task("помыть посуду", 4)
> manager.new_task("отдохнуть", 1)
> manager.new_task("поесть", 2)
> manager.new_task("сдать ДЗ", 2)
> print(manager)

Результат:
> 1 — отдохнуть
> 2 — поесть; сдать ДЗ
> 4 — сделать уборку; помыть посуду

Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.
"""


class MyStack:

    def __init__(self):
        self.elems = list()

    def __str__(self):
        return '; '.join(self.elems)

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):  # Удаление и получение элемента из начала очереди
        if self.empty:
            return None
        return self.elems.pop()

    @property
    def empty(self):
        return len(self.elems) == 0


class TaskManager:

    def __init__(self):
        self.tasks = dict()
        # self.tasks_seq = MyStack()

    def new_task(self, task: str, priority: int):
        if priority not in self.tasks:
            self.tasks[priority] = MyStack()
        self.tasks[priority].push(task)

    @staticmethod
    def _remove_task(task_to_remove, tasks):
        tmp = MyStack()
        while not tasks.empty:
            task = tasks.pop()
            if task == task_to_remove:
                # deletion
                break
            tmp.push(task)
        while not tmp.empty:
            tasks.push(tmp.pop())

    def del_task(self, task_for_del: str, priority=None):
        if priority is not None:
            self._remove_task(task_for_del, self.tasks[priority])
            return

        for prior, tasks in self.tasks.items():
            self._remove_task(task_for_del, tasks)

    def __str__(self):
        display = list()
        if self.tasks:
            for priority in sorted(self.tasks.keys()):
                display.append(f'{str(priority)} - {self.tasks[priority]}')
        return '\n'.join(display)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)

print()
manager.del_task('поесть')
print(manager)




