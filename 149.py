# 149. Max Points on a Line
# Hard
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Constraints:
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.

# 2026-02-14 15:12 edit: time limit exceeded, slowwww
def maxPoints(points) -> int: # points: list[list[int]]
    if len(points) == 2 or len(points) == 1:
        return len(points)
    lines = []
    lines_vert = []
    max_num_points_on_line = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]

            if x2 - x1 == 0:
                if x1 in lines_vert:
                    continue
                lines_vert.append(x1)
                max_num_points_on_line = max(max_num_points_on_line, len(list(filter(lambda point: point[0] == x1, points))))
            else:
                c = x2 - x1
                m = (y2 - y1)/c
                b = y1 - m * x1

                if [m, b] in lines:
                    continue
                lines.append([m,b])
                max_num_points_on_line = max(max_num_points_on_line, len(list(filter(lambda point: c * point[1] == (y2 - y1) * point[0] + b * c, points))))
    return max_num_points_on_line

# Testing
for points in [[[-6,-1],[3,1],[12,3]]]: #[[-2, -2], [-1,-1], [1,1],[2,2],[3,3], [1,4], [1,5], [4,1], [4,2], [4,3], [4,4]], [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 
    print(points,maxPoints(points))
