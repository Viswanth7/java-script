sear_ele =int(input("enter the search elemet:"))
list1=[12,17,18,45,42]

for i in list1:
    if i == sear_ele:
        print("emement found at:", list1.index(i))
        break
else:   
    print("element not found")