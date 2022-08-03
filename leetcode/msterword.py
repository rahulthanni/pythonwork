master_word="aabbccaadtdteeggm"
chk_word="game"
mw_dic={}
flag=0

mc_count={}
for char in master_word:
    if char in mw_dic:
        mc_count[char]+=1
    else:
        mc_count[char]=1
for char in chk_word:
    if char in mc_count:
        cur_count=mc_count[char]
        if cur_count>0:
            mc_count[char]-=1
        elif cur_count==0:
            flag=1
            break
    else:
        flag=1
        break
print(True if flag==0 else False)
