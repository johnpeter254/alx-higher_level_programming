def islower(c):
    return ord('a') <= ord(c) <= ord('z')


print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('9'))  # False

