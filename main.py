import random
import string
encoded = ""

with open('words.txt', 'r', encoding='UTF-8') as f:
	words = f.readlines()
words = [word.strip() for word in words]
for _ in range(0, 8):
	random.shuffle(words)

message = input("Come on, tell me.\n~ ").strip()
for letter in message:
	if letter == ' ':
		encoded += "~ "
		continue
	if letter not in string.ascii_letters:
		encoded += letter + " "
		continue
	while True:
		word = random.choice(words)
		if word[0] == letter[0].lower():
			encoded += word + " "
			break

if len(encoded) < 2001:
	print("Your message:")
	print(encoded)
else:
	print("Oh no! Your message is quite big. I saved it to output.txt")
	with open('output.txt', 'a+', encoding='UTF-8') as f:
		f.write(encoded)