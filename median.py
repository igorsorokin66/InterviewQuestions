__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem: 
Numbers are randomly generated and stored into an (expanding) array 
How would you keep track of the median?
Source:
Cracking the Code Interview 4ed Page 36
'''
import random
raw = []
dict = {}
target = 0
for i in range(0, 10):
    n = random.randrange(1, 10)
    raw.append(n)
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
    target += 1
print(sorted(raw))
f = -1
prev = 0
for i in range(1, 10):
    if i in dict:
        for k in range(0, dict[i]):
            f += 1
            if f == target//2:
                if target % 2 != 0 or k-1 != -1:
                    print("Your answer: " + str(i))
                    print("Correct answer: " + str(sorted(raw)[len(raw)//2]))
                else:
                    print("Your answer: " + str((prev+i)/2))
                    print("Correct answer: " + str(((sorted(raw)[len(raw)//2-1]+sorted(raw)[len(raw)//2])/float(2))))
                break
            prev = i