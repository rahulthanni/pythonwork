# lst=[10,10,1,12,13,14,16,15,16,16,16]
# st=set(lst)
# print(st)
# print(dir(set))
#
# st1={1,2,3,4,5}
# st2={10,11,12,2,3}
# #st.add(10)
# union_set=st1.union(st2)
# print(union_set)
#
# intersection_set=st1.intersection(st2)
# print(intersection_set)
#
# difference_set=st1.difference(st2)

students=["ram","ravi","hari","tom","nikhil","jain","john"]
passed_students=["ravi","hari","tom"]

failed_students=set(students).difference(set(passed_students))
print(failed_students)