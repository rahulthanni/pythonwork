from functools import reduce
lst=[88,2,55,4,6,8,97]

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)

gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)

even_num=list(filter(lambda n:n%2==0,lst))
print(even_num)

max_num=reduce(lambda n1,n2:max(n1,n2), lst)
print(max_num)

