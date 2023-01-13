import random

secret=random.randint(1,10)
guess=5
if guess<secret:
    print('too low')
elif guess>secret:
        print('too high')
elif guess==secret:
        print('just right')