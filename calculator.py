#Addition
def add(*args):
    counter = 0
    for each_number in args:
            counter += each_number
    return counter
print(add(1,2))        

#Multiplication
def multiply(*args):
    counter = 1
    for each_number in args:
        counter *= each_number
    return counter
print(multiply(1,2))        
