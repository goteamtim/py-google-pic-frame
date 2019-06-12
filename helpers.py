import random

class Helpers(object):
	def __init__():
		pass
	
def generate_random_string( length ):
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.~0987654321'
    generated_string = ''
    counter = 0
    while (counter < length ):
        generated_string += seed[random.randint(0,len(seed))]
        counter += 1

    return generated_string