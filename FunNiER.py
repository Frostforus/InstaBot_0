import time
import random


def FuNnY(not_funny):
    random.seed(time.time())
    FuNnyxd = ""
    for i, char in enumerate(not_funny, 0):
        if i % 3 == 0:
            FuNnyxd += char.upper()
        elif i % 3 == 1:
            FuNnyxd += char.lower()
        else:
            if random.choice([0, 1]):
                FuNnyxd += char.upper()
            else:
                FuNnyxd += char.lower()
    return FuNnyxd


if __name__ == "__main__":
    print(FuNnY("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"))
