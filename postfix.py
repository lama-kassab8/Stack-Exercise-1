

def postfix(string):
    stack= []

    operators= ['+', '-', '/', '*', '%']

    for item in string:
        if item.isdigit():
            stack.append(int(item))
        elif item in operators:
            num2= stack.pop()
            num1= stack.pop()

            if item =='+':
                result= num1 + num2
            elif item =='-':
                result= num1 - num2
            elif item== '*':
                result= num1 * num2
            elif item== '/' and num2 != 0:
                result= num1 / num2
            elif item== '%':
                result= num1 % num2

            stack.append(result)

    return stack[0]

print(postfix(["2", "1", "+", "3", "*"]))

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class StackLinkedList:
    def __init__(self):
        self.top=None

    def push(self, data):
        new_node= Node(data)
        new_node.next= self.top
        self.top= new_node

    def pop(self):
        if self.top is None:
            print("The list is empty")
            return
        temp= self.top.data
        self.top= self.top.next
        return temp
    
def postfix(string):
    stack= StackLinkedList()

    operators= ['+', '-', '/', '*', '%']
    for item in string:
        if item.isdigit():
            stack.push(int(item))
        elif item in operators:
            num2= stack.pop()
            num1= stack.pop()

            if item =='+':
                result= num1 + num2
            elif item =='-':
                result= num1 - num2
            elif item== '*':
                result= num1 * num2
            elif item== '/' and num2 != 0:
                result= num1 / num2
            elif item== '%':
                result= num1 % num2

            stack.push(result)

    return stack.pop()
