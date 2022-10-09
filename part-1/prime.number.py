# Program to check if a number is prime or not

num = 407

#num = int(input("Enter a number: "))

if num > 1:
    # check 
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "isn't prime")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is prime")

# if number is less than, or equal to 1, it is not prime.
else:
    print(num, "isn't prime")
