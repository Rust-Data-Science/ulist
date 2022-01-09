import re
import subprocess


def run() -> None:
    with open("../htmlcov/index.html", "r") as file:
        text = file.read()
    start = text.index("total")
    text = text[start:]
    result = re.findall('[0-9]+\.?[0-9]+%{1}', text)[0]
    print(f"The coverage is {result}!")

    subprocess.run([f'echo "total={result}" >> $GITHUB_ENV'])
    print("Result saved into `GITHUB_ENV`!")


if __name__ == "__main__":
    run()
