import time
import numpy as np
from random import randrange, randint

reaction_time = []
for i in range(5):
    print('ready...')
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('0, set!')
    
    dt = randrange(0, 500) / 100
    time.sleep(dt)
    t0 = time.time()
    if randint(0, 1):
        print('\a')  # Beep
    else:
        print('REACT!!!')
    input()
    reaction_time.append(time.time() - t0)
    print('Reaction time: ')
    print(str(reaction_time[-1]) + ' s' )
    print()
    
print()
print('Avg. reaction time: {0:.3f} s, STD {1:.3f}'.format(np.mean(reaction_time), np.std(reaction_time)))
