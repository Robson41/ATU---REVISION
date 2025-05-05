# Removes and returns the last element by default
queue = [1, 2, 3]
item = queue.pop()
print(item)   # Output: 3
print(queue)  # Output: [1, 2]

# Removes the first element (like a queue) if you specify index 0
queue = [1, 2, 3]
item = queue.pop(0)
print(item)   # Output: 1
print(queue)  # Output: [2, 3]
