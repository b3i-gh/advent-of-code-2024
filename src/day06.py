# my solution (part 1)

def main(input):
    ans1 = 0
    ans2 = 0

    direction = 0
    visited = set()

    [x,y] = findStartingPosition(input)
    area = input.strip().splitlines()
    visited.add((x,y))
    while True:
        
        dr, dc = [(-1,0),(0,1),(1,0),(0,-1)][direction]
        x1 = x + dc
        y1 = y + dr

        if x1 < 0 or x1 >= len(area[0]) or y1 < 0 or y1 >= len(area):
            ans1 = len(visited)
            break

        if area[y1][x1] == '#':
            direction = (direction + 1 ) % 4
        else:
            [x,y] = [x1,y1]            
            visited.add((x,y))

    ans2 = part2FromReddit(input, visited)
    return ans1, ans2

def findStartingPosition(input):
    area = input.strip().splitlines()
    columns = len(area[0])
    stringInput = input.strip().replace('\n', '')
    for i in range(len(stringInput)):        
        if(stringInput[i] == '<' or
           stringInput[i] == '>' or
           stringInput[i] == 'v' or
           stringInput[i] == '^'):
            x = i % columns
            y = int(i / columns)
    return x, y
         

# part 2 from reddit
def part2FromReddit(input, path):
    lines = input.strip().splitlines()
    extents = len(lines), len(lines[0])
    pos = None
    blocks = set()
    for y, line in enumerate(lines):
        for x, space in enumerate(line):
            if space == '#':
                blocks.add((x, y))
            elif space == '^':
                assert pos is None, "Multiple starting spaces are not allowed"
                pos = (x, y)

    assert pos is not None, "Cannot find starting space"

    start = pos
    answer = 0    
    for x, y in path:
        seen = set()
        pos = start
        direction = (0, -1)
        cycle = False
        while (0 <= pos[0] < extents[0]) and (0 <= pos[1] < extents[1]) and (not cycle):
            state = (pos, direction)
            if state in seen:
                cycle = True
                continue
            
            seen.add(state)
            step = pos[0] + direction[0], pos[1] + direction[1]
            if (step in blocks) or (step == (x, y)):
                direction = TURN[direction]
            else:
                pos = step
        answer += cycle
        print(answer)
    return answer

TURN = {( 0, -1): ( 1,  0),    # Up -> Right
        ( 1,  0): ( 0,  1),    # Right -> Down
        ( 0,  1): (-1,  0),    # Down -> Left
        (-1,  0): ( 0, -1),    # Left -> Up
       }