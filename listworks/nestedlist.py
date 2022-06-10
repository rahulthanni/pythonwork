lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16],
    [45,70]
]
#print all numbers greater than 16
# for sub_ls in lst:
#     for num in sub_ls:
#         if num>16:
#             print(num)

#print max number in list
# flatten_ls=[]
# for sub_ls in lst:
#     for num in sub_ls:
#         flatten_ls.append(num)
#
# print(max(flatten_ls))

#List Comprehension
flatten_lst=[num for sub_ls in lst for num in sub_ls]
print(flatten_lst)
#
# num_grt_six=[num for num in flatten_lst if num>16]
# print(num_grt_six)
#
# odd_num=[num for num in flatten_lst if num%2!=0]
# print(odd_num)

#num>25 num+1 else num-1
new_lst=[num+1 if num>25 else num-1 for num in flatten_lst]
print(new_lst)

# even_sum=sum([num for num in flatten_lst if num%2==0])
# print(even_sum)
