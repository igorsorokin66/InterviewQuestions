__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''
'''
realData = [4:"jpg", 6:"jpg"]
inputData = [4,6,3,7,6,5,4]

#cache 4 6 3 7

# 3:(7)
# end (6)
#stack (4) (3) (7) (6)

#table 4:0 6:1 3:2 7:3
'''
class Node:
    def __init__(self, prev, next, key, value):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value

def addToEnd(lookup, tail, page, value):
    lookup[page] = Node(tail, None, page, value)
    tail.next = lookup[page]
    return lookup[page]

def printCache(head):
    current = head
    print("Cache\t" ,end="")
    for i in range(4):
        print(current.key, end="")
        if current.next != None:
            current = current.next
        else:
            break
    print("\n")

def insert(page, value, lookup):
    global head
    global tail
    if len(lookup.keys()) < 4:  # the value 4 represents the cache size
        if len(lookup.keys()) == 0:
            lookup[page] = Node(None, None, page, value)
            head = lookup[page]
            tail = lookup[page]
        else:
            tail = addToEnd(lookup, tail, page, value)
    else:
        if page in lookup:   # hit
            if tail.key != page:
                current = lookup[page]
                if head.key != page:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    head = current.next
                tail.next = current
                current.prev = tail
                current.next = None
                tail = current
        else:               # miss
            print("Remove\t" + str(head.key))
            lookup.pop(head.key)
            current = head.next
            current.prev = None
            head = current
            tail = addToEnd(lookup, tail, page, value)
    print("Add:\t", end="")
    print(page)
    printCache(head)

def value_from_cache(key, lookup):
    if key not in lookup:
        print("Key not in cache")
    else:
        print("Value in cache: ", end="")
        print(lookup[key].value)

lookup = {}
insert(4, "4.jpg", lookup)
insert(6, "6.jpg", lookup)
insert(3, "3.jpg", lookup)
insert(7, "7.jpg", lookup)
insert(6, "6.jpg", lookup)
insert(5, "5.jpg", lookup)
insert(4, "4.jpg", lookup)
insert(4, "4.jpg", lookup)
insert(7, "7.jpg", lookup)
insert(0, "0.jpg", lookup)
insert(2, "2.jpg", lookup)
value_from_cache(7, lookup)