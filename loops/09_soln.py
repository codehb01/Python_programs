myList = ["Apple","Banana","Mango","JackFruit","Apple"]
unique_item = set()

for item in myList:
    if item in unique_item:
        print("Duplicate ",item)
        break
    unique_item.add(item)