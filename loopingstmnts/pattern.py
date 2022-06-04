# 1
# 1   2
# 1   2   3
# 1   2   3   4
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="\t")
#     print()


# 1
# 2   2
# 3   3   3
# 4   4   4   4
# for row in range(1,5):
#     for col in range(1,row+1):
#         print("#",end="\t")
#     print()

#
#   #
#   #   #
#   #   #   #

# for row in range(1,5):
#     for col in range(5,row,-1):
#         print("#",end="\t")
#     print()
# for r in range (1,5):
#     for c in range(5,r,-1):
#         print("#",end="\t")
#         print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# for row in range(1,6):
#     for space in range(1,(6-row)):
#         print(end=" ")
#     for col in range(1,(row+1)):
#         print("*",end=" ")
#     print()


#    *
#   * *
#  *   *
# *******
# for row in range(1,5):
#
#     for col in range(1,8):
#         if row==4 or row+col==5 or col-row==3:
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()