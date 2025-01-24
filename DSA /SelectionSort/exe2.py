l = [5,2,3,4,1]
target = 10
# output = [3,4]
def twonumsum(l, target):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i]  +  l[j] == target:
                return [i,j]
    return [-1,-1]
a = twonumsum(l, target)
print(a)