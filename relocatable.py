from __future__ import print_function

import array
import pickle
import random


def load(memory, program, start, fixups):
    """Load program into memory from the given start address."""
    # IMPLEMENT ME


def run(memory, start):
    """Runs the program in memory beginning at start."""
    # DO NOT CHANGE THIS FUNCTION
    pc = start
    result = ""
    while True:
        instruction = memory[pc]
        if instruction == 0:
            # Stop
            break
        else:
            result = result + chr(memory[instruction])
        pc = pc + 1
    print(result)


def main():
    memory = array.array('L', [0] * 2 ** 18)
    start = random.randint(0, 250000)

    with open("relocatable.dat", "rb") as data:
        program = pickle.load(data)
        fixups = pickle.load(data)

    load(memory, program, start, fixups)
    run(memory, start)


if __name__ == "__main__":
    main()
