pattern="ABACCD"
char_count={}
#
# for char in pattern:
#     if char in char_count:
#         print(f"first rec character is {char}")
#         break
#     else:
#         char_count[char]=1

rec_char=[]
for char in pattern:
    if char in char_count:
        rec_char.append(char)
    else:
        char_count[char]=1

print(f"Second recc character is {rec_char[1]}")