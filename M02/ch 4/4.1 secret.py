import random
secret = random.randint(1, 10)
while True:
    print('Guess a number between 1 and 10')
    guess = input()
    i = int(guess)
    if i == secret:
        print('Just Right')
        break
    elif i < secret:
               print('Too Low')
    elif i > secret:
               print('To High')
