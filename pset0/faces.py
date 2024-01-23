def main():
    text = input("")
    converted_text = convert(text)
    print(converted_text)

def convert(i):
    i = i.replace(":)", "🙂")
    i = i.replace(":(", "🙁")
    return i

main()
