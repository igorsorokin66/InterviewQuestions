__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'

arr = []
for t in range(5):
    arr.append(input())

dict = {}
stor = {}
for a in arr:
    if a[0] in dict:
        if a[1] in dict:
            dict[a[0]] += a[1]
        else:
            dict[a[0]] += {a[1]}
        if a[2] in dict:
            dict[a[0]] += a[2]
        else:
            dict[a[0]] += {a[2]}
    else:
        if a[1] in dict:
            dict[a[0]] = dict[a[1]]
        else:
            stor[a[1]] = {}#done
            dict[a[0]] = stor[a[1]]
            dict[a[0]][a[1]] = stor[a[1]]
        if a[2] in dict:
            dict[a[0]] = dict[a[2]]
        else:
            stor[a[2]] = {}#done
            dict[a[0]][a[2]] = stor[a[2]]
    if a[1] in dict:
        if a[2] in dict:
            dict[a[1]] += dict[a[2]]
        else:
            dict[a[1]] += {a[2]}
    else:
        if a[2] in dict:
            dict[a[1]] = dict[a[2]]
        else:
            dict[a[1]] = [a[2]]

final = {}
for d in dict:
    l = list(set(dict[d]))
    if len(l) == 1:
        final[0] = dict[d][0]
    final[len(l)] = d
    print(str(d) + " " + str(l))
print("".join(list(reversed(list(final.values())))))
#print(dict)
'''
SMH
TON
RNG
WRO
THG
'''
#S -> MH
#T -> ON
#R -> NG
#W -> RO
#T -> HG
#M -> H
#O -> N
#N -> G
#R -> O
#H -> G

#S M H G