# Один елемент

my_list = [1]
result = []
if my_list:
    result.append(my_list.pop())
    result.extend(my_list)

print(result)

# декілька елементів

my_list = [1, 2, 3]
result = []
if my_list:
    result.append(my_list.pop())
    result.extend(my_list)

print(result)

# нема елементів

my_list = []
result = []
if my_list:
    result.append(my_list.pop())
    result.extend(my_list)

print(result)
