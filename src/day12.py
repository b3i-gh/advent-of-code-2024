def main(input):
    ans1 = ans2 = 0

    grid = input.strip().split("\n")
    R = len(grid)
    C = len(grid[0])
    
    def findPlots(grid):
        plots = []
        plotted = list() 

        def dfs(r, c, a, p): 
                visited.add((r,c))
                if grid[r][c] == a:
                    N = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for n in N:
                        if (r + n[0], c + n[1]) not in visited and (0 <= r + n[0] < R) and (0 <= c + n[1] < C):
                            dfs(r + n[0], c + n[1], a, p)
                    p.append((r,c))
                return p
      
        for r in range(R):
             for c in range(C):
                  visited = set()
                  if (r,c) not in plotted:
                    plot = dfs(r, c, a = grid[r][c], p = [])
                    plots.append((grid[r][c], plot))
                    plotted += plot
        return plots

    plots = findPlots(grid)
    
    # part 1
    for plot in plots:
        area = len(plot[1])
        perimeter = 0
        for square in plot[1]:
            N = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            r = square[0]
            c = square[1]
            
            for n in N:
                r = square[0] + n[0]
                c = square[1] + n[1]
                
                if not (0 <= r < R) or not (0 <= c < C) or grid[r][c] != plot[0]:
                    perimeter += 1
        ans1 += area * perimeter

    # part 2
    for plot in plots:
        area = len(plot[1])
        sides = 0
        for r in range(R): # top to bottom 
            encounteredSquares = []
            for c in range(C):
                if (r,c) in plot[1] and (r == 0 or grid[r-1][c] != grid[r][c]):
                    encounteredSquares.append((r,c))
            if(len(encounteredSquares) > 0):
                t = 1
                for i in range(len(encounteredSquares))[1:]:
                    if encounteredSquares[i][1] - encounteredSquares[i-1][1] > 1:
                        t += 1
                sides += t

        for r in range(R - 1, -1, -1): # bottom to top
            encounteredSquares = []
            for c in range(C):
                if (r,c) in plot[1] and (r+1 == R or grid[r][c] != grid[r+1][c]):
                    encounteredSquares.append((r,c))
            if(len(encounteredSquares) > 0):
                t = 1
                for i in range(len(encounteredSquares))[1:]:
                    if encounteredSquares[i][1] - encounteredSquares[i-1][1] > 1:
                        t += 1
                sides += t  

        for c in range(C): # left to right
            encounteredSquares = []
            for r in range(R):
                if (r,c) in plot[1] and (c == 0 or grid[r][c-1] != grid[r][c]):
                    encounteredSquares.append((r,c))
            if(len(encounteredSquares) > 0):
                t = 1
                for i in range(len(encounteredSquares))[1:]:
                    if encounteredSquares[i][0] - encounteredSquares[i-1][0] > 1:
                        t += 1
                sides += t

        for c in range(C - 1, -1, -1): # right to left
            encounteredSquares = []
            for r in range(R):
                if (r,c) in plot[1] and (c+1 == C or grid[r][c] != grid[r][c+1]):
                    encounteredSquares.append((r,c))
            if(len(encounteredSquares) > 0):
                t = 1
                for i in range(len(encounteredSquares))[1:]:
                    if encounteredSquares[i][0] - encounteredSquares[i-1][0] > 1:
                        t += 1
                sides += t  
                 
        ans2 += area * sides

    # assert ans2 == 1206, f"error: expected = 1206, returned = {ans2}"
    return ans1, ans2