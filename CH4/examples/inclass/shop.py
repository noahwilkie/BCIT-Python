shopList = open("shopping.txt")

shopArray = []

for item in shopList:
    shopArray.append(item)
shopList.close()

shopArray.sort()

for shopSort in shopArray:
    print(shopSort.strip())
