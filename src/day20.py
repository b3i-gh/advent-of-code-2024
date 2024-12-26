import sys

def main(input):
    G = {(x, y): c for y, line in enumerate(input.splitlines()) for x, c in enumerate(line)}

    S = next(pos for pos, c in G.items() if c == 'S')
    E = next(pos for pos, c in G.items() if c == 'E')

    path = [S]
    prev = ()
    while path[-1] != E:
        x, y = path[-1]
        for dx, dy in (0, -1), (1, 0), (0, 1), (-1, 0):
            nxy = x+dx, y+dy
            if nxy != prev and G.get(nxy, '#') != '#':
                prev = path[-1]
                path.append(nxy)
                break

    path = {loc: dist for dist, loc in enumerate(path)}

    p1 = 0
    p2 = 0
    for dx in range(-20, 21):
        for dy in range(-20, 21):
            cheat = abs(dx)+abs(dy)
            if cheat < 2 or cheat > 20:
                continue
            for sx, sy in path:
                if (sx+dx, sy+dy) in path and path[sx+dx, sy+dy]-path[sx, sy]-cheat >= 100:
                    if cheat == 2:
                        p1 += 1
                    p2 += 1
    return p1,p2