num=123
# rev=321
res=" "
while(num !=0):
    last_digit=num%10
    res=res+" "+str(last_digit)
    num=num//10
print(f"{res}")

