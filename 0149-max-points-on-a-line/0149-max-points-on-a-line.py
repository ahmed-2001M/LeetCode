class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        mx =1
        for i in range(len(points)):
            mp = {}
            same =0
            for j in range(i,len(points)):
                x,y = points[j][0] , points[j][1]
                if x == points[i][0] and y == points[i][1]: 
                    same += 1
                    continue
                if points[i][0] == x: slope = 'i'
                else:slope = (points[i][1] - y) / (points[i][0] - x)
                if mp.get(slope):
                    mp[slope]+=1
                else:
                    mp[slope] =1
            for i in mp.values():
                mx = max(mx,i+same)
        return mx

        