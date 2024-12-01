def main(input):
	# my solution

	# lines = input.splitlines()
	# total1 = 0
	# total2 = 0

	# list1 = []
	# list2 = []
	# locationRepetitions = {}

	# for line in lines: 
	# 		[id1, id2] = line.split()
	# 		list1.append(int(id1))
	# 		list2.append(int(id2))

	# 		if(int(id2) in locationRepetitions):
	# 			locationRepetitions[int(id2)] += 1
	# 		else: 
	# 			locationRepetitions[int(id2)] = 1

	# list1.sort()
	# list2.sort()

	# i = 0
	# while i < len(list1):
	# 	total1 += abs(list1[i] - list2[i])
		
	# 	if list1[i] in locationRepetitions:
	# 		total2 += list1[i] * locationRepetitions[list1[i]]	
		
	# 	i += 1




	# optimized solution:
	left, right = [], []	
	total1 = 0
	total2  = 0
	lines = input.splitlines()
	for line in lines:
		line = line.split()
		left.append(int(line[0]))
		right.append(int(line[1]))
    	

	for l,r in zip(sorted(left), sorted(right)):
		total1 += abs(l-r)

	# for l in left:
	# 	total2 += l * right.count(l)
		
	#  more optimized:
	total2 = sum(l * right.count(l) for l in left)

	return total1, total2