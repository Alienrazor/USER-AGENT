#pure python
#tunnel continues print agent's

import time
import os
     
from user_agent import generate_user_agent, generate_navigator

from pprint import pprint

a = generate_user_agent()

print(a, end="\n")


open('/sdcard/USER-AGENT.txt', 'a').write(a+'\n')


os.system('python test.py')
    


#Script End