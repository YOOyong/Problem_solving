class Solution:
    def dfs(self, grid, x, y):
        if x <= -1 or y <= -1 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return

        grid[x][y] = '0'

        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y + 1)
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x, y - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(x, y):
            if x <= -1 or y <= -1 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)


        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    answer += 1

                    # dfs가 한 일은 인접한 육지를 모두 순회하며 숫자를 바꾼것.
                    # dfs가 실횅된 횟수가 육지의 개수.

        return answer