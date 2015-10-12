#you are given a list of integers from 1 to 100. two are randomly deleted.
#identify which have been deleted without using a data structure
import random
arr = [i for i in range(1, 11)]
random.shuffle(arr)
print(arr)

s1 = sum(arr)
print("Sum:\t\t" + str(s1))
m1 = 1
for i in arr:
    m1 *= i
print("Product:\t" + str(m1))

print()
print("Deleting:\t" + str(arr[0]))
del arr[0]
print("Deleting:\t" + str(arr[0]))
del arr[0]
print()

print(arr)
s2 = sum(arr)
print("Sum:\t\t" + str(s2))
m2 = 1
for i in arr:
    m2 *= i
print("Product:\t" + str(m2))

s = s1 - s2
m = m1 // m2
print("Diff Sum:\t" + str(s))
print("Diff Prod:\t" + str(m))
for i in range(1, s):
    if i * (s - i) == m:
        print("Answer:\t\t" + str(s - i))
        print("Answer:\t\t" + str(i))
        break