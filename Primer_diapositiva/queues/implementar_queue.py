
#Implementa un queue usando stacks.

stackQueue = []

stackQueue.append(1)
stackQueue.append(2)
stackQueue.append(3)
stackQueue.append(4)
stackQueue.append(5)

print(stackQueue)
print("\n\n")

#Funcion para eliminar el primer elemento como una Queue

def shiftStack(stack):
    stack2 = []
    for i in range(len(stack)):
        stack2.append(stack.pop())
    stack2.pop()
    
    for i in range(len(stack2)):
        stack.append(stack2.pop())
    
shiftStack(stackQueue)
shiftStack(stackQueue)
shiftStack(stackQueue)

print(stackQueue)
        