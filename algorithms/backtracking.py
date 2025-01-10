class Solution:
    def findPath(self, mat):
        
        n = len(mat)
        visited = set()
        paths = []
        
        def dfs(row, col, path):
            if (row == n-1) and (col==n-1):
                paths.append(''.join(path))
                return
            
            if row < 0 or row >= n or col < 0 or col >= n or mat[row][col] != 1 or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col, path + ['D']) 
            dfs(row, col - 1, path + ['L']) 
            dfs(row - 1, col, path + ['U'])
            dfs(row, col + 1, path + ['R']) 

            
            visited.remove((row, col))
                    
        dfs(0,0,[])
        return sorted(paths)

solution = Solution()
matrix = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]
result = solution.findPath(matrix)
print(result)



