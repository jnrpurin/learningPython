###################################################################
# Practice 2 tuple:

listNumbers = [1, 3, 5, 7]
listStr = ['dog', 'cat', 'rat']

# tuple == immutable
newTuple = (1, 10, 100)
print(newTuple)
print(len(newTuple))  # 3

# convert list to tuple
tupleNumbers = tuple(listNumbers)
print(tupleNumbers)

# convert tuple to list
newList = list(newTuple)
print(newList)

###################################################################
# Practice 1 list:

# listNumbers = [1, 3, 5, 7]
# listStr = ['dog', 'cat', 'rat']
# newListStr = listStr * 3  # create 3 lists like the listStr
# print(newListStr)
#
# listMixed = ['One', 2, 3, 'four']  # not good
# print(listMixed)
# print(listStr[2])
#
# for i in listStr:
#     print(i)
#
# print(sum(listNumbers))
# print(max(listNumbers))
# print(max(listStr))
# print(min(listNumbers))
# print(min(listStr))
#
# if 'dog' in listStr:
#     print('There is a dog')
# else:
#     print('dog is not there')
#
# listStr[1] = 'another animal'
#
# # add a item on the list
# listStr.append('elephant')
#
# # remove the last item
# listStr.pop()
#
# # remove pos 0 from the list
# listStr.pop(0)
#
# # remove element I know from the list
# listStr.remove('dog')
#
# # to order lists
# listStr.sort()
# listNumbers.reverse()

###################################################################
