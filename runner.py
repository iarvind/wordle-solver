# Design
# We create a set of all 5 letter words
# .filter -> user inputs (fix position, varied position)
# .order -> using frequency of each letter

def filterIt(masterList, fixPos, varPos, selectedWords):
	result = []
	invalidChars = [];
	
	for word in selectedWords:
		for c in word:
			if c not in fixPos and c not in varPos:
				invalidChars.append(c)
	
	for word in masterList:
		for key in fixPos.keys():
			idxs = fixPos[key];
			for idx in idxs:
				if word[idx-1] != key:
					print("leaving1" + word[idx-1] + ":" + key);
					continue

		for key in varPos.keys():
			idxs = varPos[key];
			for idx in idxs:
				if word[idx-1] == key:
					# print("leaving2 " + word[idx-1] + ":" + key);
					continue

		for c in invalidChars:
			if c in word:
				# print("leaving3 " + word + " " );
				# print(invalidChars)
				continue

		result.append(word);
	return result


def analyse(fixPos, varPos, selectedWords):
	print ("analysing...");	
	file1 = open('five-letter-words.txt', 'r')
	Lines = file1.readlines()
	masterList = []
	for line in Lines:
		masterList.append(line.strip().upper())

	#filter
	masterList = filterIt(masterList, fixPos, varPos, selectedWords)
	
	#order
	#return list
	return masterList


# input format: <char>:1,2,3
def getInput():
	result = {};
	var = "";
	while True:
		var = input()
		if var != ".":
			var = var.replace(':', ',')
			var = var.split(',')
			result[var[0]] = []
			for v in var[1:]:
				result[var[0]].append(int(v))
		else:
			print("received inputs: ")
			print(result)
			break
	return result


def main():
	print("inside main")
	selectedWords = []
	start = True

	while True:
		fixPos = {}
		varPos = {}
		if not start:
			print ("what did you input?")
			selectedWords.append(input())
			print ("Provide fix position. To end, provide .")
			fixPos = getInput();
			print ("Provide var position. To end, provide .")
			varPos = getInput();

		list = analyse(fixPos, varPos, selectedWords)
		if not start:
			print(list)
		start = False



if __name__ == '__main__':
	print ("hi, let's solve it!");
	main()

'''
input
APPLE
A:1
.
P:2
.
'''