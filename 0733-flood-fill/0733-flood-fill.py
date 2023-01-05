class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        point = image[sr][sc]
            
        def fill(i , j):
            if image[i][j] == color:
                return 
            if image[i][j] != point:
                return
            
            image[i][j]=color
            
            if i+1 <len(image): fill(i+1,j)
            if i>=1: fill(i-1,j)
            if j+1 <len(image[0]): fill(i , j+1)
            if j>=1: fill(i , j-1)
            
        fill(sr , sc)
        return image
            
            
            
            
            