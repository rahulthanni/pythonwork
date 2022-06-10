# list
# expenses=[10,20,18,36,42]
# for amount in expenses:
#     print(amount)
#
# for i in range(0,len(expenses)):
#     print(expenses[i])


# numbers=[12,13,14,15,16,17,18]
# #evan numbers
# for num in numbers:
#     if num%2==0:
#         print(num)

# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num>15:
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     elif num==15:
#         print(num)

#print count of numbers where numbers in range of 14-18

# numbers=[14,15,16,17,18]
# count=0
# for num in numbers:
#     if num>=14 and num<=18:
#         count+=1
#
# print(count)

# numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
# pos=0
# neg=0
# zero=0
# for num in numbers:
#     if num<0:
#         neg+=1
#     elif num>0:
#         pos+=1
#     elif num==0:
#         zero+=1
#
# print("Positive=" f"{pos} ","Negative=" f"{neg}","Zero=" f"{zero}")
# sum=0
# for num in numbers:
#     sum+=num
# print(sum)

numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
sum_pos=0
sum_neg=0
 for num in numbers:
     if num<0:
         sum_pos=sum_pos+num
     elif num>0:
         sum_neg=sum_neg+num


print(f"Sum of positive nos: {sum_pos} , Sum of negative nos: {sum_neg}")
