num=4

i=1
pattern=""
sum=0
while(i<=num):
    pattern=pattern+str(num)
    sum=sum+int(pattern)
    #print(pattern)
    i+=1
print(sum)