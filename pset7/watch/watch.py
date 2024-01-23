import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        link = re.search(
            r'<iframe(?: width="560" height="315")? src="https?://(?:www\.)?youtu\.?be(?:\.com)?/embed/(xvFZjo5PgG0)"(?: title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>',
            s,
        )
        return f"https://youtu.be/{link.group(1)}"
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
