import random
import time

# Essence of binary search:
# If you have a sorted list and you want to search this array for something,
# You could go through each item in the list and ask, is this equal to what we're looking for?
# But we can make this *faster* by leveraging the fact that our array is sorted!
# Binary search ~ O(log(n)), naive search ~ O(n)

# In these two examples, l is a list in ascending order, and target is something that we're looking for
# Return -1 if not found

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1

'''
def naive_search(l, target):
    #l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
'''

def binary_search(l, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        print("Não ")
        return -1

    midpoint = (low + high) // 2 

    print("Target: " + str(target) + " Midpoint Index: " + str(midpoint) + " Midpoint Value: " + str(l[midpoint]))
    
    if l[midpoint] == target:
        print("Index: " + str(midpoint) + " Value: " + str(l[midpoint]))
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
    
#l = [1,3,5,8,10,13,14]
#random_Num = random.choice(l)
#print(binary_search(l, 10))

if __name__=='__main__':

    '''length = 10

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    sorted_list = [1,3,5,7,9,10,12,14,16,17]

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")
'''
    sorted_list = [1,3,5,7,9,10,12,14,16,17]

    start = time.time()
    for target in range(len(sorted_list)):
        #print("Target: " + str(target))
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")

    #Criar exceção para números fora da lista que passam pelo target