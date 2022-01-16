class MyStack():
    def __init__(self, input_data=None):
        if input_data is not None:
            self.stack_data = [item for item in input_data]
        else:
            self.stack_data = list()

    def isEmpty(self):
        return True if not self.stack_data else False

    def push(self, add_element=None):
        if add_element is not None:
            if self.isEmpty():
                self.stack_data = list()
                self.stack_data.append(add_element)
            else:
                self.stack_data.append(add_element)

    def pop(self):
        if len(self.stack_data) > 0:
            return self.stack_data.pop(-1)
        else:
            return None

    def peek(self):
        return self.stack_data[-1] if self.isEmpty() is False else False

    def size(self):
        return len(self.stack_data) if self.isEmpty() is False else False



def checkBalance(input_value: str):
    brackeds_list = {
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{'
    }
    list_data = MyStack(input_value)
    result = MyStack()

    # собираем закрывающие скобки
    for breaket in list_data.stack_data:
        if brackeds_list.get(breaket) is not None:
            if brackeds_list.get(breaket) in list_data.stack_data:
                close_braket = list_data.stack_data.index(brackeds_list.get(breaket))
                result.push(list_data.stack_data.pop(close_braket))

    if list_data.size() != result.size():
        result.stack_data = []
    else:
        for i in range(result.size()):
            if brackeds_list.get(result.stack_data[i]) != list_data.stack_data[i]:
                result.stack_data = []
                break

    if result.size():
        print('Сбалансированно')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    checkBalance('(((([{}]))))')
    checkBalance('[([])((([[[]]])))]{()}')
    checkBalance('{{[()]}}')

    checkBalance('}{}')
    checkBalance('{{[(])]}}')
    checkBalance('[[{())}]')




