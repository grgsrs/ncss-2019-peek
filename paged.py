from __future__ import print_function

import array
import pickle
import random

PAGESIZE = 1024


def translate(address, tlb):
    """Return address translated according to the supplied TLB"""
    # IMPLEMENT ME


def load(memory, program, start, tlb):
    """Load program into memory from the given start address."""
    # IMPLEMENT ME


def run(memory, start, tlb):
    """Runs the program in memory beginning at start."""
    # DO NOT CHANGE THIS FUNCTION
    pc = start
    result = ""
    while True:
        instruction = memory[translate(pc, tlb)]
        if instruction == 0:
            # Stop
            break
        else:
            result = result + chr(memory[translate(instruction + start, tlb)])
        pc = pc + 1
    print(result)


def main():
    memory = array.array('H', [0] * 2 ** 19)
    start = random.choice([i * PAGESIZE for i in range(2**19 // 1024)])
    pages = random.sample([i * PAGESIZE for i in range(2**19 // 1024)], 2**19 // 1024)
    tlb = dict((i * PAGESIZE, pages[i]) for i in range(2**19 // 1024))

    with open("paged.dat", "rb") as data:
        program = pickle.load(data)

    load(memory, program, start, tlb)
    run(memory, start, tlb)


if __name__ == "__main__":
    main()
