from z3 import *
A = 0
B = 0
C = 0
ans1 = ans2 = []
pointer = 0

def decodeCOMBO(op):
    match op:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C

def decodeInstruction(ins, operand):
    global A
    global B
    global C
    global ans1
    global ans2
    global pointer

    match ins:
        case 0: # adv
            v = A / 2**(decodeCOMBO(operand))
            A = int(v)
            pointer += 2
        case 1: # bxl
            B = B ^ operand
            pointer += 2
        case 2: # bst
            B = decodeCOMBO(operand) % 8
            pointer += 2
        case 3: # jns
            if A != 0:
                pointer = operand
            else:
                pointer += 2
        case 4: # bxc
            B = B ^ C
            pointer += 2
        case 5: # out
            v = decodeCOMBO(operand) % 8
            ans1.append(v)
            pointer += 2
        case 6: # dbv
            v = A / 2**(decodeCOMBO(operand))
            B = int(v)
            pointer += 2
        case 7: # cdv
            v = A / 2**(decodeCOMBO(operand))
            C = int(v)
            pointer += 2
            

def main(input):
    global A
    global B
    global C
    global ans1
    global ans2
    global pointer

    # read the input
    op = []
    for l in input.strip().split("\n"):
        if len(l.split(":")) > 1:
            op.append(l.split(":")[1].strip())
    A = int(op[0])
    B = int(op[1])
    C = int(op[2])
    P = list(map(int, op[3].split(",")))

    # part 1
    while pointer < len(P):
        decodeInstruction(P[pointer], P[pointer+1])


    def part2(input):
        # Each 3 bits of A is a function of at most 10 bits, and each iteration of the program 
        # shifts by 3 bits. We can choose the lowest 10-bit number producing the last opcode, 
        # shift by 3 bits, find a 10-bit number matching the previous opcode and also 
        # the 10 bits we chode before, etcetera. There are multiple options for the second part, 
        # so we add backtracking to make sure we find the sequence of options that makes us 
        # produce the entire program. 
        
        import sys
        import re

        def run(program, regs):
            a, b, c = range(4, 7)
            ip = 0
            combo = [0, 1, 2, 3, *regs]
            while ip < len(program):
                opcode, operand = program[ip:ip + 2]
                if opcode == 0:
                    combo[a] >>= combo[operand]
                elif opcode == 1:
                    combo[b] ^= operand
                elif opcode == 2:
                    combo[b] = combo[operand] % 8
                elif opcode == 3:
                    if combo[a]:
                        ip = operand - 2
                elif opcode == 4:
                    combo[b] ^= combo[c]
                elif opcode == 5:
                    yield combo[operand] % 8
                elif opcode == 6:
                    combo[b] = combo[a] >> combo[operand]
                elif opcode == 7:
                    combo[c] = combo[a] >> combo[operand]
                ip += 2

        def expect(program, out, prev_a=0):
            if not out:
                return prev_a
            for a in range(1 << 10):
                if a >> 3 == prev_a & 127 and next(run(program, (a, 0, 0))) == out[-1]:
                    ret = expect(program, out[:-1], (prev_a << 3) | (a % 8))
                    if ret is not None:
                        return ret

        nums = list(map(int, re.findall(r'\d+', input)))
        regs = nums[:3]
        program = nums[3:]
        print(','.join(map(str, run(program, regs))))
        print(expect(program, program))
        
    print(part2(input))    
    return ans1, ans2

        


