# Install SQLite system wide in Raspberry Pi 500 or Compute Module 4 (CM4) usint "sudo apt-get install sqlite3" command

## Standard Python libraries
import time                         # https://docs.python.org/3/library/time.html
import argparse # TODO

import subprocess                   # https://docs.python.org/3/library/subprocess.html
from subprocess import Popen, PIPE  # TODO
from subprocess import check_call   # TODO


## 3rd party libraries
# Peek makes printing debug information  easy and adds basic benchmarking functionality. See https://salabim.org/peek/
# pip install peek-python
import peek

## Internal libraries
import * from EngineSoundGenerator
import GlobalConstants as GC


def intergration_test():
    pass

def main():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run program in DEV, TESTING, or PRODUCTION mode?")
    parser.add_argument(
        '--mode', 
        nargs='+', 
        choices=['DEV', 'TESTING', 'a PRODUCTION'], 
        help='Configure state of GC.DEBUG_STATEMENTS_ON and wheter intergration_test() or main() is called.'
    )
    args = parser.parse_args()

    if 'DEV' in args.mode:
        pass
        # TODO peek().???
    elif 'TESTING' in args.mode:
        intergration_test()
    elif 'PRODUCTION' in args.mode:
        main():
    else:
        # Invalid mode argument should allow normal production code execution
        main()




    