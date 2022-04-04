"""
https://gist.github.com/scottjacksonx/331707/983a804ad00bdc71d1b35f29186e8ea2e0aea354
"""

import random

def rstr():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    randStr = ""
    random.seed()

    for i in range(0,24):
	    rand = random.randint(0,25)
	    randStr += alphabet[rand]

    return randStr