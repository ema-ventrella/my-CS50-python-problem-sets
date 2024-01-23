def main():
    file = input("File name: ").strip()
    typefile(file)

def typefile(i):
    if i.endswith(".gif"):
        print("image/gif")
    elif i.endswith(".jpg") or i.endswith(".jpeg"):
        print("image/jpeg")
    elif i.endswith(".png"):
        print("image/png")
    elif i.endswith(".img"):
        print("image/img")
    elif i.endswith(".pdf") or i.endswith(".PDF"):
        print("application/pdf")
    elif i.endswith(".txt"):
        print("text/plain")
    elif i.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
