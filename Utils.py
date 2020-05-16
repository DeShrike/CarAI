# Misc utility functions
import math
import random 
from Vector2 import Vector2

def map(n, start1, stop1, start2, stop2, withinBounds):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
    if withinBounds == False:
        return newval

    if start2 < stop2:
        return constrain(newval, start2, stop2)
    else:
        return constrain(newval, stop2, start2)

def myrandom(min = None, max = None):
    rand = random.random()
    if min == None:
        return rand;
    elif max == None:
            return rand * min
    else:
        if min > max:
            tmp = min
            min = max
            max = tmp
        return rand * (max - min) + min

previous = False
y2 = 0.0

def randomGaussian(mean, sd):
    global previous
    global y2
    if previous:
        y1 = y2
        previous = False
    else:
        while True:
            x1 = random.random() * 2.0 - 1.0
            x2 = random.random() * 2.0 - 1.0
            w = x1 * x1 + x2 * x2
            if w >= 1:
                break
        w = math.sqrt(-2.0 * math.log(w) / w)
        y1 = x1 * w
        y2 = x2 * w
        previous = True

    m = mean # || 0
    s = sd # || 1
    return y1 * s + m

def constrain(n, low, high):
    return math.max(Math.min(n, high), low)

def intersect(p0, p1, p2, p3):
    s1_x = p1.x - p0.x
    s1_y = p1.y - p0.y
    s2_x = p3.x - p2.x
    s2_y = p3.y - p2.y
    s = (-s1_y * (p0.x - p2.x) + s1_x * (p0.y - p2.y)) / (-s2_x * s1_y + s1_x * s2_y)
    t = (s2_x * (p0.y - p2.y) - s2_y * (p0.x - p2.x)) / (-s2_x * s1_y + s1_x * s2_y)
    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
        return Vector2(p0.x + (t * s1_x),  p0.y + (t * s1_y))
    return None

# Function to check intercept of line seg and circle
# A,B end points of line segment
# C center of circle
# radius of circle
# returns true if touching or crossing else false   
def doesLineInterceptCircle(A, B, C, radius):
    v1x = B.x - A.x
    v1y = B.y - A.y
    v2x = C.x - A.x
    v2y = C.y - A.y

    # get the unit distance along the line of the closest point to
    # circle center
    u = (v2x * v1x + v2y * v1y) / (v1y * v1y + v1x * v1x)
    
    # if the point is on the line segment get the distance squared
    # from that point to the circle center
    if u >= 0 and u <= 1:
        dist  = (A.x + v1x * u - C.x) ** 2 + (A.y + v1y * u - C.y) ** 2
    else:
        # if closest point not on the line segment
        # use the unit distance to determine which end is closest
        # and get dist square to circle
        if u < 0:
            dist = (A.x - C.x) ** 2 + (A.y - C.y) ** 2
        else:
            dist = (B.x - C.x) ** 2 + (B.y - C.y) ** 2

    return dist < radius * radius

def radians(degrees):
    return degrees * math.pi / 180.0
