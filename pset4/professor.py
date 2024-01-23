import random
import sys

# generate 10 math problems
def main():
    score = 0
    n = get_level()
    for _ in range(10):
        x, y = generate_integer(n)
        for i in range(3):
            try:
                answ = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if i == 2:
                    print(f"{x} + {y} = {x+y}")
                continue
            else:
                if answ == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {x+y}")
                    continue
    print(f"Score: {score}", end="\n")
    sys.exit()
            
# ask user for a number between 1 and 3: n
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
            else:
                raise ValueError
        except ValueError:
            continue
            
# generate values
# digits of x and y are == n
def generate_integer(level):
    if level == 1:
        min_value = 0
    else:
        min_value = 10**(level-1)
    max_value = 10**level - 1
    x = random.randint(min_value, max_value)
    y = random.randint(min_value, max_value)
    return x, y
        
if __name__ == "__main__":
    main()