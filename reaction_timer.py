import time
import numpy as np
from random import randrange, randint

reaction_time = np.array([])
audio_stimulus = np.array([], dtype=bool)
for i in range(2):
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
        audio_stimulus = np.append(audio_stimulus, True)
    else:
        print('REACT!!!')
        audio_stimulus = np.append(audio_stimulus, False)
    input()
    reaction_time = np.append(reaction_time, time.time() - t0)
    print('Reaction time: ')
    print(str(reaction_time[-1]) + ' s' )
    print()

 
print()
print('Audio stimulus:')
print('Avg. reaction time: {0:.3f} s, STD {1:.3f}'.format(
        reaction_time[audio_stimulus].mean(), 
        reaction_time[audio_stimulus].std()))
print('Visual stimulus:')
print('Avg. reaction time: {0:.3f} s, STD {1:.3f}'.format(
        reaction_time[~audio_stimulus].mean(), 
        reaction_time[~audio_stimulus].std()))