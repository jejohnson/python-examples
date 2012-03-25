__author__ = 'jamesjohnson'

def merge_sort(list):
    new_list = []
    if len(list) == 1:
        return [list[0]]
    else:
        sliceSize = int(len(list) / 2)
        a_list = merge_sort(list[0:sliceSize])
        b_list = merge_sort(list[sliceSize:])

        aIdx = 0
        bIdx = 0
        i = 0

    while i < len(list):

        if aIdx < len(a_list) and bIdx < len(b_list):

            if a_list[aIdx] > b_list[bIdx]:
                new_list.append(b_list[bIdx])
                bIdx += 1
            else:
                new_list.append(a_list[aIdx])
                aIdx += 1

        elif aIdx < len(a_list):
            new_list.append(a_list[aIdx])
            aIdx += 1

        elif bIdx < len(b_list):
            new_list.append(b_list[bIdx])
            bIdx += 1

        i += 1

    return new_list


array = [200, 12, 8, 4, 2, 68, 199, 20, 34, 10, 11, 200]

print("Unsorted:")

#array.sort()
#
for i in array:
    print i, # Works in Python 2.7
    #print(i, end=" ")

print("")

list = merge_sort(array)

print("Merge Sort:")
for i in list:
    print i, # Works in Python 2.7

print("")
