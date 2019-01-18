# Modules are files containing useful function you can incluide in your scripts
# There are core python modules, modules you can install using the pip package manager (including Django)
# custom modules

#Core python modules
import datetime
from datetime import date #import just sub module

import time
from time import time
#Pip Modules
#import camelcase

# today = datetime.date.today()
# print(today)

today = date.today()
print(today)

time = time()
print(time)

# c = camelcase.CamelCase()
# print( c.hump('are you there') )

#Importing custom modules functions.py
import functions
from functions import sayHello

print(sayHello('fred'))