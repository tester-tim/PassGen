import random
import string

print('Welcome to PassGen, the world\'s best password creator!')

length = int(input('Enter the number of character you would like your password to be: '))

low = string.ascii_lowercase
high = string.ascii_uppercase
number = string.digits
symbol = string.punctuation
all = low + high + number + symbol

temp = random.sample(all,length)

password = ''.join(temp)

print(password)


