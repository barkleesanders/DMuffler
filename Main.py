#!/usr/bin/env python3
"""
__authors__    = ["Blaze Sanders"]
__email__      = ["dev@blazesanders.com"]
__license__    = "MIT"
__status__     = "Development"
__deprecated__ = "False"
__version__    = "2025.0"
__doc__        = "Code entry point for DMuffler embedded application"
"""

## Standard Python libraries
import time                         # https://docs.python.org/3/library/time.html
import argparse 		    # https://docs.python.org/3/library/argparse.html
import subprocess                   # https://docs.python.org/3/library/subprocess.html
from subprocess import Popen, PIPE  # https://docs.python.org/3/library/subprocess.html#subprocess.Popen
from subprocess import check_call   # https://docs.python.org/3/library/subprocess.html#subprocess.check_call

## 3rd party libraries
# Peek makes printing debug information easy and adds basic benchmarking functionality (see https://salabim.org/peek)
# pip install peek-python
try:
    from peek import peek  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    def peek(message: str, **_kwargs) -> None:
        """Fallback debug printer when :mod:`peek` is unavailable."""
        print(message)

## Internal libraries
#TODO from EngineSoundGenerator import *
import GlobalConstants as GC


def integration_test():
    """
    https://en.wikipedia.org/wiki/Integration_testing

    """
    pass


def main():
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run DMuffler application in DEV, TESTING, or PRODUCTION mode?")
    parser.add_argument(
        "--mode",
        choices=["DEV", "TESTING", "PRODUCTION"],
        default="PRODUCTION",
        help="Configure state of GC.DEBUG_STATEMENTS_ON and whether integration_test() or main() is called."
    )

    args = parser.parse_args()

    if args.mode == "DEV":
        peek("DMuffler booting in DEV mode", color="red")
        peek("Install SQLite system wide on Raspberry Pi Compute Module 4 using:", color="yellow")
        peek("sudo apt install sqlite3", color="white")

    elif args.mode == "TESTING":
        peek("DMuffler booting in TESTING mode", color="red")
        integration_test()

    elif args.mode == "PRODUCTION":
        peek("DMuffler booting in standard PRODUCTION mode", color="green")
        main()
