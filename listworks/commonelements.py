arr1=[10,13,14,12,15,16]
arr2=[14,10,16,18,8,7]

arr1.sort()
arr2.sort()
count=0
p1=0
p2=0

while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(f"Common elements is {arr1[p1]}")
        p1+=1
        p2+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
    count+=1
print(count)