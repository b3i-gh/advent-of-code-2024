# my solution

# dict = {}

# def main(input):
#     ans1 = 0
#     ans2 = 0

#     [rules, updates] = input.split("\n\n")
    
#     # setups the rule dictionary
    
#     for rule in rules.splitlines():
#         [f,s] = rule.split("|")
#         if f not in dict:
#             dict[f] = []
#         dict[f].append(int(s))


#     # check the updates
#     for update in updates.splitlines():
#         update = update.split(",")
#         correctUpdate = True
#         # print("update:", update)
#         # print(dict)
#         for page in update:
#             if page not in dict:
#                 continue
#             else:
#                 correctUpdate = checkCorrectness(page, update)

#             if not correctUpdate:
#                 break
#         # print(update, correctUpdate)
#         if correctUpdate:            
#             ans1 += int(update[len(update)//2])
#         # else:
#             # correctedUpdate = fixUpdate(update)
#             # ans2 += int(correctedUpdate[len(correctedUpdate)//2])
#     return ans1, ans2


# def checkCorrectness(currPage, update):  
#     correct = True      
#     # print("currPage:",currPage)
#     for page in update:
#         if page == currPage:
#             break
#         else:
#             if int(page) in dict[currPage]:
#                 return False
#     return correct

# def fixUpdate(update):
#     fixedUpdate = update
#     print("fixedUpdate:", fixedUpdate)
    
#     currPageIndex = len(update)-1
#     print("currPageIndex:", currPageIndex)
    
#     while currPageIndex > 0:
#         currPage = update[currPageIndex]
#         print("currPage:", currPage)

#         for i, page in enumerate(update):
#             if page in dict[currPage]:
#                 fixedUpdate = update[:i] + update[i+1:] + update[i]
#                 break
#         currPageIndex -= 1

#     return fixedUpdate


# reddit solution
def main(input):
    rules, pages = input.strip().split('\n\n')
    rules = {tuple(map(int, x.split('|'))) for x in rules.split()}
    pages = [ list(map(int, x.split(','))) for x in pages.split()]

    from functools import cmp_to_key
    key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))

    ans1 = sum(new_row[len(row)//2] for row in pages if row == (new_row := sorted(row, key=key))) 
    ans2 = sum(new_row[len(row)//2] for row in pages if row != (new_row := sorted(row, key=key))) 
    return ans1, ans2