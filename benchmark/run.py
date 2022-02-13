from integer import ArraySum

if __name__ == "__main__":
    print("Benchmarking...")
    result = ArraySum().run()
    print(result.name, result.dtype, result.scores)
