# Python Program to Access Index of a List Using for Loop

my_list = [21, 44, 35, 11]

# Using enumerate
for index, val in enumerate(my_list):
    print(index, val)


# Start the indexing with non zero value
for index, val in enumerate(my_list, start=1):
    print(index, val)


# Without using enumerate()
for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)
