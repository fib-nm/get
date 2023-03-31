import matplotlib.pyplot as plt
import math
n = int(input('enter number of iterations '))


def x_transformation(x, y):
    p1 = [x[0], y[0]]
    p2 = [x[1], y[1]]
    p3 = [(2*x[0]+x[1])/3, (2*y[0]+y[1])/3]
    p4 = [(2 * x[1] + x[0]) / 3, (2 * y[1] + y[0]) / 3]
    m = [(x[0]+x[1])/2, (y[0]+y[1])/2]
    length = ((x[1]-x[0])**2 + (y[1]-y[0])**2)**0.5
    if y[1]-y[0] >= 0 and x[1]-x[0] >= 0:
        angle = math.asin((y[1]-y[0])/length)
    elif y[1]-y[0] >= 0 > x[1]-x[0]:
        angle = math.pi - math.asin((y[1]-y[0])/length)
    elif y[1]-y[0] < 0 and x[1]-x[0] < 0:
        angle = math.pi - math.asin((y[1]-y[0])/length)
    else:
        angle = 2*math.pi + math.asin((y[1]-y[0])/length)
    p5 = [m[0] + (length/(12**0.5))*math.cos(angle+math.pi/2), m[1] + (length/(12**0.5))*math.sin(angle+math.pi/2)]
    x_ = [p1[0], p3[0], p5[0], p4[0]]
    return x_


def y_transformation(x, y):
    p1 = [x[0], y[0]]
    p2 = [x[1], y[1]]
    p3 = [(2*x[0]+x[1])/3, (2*y[0]+y[1])/3]
    p4 = [(2 * x[1] + x[0]) / 3, (2 * y[1] + y[0]) / 3]
    m = [(x[0]+x[1])/2, (y[0]+y[1])/2]
    length = ((x[1]-x[0])**2 + (y[1]-y[0])**2)**0.5
    if y[1]-y[0] >= 0 and x[1]-x[0] >= 0:
        angle = math.asin((y[1]-y[0])/length)
    elif y[1]-y[0] >= 0 > x[1]-x[0]:
        angle = math.pi - math.asin((y[1]-y[0])/length)
    elif y[1]-y[0] < 0 and x[1]-x[0] < 0:
        angle = math.pi - math.asin((y[1]-y[0])/length)
    else:
        angle = 2*math.pi + math.asin((y[1]-y[0])/length)
    p5 = [m[0] + (length/(12**0.5))*math.cos(angle+math.pi/2), m[1] + (length/(12**0.5))*math.sin(angle+math.pi/2)]
    y_ = [p1[1], p3[1], p5[1], p4[1]]
    return y_


a = [0, 1]
b = [0, 0]
for i in range(n):
    a1 = []
    b1 = []
    for j in range(len(a)-1):
        ax = [a[j], a[j+1]]
        bx = [b[j], b[j+1]]
        a1.extend(x_transformation(ax, bx))
        b1.extend(y_transformation(ax, bx))
    a = a1
    a.append(1)
    b = b1
    b.append(0)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(a, b, color="black", linewidth=1)
ax.axis('equal')

plt.show()
