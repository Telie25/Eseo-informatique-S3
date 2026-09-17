import copy 
a = ['A'] 
b = copy.copy(a)  
b[0] = 1 
print(a) 
print(b)
