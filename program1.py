class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        total_islands = 0

        def dfs(x, y):
            # If out of bounds or water, stop recursion
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 'W':
                return
            
            # Mark the current land as visited
            grid[x][y] = 'W'
            
            # Recursively visit all adjacent land cells
            dfs(x - 1, y)  # up
            dfs(x + 1, y)  # down
            dfs(x, y - 1)  # left
            dfs(x, y + 1)  # right

        # Iterate through the grid to find islands
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':  # Found a new island
                    total_islands += 1
                    dfs(i, j)  # Explore the entire island
        
        return total_islands
