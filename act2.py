set1={2,4,6,8,0}
print("set1 is",set1)

set1.add(12)
print("updated set is ",set1)

set2={1,3,5,7,9}
print("set2 is ",set2)
print(set1.difference(set2))
print(set1.symmetric_difference(set2))