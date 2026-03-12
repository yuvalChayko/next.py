import functools

def double_letter(word):
    return "".join(list(map(lambda x: x+x, word)))


def four_dividers(number):
    return list(filter(lambda x: x%4 == 0, range(1, number+1)))


def sum_of_digits(number):
    return functools.reduce(lambda x,y: int(x)+int(y), str(number))

def main():
    print(double_letter("hello"))
    print(four_dividers(9))
    print(sum_of_digits(104))
if __name__ == "__main__":
    main()