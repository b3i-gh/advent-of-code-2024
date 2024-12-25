def main(input):
    ans1 = ans2 = 0

    s1, s2 = input.split("\n\n")
    s1 = set(s1.split(", "))

    cache = {}

    def solve(s):
        if s not in cache:
            if len(s) == 0:
                return 1
            else:
                result = 0
                for poss in s1:
                    if s.startswith(poss):
                        result += solve(s[len(poss):])
                cache[s] = result
        return cache[s]
            
    for l in s2.split("\n"):
        if solve(l) > 0:
            ans1 += 1
        ans2 += solve(l)

    return ans1, ans2