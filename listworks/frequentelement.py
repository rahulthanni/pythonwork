ls1=[10,11,11,11,12,13,14,14]
count=0
temp=0
index=0

for num in range(0,len(ls1)):
    temp = ls1.count(ls1[num])
    if(temp>count):
        count=temp
        index=num

mostFrequentNo = ls1[index]
print("the most frequent number is:", mostFrequentNo)