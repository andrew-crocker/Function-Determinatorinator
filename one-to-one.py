# one-to-one prompts the user for input and/or reads a list of function pairs from a file, then determines whether the data points represent a one-to-one function or not.

def print_instructions():
	print("\nThe following program is intended to take a list of function pairs as input, and it determines if the function is one-to-one and/or onto.\n")
	print("You will be asked to enter function pairs either by hand, or by giving the name of a file where they are stored.\n")

def multisplit(s, sep):
    for char in sep:
    	s = " ".join(s.split(char))
    return s.split()

def from_file():
	while True:
		try:
			filename = input("What file are the function pairs in? ")
			infile = open(filename, "r")
			break
		except FileNotFoundError:
			print("Looks like that file doesn't exist. Please try again.")
	text_string = "".join(infile.readlines()).lower()
	function = multisplit(text_string, "\n\t|'\".,/?><;:[]{}-_=+()!@#$%^&*`~ abcdefghijklmnopqrstuvwxyz")
	return function

def from_user():
	data = ""
	while True:
		data2 = input("Type a function pair and press Enter. (Blank line to quit): ").lower()
		if data2 == "":
			break
		data = data + " " + data2
	function = multisplit(data, "\n\t|'\".,/?><;:[]{}-_=+()!@#$%^&*`~ abcdefghijklmnopqrstuvwxyz")
	return function

def separate(function):
	domain = []
	codomain = []
	for s in range(0, len(function), 2):
		domain.append(function[s])
		codomain.append(function[s+1])
	return domain, codomain

def get_input():
	second_prompt = 0
	location = input("Are the function pairs stored in a file? [Yes/No]: ").lower()
	while True:
		try:
			if location[0] != "y" and location[0] != "n":
				second_prompt = 1
				location = input("Try again.. input from file? [Y/N]: ").lower()
			else:
				break
		except IndexError:
			if not second_prompt:
				location = input("Are the function pairs stored in a file? [Yes/No]: ").lower()
			else:
				location = input("Try again.. input from file? [Y/N]: ").lower()
	
	if location[0] == "y":
		FuncList = from_file()
	else:
		FuncList = from_user()

	domain, codomain = separate(FuncList)
	return domain, codomain

def function_check(domain, codomain):
	index = 0
	while index < len(domain):
		subindex = index + 1
		while subindex < len(domain):
			if domain[index] == domain[subindex]:
				if codomain[index] == codomain[subindex]:
					domain.remove(domain[index])
					codomain.remove(codomain[index])
					index = -1
					subindex = 0
					break
				else:
					return 0
			subindex = subindex + 1
		index = index + 1
	return 1

def is_OneToOne(codomain):
	for element in codomain:
		codomain.remove(element)
		for duplicate_entry in codomain:
			if element == duplicate_entry:
				return 0
	return 1

def is_Onto(Range, codomain):
	for i in Range:
		if i not in codomain:
			return 0

	return 1


def ask_onto():
	answer = input("Do you want to check if this function is Onto? [Yes/No]: ").lower()
	if answer[0] == 'y':
		return 1
	else:
		return 0

def get_range():
	location = input("Are the range values stored in a file? [Yes/No]: ").lower()
	Range = []
	while True:
		try:
			if location[0] != "y" and location[0] != "n":
				second_prompt = 1
				location = input("Try again.. input from file? [Y/N]: ").lower()
			else:
				break
		except IndexError:
			if not second_prompt:
				location = input("Are the range values stored in a file? [Yes/No]: ").lower()
			else:
				location = input("Try again.. input from file? [Y/N]: ").lower()
	
	if location[0] == "y":
		while True:
			try:
				filename = input("What file are the range values in? ")
				infile = open(filename, "r")
				break
			except FileNotFoundError:
				print("Looks like that file doesn't exist. Please try again.")
		text_string = "".join(infile.readlines()).lower()
		data = multisplit(text_string, "\n\t|'\".,/?><;:[]{}-_=+()!@#$%^&*`~ abcdefghijklmnopqrstuvwxyz")
		for i in range(0, len(data)):
			Range.append(data[i])

	else:
		data = input("Enter the range as a list of numbers and press Enter: ").lower()
		data2 = multisplit(data, "\n\t|'\".,/?><;:[]{}-_=+()!@#$%^&*`~ abcdefghijklmnopqrstuvwxyz")
		for i in range(0, len(data2)):
			Range.append(data2[i])

	return Range
	

def process_input(domain, codomain, Range):
	if function_check(domain, codomain):
		if Range:
			Onto = is_Onto(Range, codomain)
		else:
			Onto = -1
		OneToOne = is_OneToOne(codomain)
		return OneToOne, Onto, 1
	else:
		return 0, 0, 0

def print_result(OneToOne, Onto, Function):
	print()
	if not Function:
		print("This is not a function.")
	else:
		if OneToOne:
			print("One-to-one!")
		else:
			print("Not one-to-one.")
		if Onto:
			print("Onto!")
		elif Onto == 0:
			print("Not onto.")

def main():
	print_instructions()
	checkOnto = ask_onto()
	Range = 0
	if checkOnto:
		Range = get_range()
	domain, codomain = get_input()
	OneToOne, Onto, Function = process_input(domain, codomain, Range)
	print_result(OneToOne, Onto, Function)

main()