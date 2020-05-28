import math
import os
import sys

import requests

print("hello World")

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello. {}'.format(who_to_greet)
    return greeting


print(greet('Durgesh'))
print(greet(' Singh'))
r = requests.get('https://fb.com')
print(r.status_code)
