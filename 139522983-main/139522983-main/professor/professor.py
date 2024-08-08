import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x, y = generate_integer(level)
        ans = x + y
        tr = 0
        while tr < 3:
            try:
                n = int(input(f"{x} + {y} = "))
                if n == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    tr += 1
            except ValueError:
                print("EEE")
                tr += 1
        if tr == 3:
            print(f"{x} + {y} = {ans}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)


if __name__ == "__main__":
    main()
