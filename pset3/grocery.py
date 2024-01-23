def main():
    grocery_list = []
    while True:
        try:
            item = input("").upper().strip()
        except EOFError:
            grocery_list.sort()
            note(grocery_list)
            break
        else:
            grocery_list.append(item)
            continue
    
def note(note):
    check_list = []
    for i in note:
        if i not in check_list:
            check_list.append(i)
            count = note.count(i)
            print(count, i)
        else:
            pass

main()