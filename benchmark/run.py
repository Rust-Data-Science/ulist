import gc
import platform
import sys
from datetime import datetime
from inspect import isclass
from itertools import chain

import numpy as np
import ulist as ul

import floating as F32
import integer as I32


def display_info() -> None:
    print("Info:")
    line = "=" * 60
    print(line)
    print("Date:", datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    print("System OS:", platform.system())
    print("Python version:", sys.version.split()[0])

    try:
        print("Ulist version:", ul.__version__)
    except:
        print("Ulist version:", "unknown")
    print("Numpy version:", np.__version__)
    print(line)
    print()


def display_result():
    print("Result:")
    print()
    i = 0
    iterator = chain(
        I32.__dict__.values(),
        F32.__dict__.values(),
    )
    for cls in iterator:
        if not isclass(cls):
            continue
        if cls is I32.Benchmarker:
            continue
        if issubclass(cls, I32.Benchmarker):
            result = cls().run()
            if i == 0:
                result.display()
            else:
                result.display(False)
            i += 1
        gc.collect()
    print()


def main():
    """
    Comparing Ulist and Numpy performances, and output the
    result as Markdown Table.
        Item - The task to compare the performances.
        Dtype - The array element type.
        Sample Vol. - {XS: 100, S: 1k, M: 10k, L: 100k, XL: 1M}.
    """
    print("GC disabled...")
    gc.disable()
    print("Benchmarking...\n")
    display_info()
    # display_result()
    print("GC enabled...")
    gc.enable()


if __name__ == "__main__":
    main()
