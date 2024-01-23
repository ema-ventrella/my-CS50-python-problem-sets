def main():
    text = input("Input: ")
    r_text = shorten(text)
    print(f"Output: {r_text}")
    
def shorten(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    r_text = ""
    for l in text:
        if l not in vowels:
            r_text += l
        else:
            continue
    return r_text
    
if __name__ == "__main__":   
    main()