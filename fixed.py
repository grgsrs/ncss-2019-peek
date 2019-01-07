from __future__ import print_function

import array
import pickle


def load(memory, program, start):
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
    memory = array.array('H', [0] * 2 ** 14)

    with open("fixed.dat", "rb") as data:
        program = pickle.load(data)
        start = pickle.load(data)

    load(memory, program, start)
    run(memory, start)


if __name__ == "__main__":
    main()
