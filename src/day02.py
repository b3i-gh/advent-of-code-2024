# my solution
# def main(input):

    # reports = input.splitlines()

    # answer1 = 0
    # answer2 = 0

    # # part 1
    # for report in reports:
    #     safe = True
    #     levels = list(map(int,report.split()))
    #     sign = levels[0] < levels[1]
    #     for i in range(len(levels) -1):
    #         if sign: # 0, 1 , 2 ...
    #             if levels[i+1] - levels[i] > 3 or levels[i+1] - levels[i] < 1:
    #                 safe = False
    #                 break                    
    #         else: # 9, 8 , 7 ...
    #             if levels[i] - levels[i+1] > 3 or levels[i] - levels[i+1] < 1:
    #                 safe = False
    #                 break
    #     if safe:
    #         answer1 += 1

    # # part 2
    # for report in reports:
    #     if checkReportSafety(report):      
    #         answer2 += 1
    
    # return answer1, answer2


# def checkReportSafety(report):
#     safe = True
#     levels = list(map(int,report.split()))      
#     sign = levels[0] < levels[1]
#     for i in range(len(levels) -1):            
#         if sign: # 0, 1 , 2 ...
#             if levels[i+1] - levels[i] > 3 or levels[i+1] - levels[i] < 1:
#                 safe = False
#                 break                    
#         else: # 9, 8 , 7 ...
#             if levels[i] - levels[i+1] > 3 or levels[i] - levels[i+1] < 1:
#                 safe = False
#                 break
#     if not safe:        
#         safe = tryToSanitize(report)        
#     return safe


# def tryToSanitize(report):
#     print(f"trying to sanitize {report}")
#     levels = list(map(int,report.split())) 
#     for i in range(len(levels)):   
#         safe = True
#         print(f"removing {i} element ({levels[i]})")
#         tempLevels = levels[:i] + levels[i+1:]  # slices the i element from the report
#         print(tempLevels)
#         if tempLevels[0] == tempLevels[1]:
#             return False
#         sign = tempLevels[0] < tempLevels[1]
#         for i in range(len(tempLevels) -1):            
#             if sign: # 0, 1 , 2 ...
#                 if tempLevels[i+1] - tempLevels[i] > 3 or tempLevels[i+1] - tempLevels[i] < 1:
#                     safe = False
#             else: # 9, 8 , 7 ...
#                 if tempLevels[i] - tempLevels[i+1] > 3 or tempLevels[i] - tempLevels[i+1] < 1:
#                     safe = False
#         if safe:
#             return True
#     return False


# optimized solution from reddit

def main(input):
    reports = [[int(x) for x in line.split()] for line in input.splitlines()]
    
    def safe(report):
        diffs = [y-x for x,y in zip(report, report[1:])]
        return all(1 <= x <= 3 for x in diffs) or all(1 <= -x <= 3 for x in diffs)
    
    def safe2(report):
        options = [report[0:i] + report[i+1:] for i in range(len(report))]
        return any(safe(report) for report in options)
    
    answer1 = sum(safe(report) for report in reports)
    answer2 = sum(safe2(report) for report in reports)
    return answer1, answer2