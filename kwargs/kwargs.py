# def add(*args):
#     return sum(args)
#
# print(add(10,20,30))
#
# def max_fun(*args):
#     return max(args)
#
# print(max_fun(900,10,50))

def add_nums(**kwargs):
    #print(sum(v for k,v in kwargs.items()))
    print(sum(v for v in kwargs.values()))

add_nums(n1=10,n2=20,n3=40)