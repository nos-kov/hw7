from queue import LifoQueue


class Mystack:

    def __init__(self, size):
        self.size = size

    def newstack(self):
        stack = LifoQueue(maxsize=self.size)
        return stack

    def push(stack, item):
        if (stack.full()):
            print('Stack is full')
        else:
            stack.put(item)

    def pop(stack):

        if (stack.empty()):
            print('Stack is empty')
        else:
            stack.get()

    def is_empty(stack):
        return stack.empty()
            
    def peek(stack):
        item = stack.get()
        stack.put(item)
        return item
    
    def size(stack):
        return stack.qsize()


if __name__ == '__main__':

    thestack = Mystack(10)
    thestack = Mystack.newstack(thestack)
    Mystack.push(thestack, 1)
    Mystack.push(thestack, 2)
    print(Mystack.peek(thestack))
    print(Mystack.size(thestack))
    print(Mystack.is_empty(thestack))
    Mystack.pop(thestack)
    print(Mystack.size(thestack))