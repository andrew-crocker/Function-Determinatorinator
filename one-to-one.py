# one-to-one prompts the user for input and/or reads a list of function pairs from a file, then determines whether the data points represent a one-to-one function or not.

def print_instructions():
	print("\nThe following program is intended to take a list of function pairs as input, and it determines whether or not the function is one-to-one.\n")
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
	text_string = "".join(infile.readlines())
	function = multisplit(text_string, "\n\t|'\".,/?><;:[]{}-_=+()!@#$%^&*`~ abcdefghijklmnopqrstuvwxyz")
	return function

def from_user():
	data = ""
	while True:
		data2 = input("Type a function pair and press Enter. (Blank line to quit): ")
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
					index = -1;
					subindex = 0;
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

def is_Onto(codomain):
	return 1

def process_input(domain, codomain):
	if function_check(domain, codomain):
		OneToOne = is_OneToOne(codomain)
		Onto = is_Onto(codomain)
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
			print("Onto not currently implemented.")
		else:
			print("Not onto.")

def main():
	print_instructions()
	domain, codomain = get_input()
	OneToOne, Onto, Function = process_input(domain, codomain)
	print_result(OneToOne, Onto, Function)

main()