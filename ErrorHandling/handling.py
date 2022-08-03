# num1=int(input("enter number 1:"))
# num2=int(input("enter number 2:"))
#
# try:
#     res=num1/num2
#     print(f"result:{res}")
# except Exception as e:
#     num2=int(input("enter num2:"))
#     print(res)
#
# finally:
#         print("db transaction")
#         print("file operation")

phn_num=input("enter phn:")

if len(phn_num)!=10:
    raise Exception("invvalid number")
else:
    print("valid")