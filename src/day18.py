from collections import deque

def main(input):
    ans1 = ans2 = 0

    DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
    N = 71
    G = [['.' for c in range(N)] for r in range(N)]

    for i, line in enumerate(input.split("\n")):
        x,y = [int(x) for x in line.split(',')]
        if 0 <= y < N and 0 <= x < N:
            G[y][x] = "#"

        Q = deque([(0,0,0)])
        SEEN = set()
        ok = False
        while Q:
            d,r,c = Q.popleft()
            if (r,c) == (N-1,N-1):
                if i == 1023:
                    ans1 = d
                ok = True
                break
            if (r,c) in SEEN:
                continue
            SEEN.add((r,c))
            for dr,dc in DIRS:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < N and 0 <= cc < N and G[rr][cc] != '#':
                    Q.append((d+1, rr, cc))
        if not ok:
            ans2 = (x,y)
            break

    return ans1,ans2