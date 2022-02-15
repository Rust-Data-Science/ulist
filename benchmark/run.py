from integer import ArraySum
import platform
import ulist as ul
import numpy as np

if __name__ == "__main__":
    print("Benchmarking...")
    print()

    line = "=" * 32
    print(line)
    print("System OS:", platform.system())
    print("Ulist version:", ul.__version__)
    print("Numpy version:", np.__version__)
    print(line)
    print()

    result = ArraySum().run()
    line = "-" * 128
    print(line)
    print(result.name, result.dtype, result.scores)
    print(line)
