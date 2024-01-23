import emoji

def main():
    text_emoji = input("Input: ")
    print(f"Output: {emoji.emojize(text_emoji, language='alias')}")
    
main()