# def add_numbers(n1,n2):
#     return n1+n2
# print(add_numbers(10,20))

# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# def num_chk(num):
#     return "even" if num%2==0 else "odd"
# print(smart_sub(5,10))
# print(num_chk(12))

# def validate_gmail(email):
#     return email.endswith("@gmail.com")
# print (validate_gmail("rahul@gmail.com"))

# def factorial(num):
#     fact=1
#     for i in range(1,(num+1)):
#         fact=fact*i
#     return fact
# print(factorial(3))

def is_prime(num):
    flag = 0
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break

    return True if flag==0 else False

def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if is_prime(num):
            print(num)

prime_range(10,27)

    