import time
import matplotlib.pyplot as plt
from random import randrange, randint


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
        plt.plot(1,1)
        plt.title('React!')
    input()
    t1 = time.time()
    print('Reaction time: ')
    plt.close()
    print(str(t1 - t0) + ' s' )
    print()
    