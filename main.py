import traceback
import importlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("day", nargs="?", type=int, help="Select just one day to run")
parser.add_argument("-t", "--test", action="store_true", help="Run tests instead of input")
parser.add_argument("-d", "--debug", action="store_true", help="Include error outputs for test cases")

args = parser.parse_args()

if args.debug:
	args.test = True

	
def runDay(day, path=None):
	path = path or f"data/day{day:02d}/input"
	with open(path,'r') as f:
		inp = f.read().strip()
		try:
			results = importlib.import_module(f"src.day{day:02d}").main(inp)
		except Exception as e:
			if args.debug:
				traceback.print_exc()
			results = (str(e),None)
		return results

def printDay(intro, results):
	print(intro)
	if results == None:
		print("  No output")
	else:
		print("  Part 1:",results[0])
		if results[1] != None:
			print("  Part 2:",results[1])		

# def runTests(day):
# 	test_paths = os.listdir(f"data/day{day:02d}/tests")
# 	test_paths.remove(".gitkeep")
# 	for test_path in test_paths:
# 		printDay(f"Test {test_path}:", *runDay(day, f"data/day{day:02d}/tests/"+test_path))
# 		print()

# 	# with open(f"data/day{day:02d}/input",'r') as f:
# 	# 	inp = f.read().strip()
# 	# 	start_time = time.time()
# 	# 	results = days[day].main(inp)
# 	# 	elapsed = time.time() - start_time
# 	# 	return results, elapsed*1000

print(" -- ADVENT OF CODE 2024 --")
print()
if args.day == None:
    print(" usage: main.py $day [-t] [-d]")
	
	# if args.test: print("(test flag ignored due to running all days)")
	# total = 0
	# for i in range(1,26):
	# 	results, elapsed = runDay(i)
	# 	if results == None: break
	# 	printDay(f"Day {i}:", results)
	# 	total+=elapsed
# 	print(f"\nAll days combined took {int(total)}ms")
# else:
# 	if args.test:
# 		runTests(args.day)
else:
	printDay(f"Day {args.day}:", runDay(args.day))