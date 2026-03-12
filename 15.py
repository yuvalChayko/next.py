import functools

def main():
    with open("names.txt", "r") as f:
        names = f.read().split("\n")[:-1]

    # 1
    print(functools.reduce(lambda name1, name2: name1 if len(name1) > len(name2) else name2, names))
    # 2
    print(len("".join(names)))
    # 3
    print("\n".join(x for x in names if len(x) == len(sorted(names, key=len)[0])))
    # 4
    with open("name_length.txt", "w") as f:
        f.write("\n".join([str(len(x)) for x in names]))
    # 5
    length = int(input("enter length of name: "))
    print("\n".join(filter(lambda x: len(x) == length, names)))

if __name__ == "__main__":
    main()