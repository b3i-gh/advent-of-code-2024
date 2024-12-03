import re

# my solution (second regexp found on reddit)

def main(input):
    answer1 = 0
    answer2 = 0

    # part 1

    matches = re.findall(r"mul\(\d+,\d+\)" , input)
   
    for match in matches:
        [a,b] = match[4:-1].split(",")
        answer1 += int(a)*int(b)


    # part 2
    matches = re.findall(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", input)
    do = True
    for match in matches:
        if match[0] == "do()":
            do = True
        elif match[1] == "don't()":
            do = False
        elif do:
            answer2 += int(match[2]) * int(match[3])

    return answer1, answer2

