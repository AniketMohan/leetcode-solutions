# 149. Max Points on a Line
# Hard
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Constraints:
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.

import math

def maxPoints(points) -> int: # points: list[list[int]]
    if len(points) in [1,2]:
        return len(points)

    lines = []
    answer = 0
    i = 0
    while i < len(points) - 1:
        j = i + 1
        while j < len(points):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2
            normalizing_factor = math.gcd(a,b,c)
            if a:
                if a < 0:
                    normalizing_factor *= -1
            elif b:
                if b < 0:
                    normalizing_factor *= -1
            line = [
                a//normalizing_factor,
                b//normalizing_factor,
                c//normalizing_factor
            ]
            if line not in lines:
                lines.append(line)
                answer = max(answer,len(list(filter(lambda point: a * point[0] + b * point[1] + c == 0,points))))
            j += 1
        i += 1
    return answer

# Testing
for points in [[[-6,-1],[3,1],[12,3]], [[-2, -2], [-1,-1], [1,1],[2,2],[3,3], [1,4], [1,5], [4,1], [4,2], [4,3], [4,4]], [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]]: 
    print(points,maxPoints(points))
