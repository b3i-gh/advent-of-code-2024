def main(input):
    ans1 = 0
    ans2 = 0

    res = []
    ops = []
    for i, line in enumerate(input.strip().splitlines()):
        res.append(int(line.split(":")[0]))
        operators = line.split(":")[1].strip().split(" ")
        ops.append(operators)

    for i in range(len(res)):
        if calc(int(res[i]), ops[i], curValue = 0 , depth = 0, part = 1):
             ans1 += res[i]

    for i in range(len(res)):
        if calc(int(res[i]), ops[i], curValue = 0 , depth = 0, part = 2):
             ans2 += res[i]

    return ans1, ans2

def calc(target, factors, curValue, depth, part):
    if curValue == target and depth >= len(factors):
        return True
    
    if depth >= len(factors):
        return False
    
    factor = factors[depth]

    # try to sum
    if calc(target, factors, curValue + int(factor), depth+1, part):
        return True
    
    # try to multiply
    if calc(target, factors, curValue * int(factor), depth+1, part):
        return True
    
    # try to concatenate 
    if part == 2 and calc(target, factors, int(str(curValue) + str(factor)), depth+1, part):
        return True
    
    return False
