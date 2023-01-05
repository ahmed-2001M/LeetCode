class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1

        points = sorted(points)
        prev=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]> prev:
                res+=1
                prev = points[i][1]
            else:
                prev = min(prev,points[i][1])
        return res
                