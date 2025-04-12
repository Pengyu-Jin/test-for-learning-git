

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

# def decorator1(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator 1: Before function call")
#         result = func(*args, **kwargs)  # 调用原函数
#         print("Decorator 1: After function call")
#         return result
#     return wrapper

# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator 2: Before function call")
#         result = func(*args, **kwargs)  # 调用原函数
#         print("Decorator 2: After function call")
#         return result
#     return wrapper

# @decorator1
# @decorator2
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello = decorator1(decorator2(say_hello))

# prices = {
#     'Acme': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75,
# }

# x = zip(prices.values(), prices.keys())
# print(sorted(x))


# print("当前工作目录：", os.getcwd())



with open("hws/1.txt", "r") as f:
    content = f.read()

print(type(content))
print(len(content))
print(content[:11])