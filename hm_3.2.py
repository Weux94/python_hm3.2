# # Один елемент

my_list = [1]
if my_list:
    num = my_list.pop()
    my_list.insert(0, num)

print(my_list)
# # декілька елементів

my_list = [1, 3, 4, 5, 6]
if my_list:
    num = my_list.pop()
    my_list.insert(0, num)

print(my_list)
# # нема елементів

my_list = []
if my_list:
    num = my_list.pop()
    my_list.insert(0, num)

print(my_list)
