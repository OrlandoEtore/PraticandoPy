#Sets
#Remove 

set = set()
set1 = {1,1,2,2,3,3,4,4,5,6,8,8,101,102,1000,5555}
# print(type(set))
# print(type(set1))
# print(set)
# print(set1)
# print(len(set))
# print(len(set1))

set.add(1)
set.add(2)

# set2 =set.union({4,5,6})
# print(set,set2)
set.add(3)
set.add(4)
set.add(5)
print(set)
set.remove(4)
print(set)
set.discard(1111)