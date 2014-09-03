__author__ = 'Christie'
# Write a function in any language that takes as input a list of lists of integers.
# The function should return void, and print to standard output the number of times each integer appeared at each index 
# in an inner list. So for instance:
#   countem ([ [ 1,2,3], [1,3,4], [1,3] ]) would output:
#   1 @ 0 -> 3
#   2 @ 1 -> 1
#   3 @ 2 -> 1
#   3 @ 1 -> 2
#   4 @ 2 -> 1
#Ordering of the output does not matter.

def countem(listOfListOfIntegers):
    listofLists = [[] for x in range(listOfListOfIntegers.__len__())]
    for l in listOfListOfIntegers:
        for i, v in enumerate(l):
            #print (i, v)
            listofLists[i].append(v)
    #print(listofLists)

    for i, v in enumerate(listofLists):
        a = set(v)
        [print (j, "@", i, "->", v.count(j)) for j in a]


countem([ [ 1,2,3], [1,3,4], [1,3] ])
