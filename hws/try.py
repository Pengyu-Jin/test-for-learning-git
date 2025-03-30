

# ls = [11, 23, 34, 3, 2, 6, 7, 8, 9, 10]
# print(sorted(ls, reverse=True))

# ls2 = [1, 2, 3]

# print(sorted(ls + ls2))

# y = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# y = dict()
# x ={3: 'd', 2: 'b', 1: 'c', 3: 'a'}
# print(x)
# print(type(x))
# y[3] = 'xs'
# print(y)
# print(type(y))
# s = "hello"
# print(s[1:4])

# s = "helloworld"
# res = ["" for i in range(len(s))]
# print(res)

# x = 7768
# print(str(x))
# s = reversed(str(x))
# print(type(s))
# print(int("".join(s)))

def my_decorator(func):
    def wrappper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrappper

@my_decorator
def say_hello():
    print("Hello")

# say_hello = my_decorator(say_hello)

# call function
say_hello()

# syntactic sugar