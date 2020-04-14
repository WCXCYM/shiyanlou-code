__author__ = 'FSZB'

'''
class Stack:
    def __init__(self):
        self.stacks = []

    def push(self,stack):
        self.stacks.append(stack)

    def pop(self):
        return self.stacks.pop()

    def clear(self):
        del self.stacks[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stacks)

    def top(self):
        return self.stacks[self.size()-1]

#十进制转二进制  堆栈典型用例
def divideBy2(num):
    restack = Stack()

    while num > 0:
        rem = num % 2
        restack.push(rem)
        num = num // 2

    binString = ''
    while not restack.empty():
        binString = binString + str(restack.pop())

    return binString

if __name__ == '__main__':
    print(divideBy2(42))
'''

class Stack(object):
    def __init__(self, limit=10):
        self.stack = []  # 存放元素
        self.limit = limit  # 栈容量极限

    def push(self, data):
        # 判断栈是否溢出
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            # 空栈不能被弹出元素
            raise IndexError('pop from an empty stack')

    def peek(self):
        # 查看栈的栈顶元素（最上面的元素）
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        # 查看堆栈的最上面的元素
        return not bool(self.stack)

    def size(self):
        # 返回栈的大小
        return len(self.stack)

def balanced_parentheses(kuohaos):
    stack = Stack(len(kuohaos))

    for kuohao in kuohaos:
        if kuohao == '(':
            stack.push(kuohao)
        elif kuohao == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))']
    print('Balanced parenthess demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
