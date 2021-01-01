import random
import time

numbers = ['10101101101110', '00010111111000', '01010101001101']

def main():
	while True:
		random_numb = random.choice(numbers)
		print(random_numb)
		time.sleep(0.1)
main()