def main(input):
    ans1 = ans2 = blinks = 0
    ostones = list(map(int, input.strip().split(" ")))
    stones = list(ostones)

    # part 1
    while blinks < 25:
        blinks += 1
        for i in range(len(stones) - 1, -1, -1):
            if stones[i] == 0:
                stones[i] = 1
            elif len(str(stones[i])) %2 == 0:
                value = str(stones[i])
                midpoint = len(value) // 2                
                stones[i] = int((value)[:midpoint])
                stones.insert(i + 1,int((value)[midpoint:]))
            else: 
                stones[i] *= 2024
        print(blinks)

    #part 2
    cache = {}
    def ans(x, n):
        if n == 0:
            return 1
        if (x,n) not in cache:
            if x == 0:
                result = ans(1, n-1)
            elif len(str(x))%2 == 0:
                x = str(x)
                result = 0
                result += ans(int(x[:len(x)//2]), n-1)
                result += ans(int(x[len(x)//2:]), n-1)
            else:
                result = ans(2024 * x, n-1)
            cache[(x,n)] = result
        return cache[(x,n)]
    
    for x in ostones:
        ans2 += ans(x, 75)

    ans1 = len(stones)
    return ans1, ans2