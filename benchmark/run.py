import gc
import platform
import subprocess
import sys
from datetime import datetime
from inspect import isclass
from itertools import chain

import numpy as np
import ulist as ul
from ulist.utils import Benchmarker

import boolean as BOOL
import floating as F32
import integer as I32
import strings as STR


def _get_processor_name() -> str:
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        command = "sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command, shell=True).strip().decode()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep 'model name' | uniq"
        return subprocess.check_output(command, shell=True).strip().decode().split(":")[1]
    return ""


def display_info() -> None:
    print("Info:  ")
    line = "*" * 60
    print(line)
    print("Date:", datetime.today().strftime("%Y-%m-%d %H:%M:%S"), "  ")
    print("System OS:", platform.system(), "  ")
    print("CPU:", _get_processor_name(), "  ")
    print("Python version:", sys.version.split()[0], "  ")

    try:
        print("Ulist version:", ul.__version__, "  ")
    except:
        print("Ulist version:", "unknown")
    print("Numpy version:", np.__version__, "  ")
    print(line)
    print()


def display_result():
    print("Result:")
    print()
    n_wins = 0
    total = 0
    iterator = chain(
        I32.__dict__.values(),
        F32.__dict__.values(),
        BOOL.__dict__.values(),
        STR.__dict__.values(),
    )
    for cls in iterator:
        if not isclass(cls):
            continue
        if cls is Benchmarker:
            continue
        if issubclass(cls, Benchmarker):
            result = cls().run()
            if total == 0:
                result.display()
            else:
                result.display(False)
            if result.scores[-1] == 'Y':
                n_wins += 1
            total += 1
        gc.collect()
    print()
    print(f"{n_wins} of {total} tasks are faster!")


def main():
    """
    Comparing Ulist and Numpy performances, show the server info and output
    the result as Markdown Table.
    """
    print("GC disabled...")
    gc.disable()
    print("Benchmarking...\n")
    display_info()
    display_result()
    print("GC enabled...")
    gc.enable()


if __name__ == "__main__":
    main()
