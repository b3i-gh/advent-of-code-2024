def main(input):
    ans1 = 0
    ans2 = 0
    grid = input.strip().split("\n")

    R = len(grid)
    C = len(grid[0])

    path = []

    grid = [list(map(int, row)) for row in grid]

    trailheads = []
    visited = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                trailheads.append((r,c))

    def dfs(y, x, ch, s):
        if (y,x) in visited:
            s += 0
        elif (not 0 <= y < R) or (not 0 <= x < C):
            s += 0
        elif grid[y][x] - ch != 1:
            s += 0
        elif grid[y][x] == 9:
            # visited.append((y,x))
            s += 1
        else:
            s = dfs(y-1, x, ch+1, s)
            s = dfs(y, x+1, ch+1, s)
            s = dfs(y+1, x, ch+1, s)
            s = dfs(y, x-1, ch+1, s)
            # visited.append((y,x))        
        return s


    for th in trailheads:
        visited = []
        score = dfs(th[0], th[1], ch = -1 , s = 0)
        ans1 += score

    return ans1, ans2
