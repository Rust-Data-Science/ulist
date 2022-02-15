from integer import ArraySum
import platform
import ulist as ul
import numpy as np
from datetime import datetime

if __name__ == "__main__":
    print("Benchmarking...")
    print()

    print("Info:")
    line = "=" * 32
    print(line)
    print("Date:", datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    print("System OS:", platform.system())
    print("Ulist version:", ul.__version__)
    print("Numpy version:", np.__version__)
    print(line)
    print()

    print("Result:")
    print()
    result = ArraySum().run()
    result.display()
    print()
