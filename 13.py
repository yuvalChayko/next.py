def intersection(list_1, list_2):
    return list(set([x for x in list_1 if x in list_2]))


def is_prime(number):
    return not ([x for x in range(2, number) if number%x == 0])


def is_funny(string):
    return not ([x for x in string if x != "h" and x != "a"])


def get_password(password):
    return "".join([chr(ord(x)+2) for x in password])


def main():
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
    print(is_prime(42))
    print(is_prime(43))
    print(is_funny("hahahahahaha"))
    print(get_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))


if __name__ == "__main__":
    main()