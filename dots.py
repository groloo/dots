import os
import time
def main(time,option):
    dot = '.'
    
    if option == 'h':
        time *= 3600
    elif option == 'm':
        time *= 60
        
    for t in time:
        if len(dot) < 3:
            dot += '.'
        elif len(dot) > 2:
            dot = '.'
        os.system('cls')
        if 3600%t == 0:
            if option == 'h':
                text = f'restarting in {time/3600} hours'
            elif option == 'm':
                text = f'restarting in {time/60} minutes'
            else:
                text = f'restarting in {time} seconds'
        print(f"{text}{dot}")
        time.sleep(1)
