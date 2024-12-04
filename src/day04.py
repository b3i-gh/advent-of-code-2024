def main(input):
    # my solution
    ans1 = 0
    ans2 = 0

    # part 1
    ARR = input.split("\n")
    R = len(ARR)
    C = len(ARR[0])
    for r in range(R):
        for c in range(C):
            if c+3<C and ARR[r][c]=="X" and ARR[r][c+1]=="M" and ARR[r][c+2]=="A" and ARR[r][c+3]=="S":
                ans1 += 1
            if r+3<R and ARR[r][c]=="X" and ARR[r+1][c]=="M" and ARR[r+2][c]=="A" and ARR[r+3][c]=="S":
                ans1 += 1
            if c+3<C and r+3<R and ARR[r][c]=="X" and ARR[r+1][c+1]=="M" and ARR[r+2][c+2]=="A" and ARR[r+3][c+3]=="S":
                ans1 += 1
            if c+3<C and ARR[r][c]=="S" and ARR[r][c+1]=="A" and ARR[r][c+2]=="M" and ARR[r][c+3]=="X":
                ans1 += 1
            if r+3<R and ARR[r][c]=="S" and ARR[r+1][c]=="A" and ARR[r+2][c]=="M" and ARR[r+3][c]=="X":
                ans1 += 1
            if c+3<C and r+3<R and ARR[r][c]=="S" and ARR[r+1][c+1]=="A" and ARR[r+2][c+2]=="M" and ARR[r+3][c+3]=="X":
                ans1 += 1
            if r-3>=0 and c+3<C and ARR[r][c]=="X" and ARR[r-1][c+1]=="M" and ARR[r-2][c+2]=="A" and ARR[r-3][c+3]=="S":
                ans1 += 1
            if r-3>=0 and c+3<C and ARR[r][c]=="S" and ARR[r-1][c+1]=="A" and ARR[r-2][c+2]=="M" and ARR[r-3][c+3]=="X":
                ans1 += 1

    # part 2
    for r in range(R):
        for c in range(C):
            if r+2<R and c+2<C and ARR[r][c]=='M' and ARR[r+1][c+1]=='A' and ARR[r+2][c+2]=='S' and ARR[r+2][c]=='M' and ARR[r][c+2]=='S':
                ans2 += 1
            if r+2<R and c+2<C and ARR[r][c]=='M' and ARR[r+1][c+1]=='A' and ARR[r+2][c+2]=='S' and ARR[r+2][c]=='S' and ARR[r][c+2]=='M':
                ans2 += 1
            if r+2<R and c+2<C and ARR[r][c]=='S' and ARR[r+1][c+1]=='A' and ARR[r+2][c+2]=='M' and ARR[r+2][c]=='M' and ARR[r][c+2]=='S':
                ans2 += 1
            if r+2<R and c+2<C and ARR[r][c]=='S' and ARR[r+1][c+1]=='A' and ARR[r+2][c+2]=='M' and ARR[r+2][c]=='S' and ARR[r][c+2]=='M':
                ans2 += 1                      

    return ans1,ans2
