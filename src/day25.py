def main(input):
    ans1 = 0

    M = 5 # max height

    K = [] # keys
    H = [] # holes

    def parseBlock(s):
        s = s.split("\n")
        k = list([0,0,0,0,0])
        for r in s[1:-1]:
            for i in range(5):
                if r[i] == "#":
                    k[i] += 1
        return  k
    
    for b in input.strip().split("\n\n"):
        if b.startswith("....."):
            K.append(parseBlock(b))
        else:
            H.append(parseBlock(b))

    for k in K:
        for h in H:
            ok = True
            for i in range(5):
                if k[i] + h[i] > 5:
                    ok = False
                    break
            if ok:
                ans1 += 1
    return ans1, "It's done :)"