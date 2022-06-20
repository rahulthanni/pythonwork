word_count={"a":2,"b":5,"c":3,"d":2,"e":1}
w_list=word_count.items()
print(sorted(w_list,key=lambda item:item[1],reverse=True))

#max()
print(max(w_list,key=lambda item:item[1]))
print(min(w_list,key=lambda item:item[1]))