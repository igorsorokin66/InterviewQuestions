__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem: Taking in two arrays print the similarities but do so in O(n) time. With and without using a hash table
'''

union = {}
def findSimilar(arrayA, arrayB):
    for a in arrayA:
        if a not in union:
            union[a] = 1
    for b in arrayB:
        if b in union:
            print(b)
            del union[b] #this removes the element after the first time it occurs

findSimilar([1,2,2,2,3],[2,3,2,2,2,2,1])