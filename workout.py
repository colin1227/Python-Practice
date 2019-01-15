hello_world = "hello"
hello_world = "hello world"
var_one = 1
var_two = 2
List = [3, 4, 5, 6, 7]
Tuple = (8, 9)
seventy2 = Tuple[0] * Tuple[1]
empty = []


for i in range(10):
    empty.append(i)


def whats_here(value):
    if(str(type(value)) == "<class 'str'>"):
        print("value is a string")

    elif(str(type(value)) == "<class 'list'>"):
        print("value is a list")

    elif(str(type(value)) == "<class 'tuple'>"):
        print("value is a tuple")

    elif(str(type(value)) == "<class 'int'>"):
        print("value is a number")

    elif(str(type(value)) == "<class 'dict'>"):
        print("value is a dictionary")

    elif(str(type(value)) == "<class 'function'>"):
        print("value is a function")

    elif(str(type(value)) == "<class '__main__.Person'>"):
        print("value is a class named Person")
    
    elif(str(type(value)) == "<class 'type'>"):
        print("value is a class")
    
    else:
        print("something has gone teribly wrong")
        print(type(value))

