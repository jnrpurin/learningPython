###################################################################
# Practice 1 set:

newSet = {1, 3, 5, 7}
print(type(newSet))  # <class 'set'>
newSet.add(10)
print(newSet)
newSet.discard(3)  # remove the item with value 3 from the set
print(newSet)

secondSet = {2, 4, 8, 10}
unionSet = newSet.union(secondSet)  # it does not duplicate equal values
print(unionSet)

intersSet = newSet.intersection(secondSet)  # get only values that have on both sets
print(intersSet)

diffSet = newSet.difference(secondSet)
print(diffSet)
diffSet2 = secondSet.difference(newSet)
print(diffSet2)

diffSymmetricSet = newSet.symmetric_difference(secondSet)
print(diffSymmetricSet)

setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
setSubSet = setA.issubset(setB)
print(setSubSet)  # True

setSuperSet = setA.issuperset(setB)
print(setSuperSet)  # False

animalsList = ['dog', 'dog', 'cat', 'elephant', 'elephant']
print(animalsList)

animalsSet = set(animalsList)  # A set does not allow duplicated items
print(animalsSet)
