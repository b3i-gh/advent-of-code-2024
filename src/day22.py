# def main(input): 
#     ans1 = ans2 = 0
#     S = list(map(int, input.strip().split("\n")))

#     def mix(a,b):
#         return a ^ b
    
#     def prune(a):
#         return a % 16777216
    
#     i = 0
#     for s in S:
#         i = 1
        
#         while i < 2001:
#             # Calculate the result of multiplying the secret number by 64. 
#             # Then, mix this result into the secret number. 
#             # Finally, prune the secret number.
#             x = s * 64
#             s = mix(x, s)
#             s = prune(s)

#             # Calculate the result of dividing the secret number by 32. 
#             # Round the result down to the nearest integer. 
#             # Then, mix this result into the secret number. 
#             # Finally, prune the secret number.
#             x = int(s / 32)
#             s = mix(x, s)
#             s = prune(s)

#             # Calculate the result of multiplying the secret number by 2048. 
#             # Then, mix this result into the secret number. 
#             # Finally, prune the secret number.
#             x = s * 2048
#             s = mix(x, s)
#             s = prune(s)

#             i += 1

#         ans1 += s
#     return ans1, ans2


import numpy as np

def main(input):
    nums = [int(x) for x in input.split('\n')]
    m = 16777216
    repeats = 2000
    total = 0
    memos = {}
    for x in nums: 
        seq = np.zeros(repeats + 1, dtype = int)
        seq[0] = x % 10
        for j in range(1, repeats + 1):
            x = (x ^ (x * 64)) % m
            x = (x ^ (x // 32)) % m
            x = (x ^ (x * 2048)) % m
            seq[j] =  x % 10
        total += x
        diffs = np.diff(seq)
        seen = set()
        for p in range(4,len(diffs)):
            h = tuple(diffs[p-3:p+1])
            if h not in memos and h not in seen:
                memos[h] = seq[p + 1]
            elif h not in seen:
                memos[h] += seq[p + 1]
            seen.add(h)
    print('Part 1:', total)
    print('Part 2: ', max(memos.values()))
    return total, max(memos.values())