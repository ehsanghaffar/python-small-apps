n = int(input())

for x in range(1, n):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 2 == 0:
        continue
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)


# ## 15
# 1
# Solo
# Learn
# 7
# Solo
# 11
# 13

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         i = "FizzBuzz"
#     elif i % 3 == 0:
#         i = "Fizz"
#     elif i % 5 == 0:
#         i = "Buzz"
#     print (i)