class Dec:
	def __init__(self, enc_msg):
		self.enc_msg = enc_msg
	def decryption(self):

		decrypt = ''

		for char in self.enc_msg:
			if char == '0':
				decrypt += ' '
			elif char == 'f':
				decrypt += 'a'
			elif char == 'g':
				decrypt += 'b'	
			elif char == 'h':
				decrypt += 'c'
			elif char == 'i':
				decrypt += 'd'
			elif char == 'j':
				decrypt += 'e'
			elif char == 'k':
				decrypt += 'f'
			elif char == 'l':
				decrypt += 'g'
			elif char == 'm':
				decrypt += 'h'
			elif char == 'n':
				decrypt += 'i'
			elif char == 'o':
				decrypt += 'j'
			elif char == 'p':
				decrypt += 'k'
			elif char == 'q':
				decrypt += 'l'
			elif char == 'r':
				decrypt += 'm'
			elif char == 's':
				decrypt += 'n'
			elif char == 't':
				decrypt += 'o'
			elif char == 'u':
				decrypt += 'p'
			elif char == 'v':
				decrypt += 'q'
			elif char =='w':
				decrypt += 'r'
			elif char =='x':
				decrypt += 's'
			elif char =='y':
				decrypt += 't'
			elif char =='z':
				decrypt += 'u'
			elif char =='a':
				decrypt += 'v'
			elif char =='b':
				decrypt += 'w'
			elif char =='c':
				decrypt += 'x'
			elif char =='d':
				decrypt += 'y'
			elif char == 'e':
				decrypt += 'z'
			elif char == '+':
				decrypt += '+'
			elif char == '*':
				decrypt += '*'
			elif char == '#':
				decrypt += '#'
			elif char == '/':
				decrypt += '/'
			elif char == '_':
				decrypt += '_'
			elif char == '.':
				decrypt += '.'
			elif char == ',':
				decrypt += ','
			elif char == '-':
				decrypt += '-'
			elif char == '\"':
				decrypt += '\"'
			elif char == ':':
				decrypt += ':'
			elif char == '9':
				decrypt += '1'
			elif char == '8':
				decrypt += '2'
			elif char == '7':
				decrypt += '3'
			elif char == '6':
				decrypt += '4'
			elif char == '`':
				decrypt += '5'
			elif char == '4':
				decrypt += '6'
			elif char == '3':
				decrypt += '7'
			elif char == '2':
				decrypt += '8'
			elif char == '1':
				decrypt += '9'
			elif char == '~':
				decrypt += '0'
		return decrypt[::-1]
