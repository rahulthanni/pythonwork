mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
print (f"Total number of mobiles= {len(mobiles)}")

# q1 total number of out_of_stock mobiles
ous_mob=[qty for qty in mobiles if qty[6]==0]
print(f"Number of out of stock mobiles are: {len(ous_mob)}")

# q2 total stock
tot_stock=sum([qty[6] for qty in mobiles  if qty[6]>0])
print(f"Number of mobiles in stock are: {tot_stock}")

# q3 pritn mobiles available in range 20k to 30k
range_mobile=[price for price in mobiles if price[4]>=20000 and price[4]<=30000]
print(f"Available mobiles in the range 20k to 30k are:{range_mobile}")

# q4 print all 5g phone
fiveg_mobile=[network for network in mobiles if network[2]=="5g"]
print(f"5g mobiles are:{fiveg_mobile}")

# q5 print samsung mobiles
samsung_mobile=[hset for hset in mobiles if hset[5]=="samsung"]
print(f"samsung mobiles are:{samsung_mobile}")

# q6 print costly mobile
costly_mobile=[price for price in mobiles if price[4]>30000]
print(f"costly mobiles are:{costly_mobile}")


# q7 prin low cost mobiles
lowcost_mobile=[price for price in mobiles if price[4]<20000]
print(f"low cost mobiles are:{lowcost_mobile}")


# q8 print all mobiles having stock >10
stock_mobile=[qty for qty in mobiles if qty[6]>10]
print(f"stock < 10:{stock_mobile}")

# q9 count of mobiles having dispaly amoled
disp_mobile=[disp for disp in mobiles if disp[3]=="AMOLED"]
print(f"count of amoled mobiles:{len(disp_mobile)}")

# q10 sort mobiles based on price oredr by desc
# order_mobile=([price for price in mobiles if price[4]>=0])
# print(f"order of mobiles:{order_mobile}")

# q11 sort mobiles based on avl stock oredr by desc


# q12 is there any mobile available at rs 10000 ?
avail_mobile=[price for price in mobiles if price[4]==10000]
print(f"Mobiles are available at rs 10000 : {avail_mobile is True}")

# q12 list all mobiles having same price
same_price=[price for price in mobiles if price[4]==price[4]]

print(f"Mobiles at same price : {same_price}")
