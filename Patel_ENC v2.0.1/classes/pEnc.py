class Enc:
	def __init__(self, input_str):
		self.input_str = input_str
	
	def enryption(self):
		if self.input_str == "back()" or self.input_str == "b()":
			print("You typed exit")
		else:
			incryped = ''
			for char in self.input_str:
				if char == ' ':
					incryped += '0'
				elif char == 'a':
					incryped += 'f'
				elif char == 'b':
					incryped += 'g'	
				elif char == 'c':
					incryped += 'h'
				elif char == 'd':
					incryped += 'i'
				elif char == 'e':
					incryped += 'j'
				elif char == 'f':
					incryped += 'k'
				elif char == 'g':
					incryped += 'l'
				elif char == 'h':
					incryped += 'm'
				elif char == 'i':
					incryped += 'n'
				elif char == 'j':
					incryped += 'o'
				elif char == 'k':
					incryped += 'p'
				elif char == 'l':
					incryped += 'q'
				elif char == 'm':
					incryped += 'r'
				elif char == 'n':
					incryped += 's'
				elif char == 'o':
					incryped += 't'
				elif char == 'p':
					incryped += 'u'
				elif char == 'q':
					incryped += 'v'
				elif char =='r':
					incryped += 'w'
				elif char =='s':
					incryped += 'x'
				elif char =='t':
					incryped += 'y'
				elif char =='u':
					incryped += 'z'
				elif char =='v':
					incryped += 'a'
				elif char =='w':
					incryped += 'b'
				elif char =='x':
					incryped += 'c'
				elif char =='y':
					incryped += 'd'
				elif char == 'z':
					incryped += 'e'
				elif char == '+':
					incryped += '+'
				elif char == '*':
					incryped += '*'
				elif char == '#':
					incryped += '#'
				elif char == '/':
					incryped += '/'
				elif char == '_':
					incryped += '_'
				elif char == '.':
					incryped += '.'
				elif char == ',':
					incryped += ','
				elif char == '-':
					incryped += '-'
				elif char == '\"':
					incryped += '\"'
				elif char == ':':
					incryped += ':'
				elif char == '1':
					incryped += '9'
				elif char == '2':
					incryped += '8'
				elif char == '3':
					incryped += '7'
				elif char == '4':
					incryped += '6'
				elif char == '5':
					incryped += '`'
				elif char == '6':
					incryped += '4'
				elif char == '7':
					incryped += '3'
				elif char == '8':
					incryped += '2'
				elif char == '9':
					incryped += '1'
				elif char == '0':
					incryped += '~'
		
			#Printing The Encrypted Text
			return incryped[::-1]