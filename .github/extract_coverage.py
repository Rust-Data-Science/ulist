import re
import subprocess


def run() -> None:
    # Score
    with open("../htmlcov/index.html", "r") as file:
        text = file.read()
    start = text.index("total")
    text = text[start:]
    score = int(re.findall('[0-9]+\.?[0-9]+%{1}', text)[0].replace('%', ''))
    print(f"The coverage is {score}%!")
    subprocess.run([f'echo "total={score}%" >> $GITHUB_ENV'], shell=True)

    # Color
    if score < 70:
        badge_color = 'red'
    elif score < 80:
        badge_color = 'orange'
    elif score < 90:
        badge_color = 'yellow'
    else:
        badge_color = 'green'
    subprocess.run(
        [f'echo "badge_color={badge_color}" >> $GITHUB_ENV'], shell=True)

    print("Result saved into `GITHUB_ENV`!")


if __name__ == "__main__":
    run()
