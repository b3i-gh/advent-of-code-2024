import re

def main(input):
    ans1 = ans2 = 0
    secs = 4750
    C = 101
    R = 103

    robots = parseRobotInitialState(input)
    q1 = q2 = q3 = q4 = 0

    # part 1
    for ro in robots:
        fx = (ro[0] + ro[2] * secs) % C
        fy = (ro[1] + ro[3] * secs) % R

        if fx < C // 2 and fy < R // 2:
            q1 += 1
        elif fx > C // 2 and fy < R // 2:
            q2 += 1
        if fy > R // 2 and fx < C // 2:
            q3 += 1
        elif fy > R // 2 and fx > C // 2:
            q4 += 1

    ans1 = q1 * q2 * q3 * q4


    # part 2

    for i in range(1, 10000):
        seen = set()
        for ro in robots:
            fx = (ro[0] + ro[2] * i) % C
            fy = (ro[1] + ro[3] * i) % R
            seen.add((fx,fy))
        if len(seen) == 500:
            ans2 = i
            print(i)
            break


    print("\n".join("".join(" " if (x,y) not in seen else "#" for x in range(103)) for y in range(101)))
  
    return ans1, ans2


def parseRobotInitialState(input):
    robots = []
    for l in input.strip().split("\n"):
        [x,y] = re.findall("-*\d+", l.split(" ")[0])
        [x,y] = [int(x), int(y)]
        [vx,vy] = re.findall("-*\d+", l.split(" ")[1])
        [vx,vy] = [int(vx), int(vy)]
        robots.append((x,y,vx,vy))
    return robots