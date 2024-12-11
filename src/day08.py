import sys 
from collections import defaultdict

def main(input):
    ans1 = 0
    ans2 = 0
    antinodes = set()
    map = input.strip().split("\n")
    R = len(map)
    C = len(map[0])
    antennas = {}
    
    for r in range(R):
        for c in range(C):
            x = map[r][c]
            if x != '.':
                if x not in antennas:
                    antennas[x] = set()
                    antennas[x].add((r, c))
                else:
                    antennas[x].add((r,c))

    for symbol in antennas:
        for y,x in antennas[symbol]:

            for yy,xx in antennas[symbol]:
                if x != xx and y != yy:
                    dir = "/" 

                    if (x <= xx and y <= yy) or (x > xx and y > yy):
                        dir = "\\"                    

                    dx = max(x,xx) - min(x,xx)
                    dy = max(y,yy) - min(y,yy)

                    if dir == "/":
                        ax = max(x,xx) + dx
                        ay = min(y,yy) - dy
                        bx = min(x,xx) - dx
                        by = max(y,yy) + dy
                    else:
                        ax = min(x,xx) - dx
                        ay = min(y,yy) - dy
                        bx = max(x,xx) + dx
                        by = max(y,yy) + dy

                    if 0 <= ax < C and 0 <= ay < R:
                        antinodes.add((ax,ay))
                    if 0 <= bx < C and 0 <= by < R:    
                        antinodes.add((bx,by))

    ans1 = len(antinodes)
    
    # part 2 from reddit
    


    def inbounds(map, x, y):
        return 0 <= x < len(map[0]) and 0 <= y < len(map)


    def antinodes(p1, p2):
        p1_pts = set()
        p2_pts = {p1, p2}

        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1

        if inbounds(data, x1 - dx, y1 - dy):
            p1_pts.add((x1 - dx, y1 - dy))
        if inbounds(data, x2 + dx, y2 + dy):
            p1_pts.add((x2 + dx, y2 + dy))

        curX, curY = x1, y1
        while True:
            curX -= dx
            curY -= dy
            if not inbounds(data, curX, curY):
                break
            p2_pts.add((curX, curY))

        curX, curY = x1, y1
        while True:
            curX += dx
            curY += dy
            if not inbounds(data, curX, curY):
                break
            p2_pts.add((curX, curY))

        return p1_pts, p2_pts


    data = input.strip().split("\n")

    lut = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == ".":
                continue
            lut[data[y][x]].append((x, y))

    p1 = set()
    p2 = set()
    for f, l in lut.items():
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                p1_pts, p2_pts = antinodes(l[i], l[j])
                p1.update(p1_pts)
                p2.update(p2_pts)

    print(f"Part 1: {len(p1)}")
    print(f"Part 2: {len(p2)}")
    ans2 = len(p2)
                        



    return ans1, ans2
