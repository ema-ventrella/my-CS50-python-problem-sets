def main():
    text = input("Input: ")
    r_text = r_remove(text)
    print(f"Output: {r_text}")
    
def r_remove(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    r_text = ""
    for l in text:
        if l not in vowels:
            r_text += l
        else:
            continue
    return r_text
        
main()