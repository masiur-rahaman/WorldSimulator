from enum import Enum
import random


class UnHappyInputs(Enum):
    SLAP = 1
    SLANG = 2


if __name__ == '__main__':
    print(random.choice(list(UnHappyInputs)).name)
