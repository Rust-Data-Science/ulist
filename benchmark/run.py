from integer import ArraySum
import platform
import ulist as ul
import numpy as np
from datetime import datetime


def main():
    """
    Comparing Ulist and Numpy performances, and output the
    result as Markdown Table.
        Item - The task to compare the performances.
        Dtype - The array element type.
        Sample Vol. - {XS: 100, S: 1k, M: 10k, L: 100k, XL: 1M}.
    """
    print("Benchmarking...")
    print()

    print("Info:")
    line = "=" * 60
    print(line)
    print("Date:", datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    print("System OS:", platform.system())
    try:
        print("Ulist version:", ul.__version__)
    except:
        print("Ulist version:", "unknown")
    print("Numpy version:", np.__version__)
    print(line)
    print()

    print("Result:")
    print()
    result = ArraySum().run()
    result.display()
    print()


if __name__ == "__main__":
    main()
