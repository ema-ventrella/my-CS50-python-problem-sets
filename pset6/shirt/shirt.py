import sys
from PIL import Image, ImageOps
import os


def main():
    extensions = [".jpeg", ".png", ".jpg"]
    extension_before = os.path.splitext(sys.argv[1])[1]
    extension_after = os.path.splitext(sys.argv[2])[1]
    if (
        len(sys.argv) == 3
        and (extension_before in extensions)
        and (extension_after in extensions)
        and (extension_before == extension_after)
    ):
        try:
            img = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            img = ImageOps.fit(img, shirt.size)
            img.paste(shirt, shirt)
            img.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("File not found")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif extension_before != extension_after:
        sys.exit("Input and output have different extensions")
    elif (extension_before not in extensions) or (extension_after not in extensions):
        sys.exit("Invalid input")


if __name__ == "__main__":
    main()
