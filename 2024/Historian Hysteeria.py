# Import the values from the files and create two lists
from os import path
pyFilePath = path.abspath(__file__)
directoryPath = path.dirname(pyFilePath)
list1FilePath = path.join(directoryPath, "testList1.txt")
list2FilePath = path.join(directoryPath, "testList2.txt")

with open(list1FilePath, 'r', encoding= "UTF-8") as file:
    list1 = list(file)
    list1 = [x.rstrip() for x in list1]


# Sort the list
print(list1)
list1 = list(map(int,list1))
sortedList1 = sorted(list1)
print(sortedList1)

#find the lowest value while also removing it from the list
