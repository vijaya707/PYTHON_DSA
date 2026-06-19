stack=[]
stack.append(5)
stack.append(6)
print(stack) #[5,6]
stack.pop() #
print(stack) #[5]
stack.append(7)
stack.append(4)
print('stack',stack) #[5,7,4]
print(stack[-1]) #4
print(len(stack)==0)

