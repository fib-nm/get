import math
tree = list(map(int, input('enter the tree ').split()))


def ancestor(i):
    if i == 0:
        return

    if (i-1)/2 == (i-1)//2:
        return (i-1)//2
    else:
        return (i - 2) // 2


def distance(a, b):
    b0 = b
    if a == 0:
        dist_b = 0
        while b > 0:
            b = ancestor(b)
            dist_b += 1
        return dist_b - 1

    dist_a = 0
    while a > 0:
        dist_b = 0
        while b > 0:
            if b == a:
                return dist_a + dist_b - 1
            b = ancestor(b)
            dist_b += 1
        b = b0
        a = ancestor(a)
        dist_a += 1

    dist_b = 0
    while b > 0:
        b = ancestor(b)
        dist_b += 1
    return dist_a + dist_b - 1


levels = math.floor(math.log(len(tree), 2))
if levels == 0:
    print(0)
else:
    m = 0
    for j in range(2**(levels-1)-1, len(tree)):
        for h in range(2 ** (levels - 1) - 1, len(tree)):
            if distance(j, h) > m:
                m = distance(j, h)
    print("the tree's diameter equals" + str(m))
