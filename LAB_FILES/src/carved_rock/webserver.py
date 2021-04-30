from random import randint
from time import sleep

def main():
    while True:
        data = []
        limit = randint(int(1e6), int(5e6))
        #print(limit)
        for n in range(limit):
            data.append(randint(0, 255))
            sleep(0.000001)

if __name__ == '__main__':
    main()