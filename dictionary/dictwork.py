laptop={"Brand":"Microsoft","Series":"Pavilion","Screen Size":"15.6","Color":"Silver","Hard Disk":"512gb","RAM":"8gb"}
# print(laptop["Brand"])
# print(laptop["Color"])
# print(laptop["RAM"])

# print("CPU Model" in laptop)
# laptop["CPU Model"]="Core i5"
# print(laptop)
#
# print(laptop["Brand"])
# laptop["Brand"]="HP"
# print(laptop)


# print(laptop.get("serie"))
# print(laptop.get("Brand"))

if "Price" in laptop:
    laptop["Price"]=50000
else:
    laptop["Price"]=85000

print(laptop)

if laptop["Price"]>70000:
    laptop["Price"]-=1000
else:
    laptop["Price"]-=500
print(laptop)