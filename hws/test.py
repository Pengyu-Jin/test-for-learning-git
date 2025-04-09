import heapq

x = [2, 3, 23, 5, 64, 6, 778, 8785, 4, 3, 0 -53, -3]
print(x)

heapq.heapify(x)

print(x)

print(heapq.heappop(x))
print(heapq.heappop(x))
print(heapq.heappop(x))
print(heapq.heappop(x))
print(heapq.heappop(x))

print(x)