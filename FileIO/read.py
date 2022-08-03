
# f=open("abc.txt")
# for line in f:
#     print(line)
#
# out=[line.rstrip("\n") for line in f]
# print(out)
#
# f=open("abc.txt","w")
# lst=["python","javascript","c++"]
# company_name="luminar"
#
# for lan in lst:
#     lan+="\n"
#     f.write(lan)

# f.write(company_name)
s=open("students.txt")
all_students=[stud.rstrip("\n") for stud in s]

f=open("failed.txt")
failed_students=[stud.rstrip("\n") for stud in f]

p=open("passed.txt","w")
passed_students=set(all_students)-set(failed_students)
print(passed_students)

for st in passed_students:
    p.write(st)
