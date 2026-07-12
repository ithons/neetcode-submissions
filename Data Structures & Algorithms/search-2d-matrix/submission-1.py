class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        print(m,n)
        i = 0
        j = n*m-1

        while i<=j:
            mid = (i+j)//2
            x,y = (mid//n, mid%n)
            if matrix[x][y] < target: i=mid+1
            elif matrix[x][y] > target: j=mid-1
            else: return True
        return False
